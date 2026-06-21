# 🧠 NeuroPulse — AI-Powered Brain Stroke Detection & Health Monitoring System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-black)
![SQLite](https://img.shields.io/badge/SQLite-Database-green)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![HealthCare](https://img.shields.io/badge/Domain-Healthcare-red)

A smart healthcare platform that uses Machine Learning to assess brain stroke risk, maintain patient records, provide stroke awareness resources, and support hospital registration through a secure web application.

---

# 🚀 Features

* 🧠 AI-Based Brain Stroke Prediction using Machine Learning
* 👤 Secure User Registration & Login System
* 📊 Prediction History Tracking
* 🏥 Hospital Registration Portal
* 📰 Health News & Stroke Awareness Section
* 🔐 Session-Based Authentication
* 📁 Database Storage for Users & Predictions
* 📈 Instant Prediction Results
* 🎨 Responsive User Interface
* ⚡ Fast Flask-Based Backend

---

# ⚙️ Tech Stack

| Layer            | Technology              |
| ---------------- | ----------------------- |
| Backend          | Flask (Python)          |
| Frontend         | HTML5, CSS3, JavaScript |
| Database         | SQLite                  |
| Machine Learning | Scikit-Learn            |
| Authentication   | Flask Sessions          |
| UI Design        | Bootstrap               |

---

# 🔗 Brain Stroke Prediction Flow

### USER FLOW

User Registration/Login

→ Enter Health Information

→ Submit Prediction Request

→ Machine Learning Model Analysis

→ Stroke Risk Prediction Generated

→ Results Displayed

→ History Stored in Database

---

### HOSPITAL FLOW

Hospital Registration

→ Submit Hospital Information

→ Registration Stored

→ Hospital Dashboard Access

---

### HEALTH AWARENESS FLOW

User Opens Health News

→ Reads Stroke Awareness Articles

→ Learns Prevention & Safety Measures

---

# 👥 Roles & Access

| Role                 | Access                                             |
| -------------------- | -------------------------------------------------- |
| User                 | Register, Login, Predict Stroke Risk, View History |
| Hospital             | Register Hospital Information                      |
| Admin (Future Scope) | Manage Users, Hospitals & Reports                  |

---

# 🛠️ Local Setup

## 1. Clone the Repository

```bash
git clone https://github.com/ujjwalkatare/Brain-Stroke.git
cd Brain-Stroke
```

## 2. Create Virtual Environment

```bash
python -m venv env

env\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run Application

```bash
python app.py
```

## 5. Open Browser

```text
http://127.0.0.1:5000
```

---

# 📂 Project Structure

```text
Brain-Stroke/
│
├── app.py
├── app.spec
├── README.md
├── .gitignore
│
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
└── instance/
```

---

# 📦 Requirements

```text
Flask
NumPy
Pandas
Scikit-Learn
Werkzeug
SQLite
```

Install:

```bash
pip install flask numpy pandas scikit-learn werkzeug
```

---

# 🔒 Environment Notes

* Do not upload virtual environments to GitHub
* Do not upload database files
* Store sensitive credentials using environment variables
* Keep large ML model files outside GitHub repositories

---

# 💡 How Prediction Works

### 1. User enters health-related information

↓

### 2. Machine Learning model processes the data

↓

### 3. Stroke risk probability is calculated

↓

### 4. Prediction result is displayed

↓

### 5. Prediction history is stored for future reference

---

# 🎯 Future Improvements

* Doctor Dashboard
* Admin Panel
* PDF Medical Reports
* Email Notifications
* Cloud Database Integration
* Deep Learning-Based MRI Analysis

---

# 👨‍💻 Author

### Ujjwal Katare

Python Developer | Flask Developer | Machine Learning Enthusiast

---

# ⭐ Give a Star

If this project helped you or you found it interesting, please consider giving it a ⭐ on GitHub!
