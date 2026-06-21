# 🧠 NeuroPulse — AI-Powered Brain Stroke Detection System

A Flask-based web application that helps users assess brain stroke risk using machine learning. The platform provides stroke prediction, health awareness resources, hospital registration, and prediction history tracking through a clean and user-friendly interface.

---

## 🚀 Features

* 🧠 AI-Based Stroke Prediction — Predict stroke risk using a trained machine learning model
* 👤 User Authentication — Secure user registration and login system
* 🏥 Hospital Registration Module — Hospitals can register and manage access
* 📊 Prediction History — View previous prediction records
* 📰 Health News Section — Access stroke-related health information and awareness content
* 🎨 Responsive UI — Clean and mobile-friendly interface
* 🔐 Session Management — Secure login and authenticated access
* 📁 Database Storage — Stores user and prediction information

---

## ⚙️ Tech Stack

| Layer            | Technology               |
| ---------------- | ------------------------ |
| Backend          | Flask (Python)           |
| Frontend         | HTML, CSS, JavaScript    |
| Database         | SQLite                   |
| Machine Learning | Scikit-Learn             |
| Authentication   | Flask Session Management |

---

## 🔗 How It Works

### STROKE PREDICTION FLOW

User Login/Register
→ Enter Health Information
→ ML Model Processes Input
→ Stroke Risk Prediction Generated
→ Result Displayed to User
→ Prediction Stored in History

### HOSPITAL REGISTRATION FLOW

Hospital Registration
→ Submit Details
→ Account Created
→ Access Dashboard Features

### HEALTH NEWS FLOW

User Opens Health News
→ Fetch Stroke Awareness Content
→ Display Latest Health Information

---

## 🛠️ Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ujjwalkatare/Brain-Stroke.git
cd Brain-Stroke
```

### 2. Create Virtual Environment

```bash
python -m venv env
env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

```text
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```text
Brain-Stroke/
│
├── app.py
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── predict.html
│   ├── result.html
│   ├── history.html
│   ├── hospital-register.html
│   ├── health_news.html
│   └── second_dashboard.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📦 Requirements

```text
Flask
scikit-learn
numpy
pandas
joblib
werkzeug
```

Install:

```bash
pip install -r requirements.txt
```

---

## 🎯 Key Modules

### User Management

* User Registration
* User Login
* Session Handling

### Stroke Prediction

* ML-Based Prediction
* Risk Assessment
* Prediction Storage

### Hospital Management

* Hospital Registration
* Data Management

### Health Awareness

* Stroke Information
* Health News Content

---

## ⚠️ Notes

* Do not commit database files or virtual environments
* Use environment variables for sensitive configuration
* Keep machine learning model files outside GitHub if they are large
* This project is intended for educational and research purposes

---

## 👨‍💻 Author

**Ujjwal Katare**

---

## ⭐ Give a Star

If you found this project useful or interesting, please consider giving it a ⭐ on GitHub.
