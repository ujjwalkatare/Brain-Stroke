import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import CustomObjectScope
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
from PIL import Image
import cv2
from flask_bcrypt import Bcrypt
import sys
import pymysql
from flask_mysqldb import MySQL
import requests
from datetime import datetime  

# Ensure the app uses UTF-8 encoding to prevent UnicodeEncodeError
sys.stdout.reconfigure(encoding='utf-8')

# Initialize the Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Folder to store uploaded images
app.secret_key = 'supersecretkey'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
bcrypt = Bcrypt(app)

# Database configuration (replace with your actual database details)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'mydatabase'

# Initialize MySQL
mysql = MySQL(app)

# User database (for demonstration purposes, replace with a proper database in production)
users = {}

# Define your custom layers
class ChannelAttention(tf.keras.layers.Layer):
    def __init__(self, ratio=8, **kwargs):
        super(ChannelAttention, self).__init__(**kwargs)
        self.ratio = ratio
    
    def build(self, input_shape):
        self.shared_layer_one = tf.keras.layers.Dense(input_shape[-1] // self.ratio, activation='relu', kernel_initializer='he_normal', use_bias=True, bias_initializer='zeros')
        self.shared_layer_two = tf.keras.layers.Dense(input_shape[-1], kernel_initializer='he_normal', use_bias=True, bias_initializer='zeros')
        super(ChannelAttention, self).build(input_shape)

    def call(self, inputs):
        avg_pool = tf.keras.layers.GlobalAveragePooling2D()(inputs)    
        avg_pool = tf.keras.layers.Reshape((1, 1, inputs.shape[-1]))(avg_pool)
        avg_pool = self.shared_layer_one(avg_pool)
        avg_pool = self.shared_layer_two(avg_pool)
        
        max_pool = tf.keras.layers.GlobalMaxPooling2D()(inputs)
        max_pool = tf.keras.layers.Reshape((1, 1, inputs.shape[-1]))(max_pool)
        max_pool = self.shared_layer_one(max_pool)
        max_pool = self.shared_layer_two(max_pool)
        
        attention = tf.keras.layers.add([avg_pool, max_pool])
        attention = tf.keras.activations.sigmoid(attention)
        return tf.keras.layers.multiply([inputs, attention])

class SpatialAttention(tf.keras.layers.Layer):
    def __init__(self, kernel_size=7, **kwargs):
        super(SpatialAttention, self).__init__(**kwargs)
        self.kernel_size = kernel_size

    def build(self, input_shape):
        self.conv = tf.keras.layers.Conv2D(1, self.kernel_size, padding='same', activation='sigmoid', kernel_initializer='he_normal', use_bias=False)
        super(SpatialAttention, self).build(input_shape)
    
    def call(self, inputs):
        avg_pool = tf.reduce_mean(inputs, axis=-1, keepdims=True)
        max_pool = tf.reduce_max(inputs, axis=-1, keepdims=True)
        attention = tf.concat([avg_pool, max_pool], axis=-1)
        attention = self.conv(attention)
        return tf.keras.layers.multiply([inputs, attention])

# Load the saved model with custom objects
MODEL_PATH = r"D:\code\python\ML\Brain stock project\Brain Data\brain_stroke_detection_model.h5"
with CustomObjectScope({'ChannelAttention': ChannelAttention, 'SpatialAttention': SpatialAttention}):
    model = load_model(MODEL_PATH, compile=False)

# Utility function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to preprocess the uploaded image
def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.resize((224, 224))  # Resize to match the input size of the model
    image = image.convert('RGB')  # Convert to RGB if it's not
    image = np.array(image)  # Convert image to numpy array
    image = cv2.medianBlur(image, 5)  # Apply median blur (optional)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image, np.array(image)  # Return both the preprocessed image and original image for display

# Home route
@app.route('/')
def index():
    return render_template('index.html', message="Upload an Image for Prediction")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username already exists in the database
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE username = %s', (username,))
        existing_user = cur.fetchone()

        if existing_user:
            flash('User already exists! Please choose another username.', 'danger')
            return redirect(url_for('register'))

        # Insert new user into the database (plaintext password)
        cur.execute('INSERT INTO users (username, password) VALUES (%s, %s)', 
                    (username, password))
        mysql.connection.commit()
        cur.close()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')  # Use .get() to avoid KeyError
        password = request.form.get('password')  # Use .get() to avoid KeyError

        if not username or not password:
            flash('Username and password are required!', 'danger')
            return redirect(url_for('login'))

        # Fetch user details from the database
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cur.fetchone()  # Fetch user record
        cur.close()

        if user:  # Check if user exists
            if password == user[1]:  # Compare plaintext passwords directly
                session['username'] = user[0]  # Store username in session
                flash('Login successful!', 'success')
                return redirect(url_for('second_dashboard'))  # Redirect to the second dashboard
            else:
                flash('Incorrect password! Please try again.', 'danger')
        else:
            flash('Username not found! Please try again.', 'danger')

        return redirect(url_for('login'))

    return render_template('login.html')

# Dashboard route (second dashboard after successful login)
@app.route('/second_dashboard')
def second_dashboard():
    if 'username' not in session:
        flash('You need to log in first!')
        return redirect(url_for('login'))
    
    return render_template('second_dashboard.html', username=session['username'])

# Hospital Register form
@app.route('/hospital-register', methods=['GET', 'POST'])
def second_register():
    if request.method == 'POST':    
        firstname = request.form['firstname']
        surname = request.form['surname']
        username = session['username']
        email = request.form['email']
        phonenumber = request.form['phonenumber']
        dateofbirth = request.form['dateofbirth']
        gender = request.form['gender']
        session['firstname']=firstname
        
        # Save to the database
        cursor = mysql.connection.cursor()  # Use the initialized mysql instance
        cursor.execute("""INSERT INTO user (firstname, surname, username, email, phonenumber, dateofbirth, gender)
                          VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                       (firstname, surname, username, email, phonenumber, dateofbirth, gender))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('predict'))

    return render_template('hospital-register.html')


# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out successfully.')
    return redirect(url_for('index'))

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # Check if the user is logged in
    if 'firstname' not in session:
        flash('Please register this page.')
        return redirect(url_for('hospital-register'))

    # Retrieve the user's details from the database
    firstname = session['firstname']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT firstname, surname, username, phonenumber, dateofbirth, gender FROM user WHERE firstname = %s", (firstname,))
    user_info = cursor.fetchone()  # Fetch user details
    cursor.close()

    # If the request method is POST (i.e., when the user submits the form)
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # Secure the filename and create the file path
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # Ensure the uploads folder exists
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])

            # Save the uploaded file
            file.save(file_path)

            # Preprocess the image and make the prediction
            x_new, original_image = preprocess_image(file_path)
            y_pred_new = model.predict(x_new)
            y_pred_new_label = [1 if i >= 0.5 else 0 for i in y_pred_new]

            # Determine the result based on the prediction
            result = "Stroke" if y_pred_new_label[0] == 1 else "Normal"

            # Get the current timestamp for the result
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Store the prediction result, image path, and timestamp in the 'result' table
            cursor = mysql.connection.cursor()
            cursor.execute("""
                INSERT INTO result (firstname, surname, username, phonenumber, dateofbirth, gender, prediction_result, image_path, timestamp) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, 
                (user_info[0], user_info[1], user_info[2], user_info[3], user_info[4], user_info[5], result, file_path, current_time))
            mysql.connection.commit()
            cursor.close()

            # Pass the user's details along with the result and image path to the result page
            return render_template('result.html', label=result, img_path=filename, user_info=user_info)

        else:
            flash('Allowed file types are png, jpg, jpeg')
            return redirect(request.url)

    # Render the prediction form if the request method is GET
    return render_template('predict.html')

# History Page
@app.route('/history')
def display_history():
    cur = mysql.connection.cursor()
    # Fetch user data along with the latest prediction without duplicates
    cur.execute("""
        SELECT u.firstname, u.surname, u.username, u.phonenumber, u.dateofbirth, 
               u.email, 
               COUNT(r.prediction_result) AS total_predictions,
               MAX(r.prediction_result) AS latest_result,
               MAX(r.gender) AS latest_gender,
               MAX(r.image_path) AS latest_image,
               MAX(r.timestamp) AS latest_timestamp 
        FROM user u 
        LEFT JOIN result r ON u.firstname = r.firstname
        GROUP BY u.firstname
        ORDER BY latest_timestamp DESC
    """)
    data = cur.fetchall()
    cur.close()

    # Convert the fetched data to a format that Jinja can iterate over
    history = []
    for row in data:
        history.append({
            'firstname': row[0],
            'surname': row[1],
            'username': row[2],
            'phonenumber': row[3],
            'dateofbirth': row[4],
            'email': row[5],  # Include email
            'total_predictions': row[6],
            'latest_result': row[7],
            'latest_gender': row[8],
            'latest_image': row[9],
            'latest_timestamp': row[10]
        })

    # Pass the history data to the template
    return render_template('history.html', history=history)




# Function to fetch news from the provided API URL
# Function to fetch health-related news from the provided API URL
def get_health_news():
    api_url = 'https://newsapi.org/v2/everything?q=health+OR+medical+OR+healthcare&from=2024-09-14&sortBy=publishedAt&apiKey=4391178cc26e44b4a0e08791bf3e55da'
    response = requests.get(api_url)

    # Check if the API call was successful
    if response.status_code == 200:
        news_data = response.json()
        return news_data.get('articles', [])
    else:
        return []

# Route to display the health-related news
@app.route('/health-news')
def display_health_news():
    articles = get_health_news()  # Fetch the health news articles
    return render_template('health_news.html', articles=articles)



# Run the app
if __name__ == '__main__':
    app.run(debug=True)