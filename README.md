# 🧠 NeuroPulse — AI-Powered Brain Stroke Detection & Health Monitoring System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-black)
![SQLite](https://img.shields.io/badge/SQLite-Database-green)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![HealthCare](https://img.shields.io/badge/Domain-Healthcare-red)

A smart healthcare platform that uses Machine Learning to assess brain stroke risk, maintain patient records, provide stroke awareness resources, and support hospital registration through a secure web application.


## 🚀 Features

- 🧠 AI-based brain stroke prediction using Machine Learning
- 👤 Secure user registration & login system
- 📊 Prediction history tracking
- 🏥 Hospital registration portal
- 📰 Health news & stroke awareness section
- 🔐 Session-based authentication
- 📁 Database storage for users & predictions
- 📈 Instant prediction results
- 🎨 Responsive user interface
- ⚡ Fast Flask-based backend

---

## ⚙️ Tech Stack

| Layer            | Technology              |
|------------------|--------------------------|
| Backend          | Flask (Python)           |
| Frontend         | HTML5, CSS3, JavaScript  |
| Database         | SQLite                   |
| Machine Learning | Scikit-Learn              |
| Authentication   | Flask Sessions             |
| UI Design        | Bootstrap                  |

---

## 💡 How Prediction Works

1. User enters health-related information
2. Machine Learning model processes the data
3. Stroke risk probability is calculated
4. Prediction result is displayed
5. Prediction history is stored for future reference

---

## 🔗 User Flows

### 👤 User Flow
```
Register / Login
   → Enter Health Information
   → Submit Prediction Request
   → ML Model Analysis
   → Stroke Risk Prediction Generated
   → Results Displayed
   → History Stored in Database
```

### 🏥 Hospital Flow
```
Hospital Registration
   → Submit Hospital Information
   → Registration Stored
   → Hospital Dashboard Access
```

### 📰 Health Awareness Flow
```
User Opens Health News
   → Reads Stroke Awareness Articles
   → Learns Prevention & Safety Measures
```

---

## 👥 Roles & Access

| Role                  | Access                                              |
|------------------------|------------------------------------------------------|
| User                   | Register, login, predict stroke risk, view history  |
| Hospital                | Register hospital information                       |
| Admin *(Future Scope)* | Manage users, hospitals & reports                    |

---

## 🛠️ Local Setup

**1. Clone the repository**
```bash
git clone https://github.com/ujjwalkatare/Brain-Stroke.git
cd Brain-Stroke
```

**2. Create a virtual environment**
```bash
python -m venv env
env\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the application**
```bash
python app.py
```

**5. Open in browser**
```
http://127.0.0.1:5000
```

---

## 📂 Project Structure

```
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

## 📦 Requirements

```
Flask
NumPy
Pandas
Scikit-Learn
Werkzeug
SQLite
```

Install all at once:
```bash
pip install flask numpy pandas scikit-learn werkzeug
```

---

## 🔒 Environment Notes

> ⚠️ **Before pushing to GitHub:**
- Do not upload virtual environments
- Do not upload database files
- Store sensitive credentials using environment variables
- Keep large ML model files outside the repository

---

## 🎯 Future Improvements

- [ ] Doctor Dashboard
- [ ] Admin Panel
- [ ] PDF Medical Reports
- [ ] Email Notifications
- [ ] Cloud Database Integration
- [ ] Deep Learning-Based MRI Analysis

---

## 👨‍💻 Author

**Ujjwal Katare**
Python Developer | Flask Developer | Machine Learning Enthusiast

---

## ⭐ Give a Star

If this project helped you or you found it interesting, please consider giving it a ⭐ on GitHub!
