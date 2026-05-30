# 📚 StudySync – Collaborative Virtual Study Room Platform

### A Real-Time Productivity & Collaboration Platform for Students

StudySync is a modern virtual study room platform that enables students to study together, track productivity, and communicate in real time within distraction-free study environments.

The platform combines **real-time communication**, **study session tracking**, **private/public study rooms**, and **activity analytics** to create an engaging online study experience.

---

## 🚀 Key Features

### 🔐 Secure Authentication

* User registration and login
* Password protection
* Session management
* Secure access control

### 🏠 Study Rooms

* Create public or private study rooms
* Unique room invite codes
* Join existing study groups
* Collaborative learning environment

### 💬 Real-Time Chat

* Instant messaging using WebSockets
* Live communication inside study rooms
* Group discussions and doubt solving
* Real-time updates without page refresh

### ⏱️ Study Session Timer

* Built-in productivity timer
* Track active study duration
* Session history management
* Monitor learning consistency

### 📊 Activity Dashboard

* Total study hours tracked
* Joined room statistics
* Recent study activity
* Productivity overview

### 📱 Responsive User Interface

* Mobile-friendly design
* Modern dashboard
* Clean user experience
* Optimized for desktop and mobile devices

---

# 🏗️ System Architecture

```text
User Authentication
        │
        ▼
Study Room Creation / Join
        │
        ▼
Real-Time Socket.IO Communication
        │
        ▼
Study Session Tracking
        │
        ▼
SQLite Database Storage
        │
        ▼
Dashboard Analytics
```

---

# 📸 Screenshots

## 🏠 Home Page

<img width="912" height="436" alt="image" src="https://github.com/user-attachments/assets/2933e556-1239-4b7d-8c4f-c74f510574c6" />

---

## 📚 Study Room Interface

<img width="927" height="404" alt="image" src="https://github.com/user-attachments/assets/e0539fab-0cb7-4a49-81d8-0d39251803de" />


## 💬 Real-Time Chat

<img width="908" height="431" alt="image" src="https://github.com/user-attachments/assets/243f2ca9-4204-4cb5-8f85-c7672fd3655a" />

---

## 📊 User Dashboard

<img width="915" height="434" alt="image" src="https://github.com/user-attachments/assets/365eb99f-de73-4e93-97d5-c04f892c8238" />

---

# 🛠️ Tech Stack

## Frontend

* HTML5
* CSS3
* JavaScript
* Jinja2 Templates

## Backend

* Python
* Flask

## Database

* SQLite
* SQLAlchemy ORM

## Real-Time Communication

* Flask-SocketIO
* WebSockets

## Authentication

* Flask-Login

---

# 📂 Project Structure

```text
study_platform/
│
├── app/
│   ├── routes/
│   │   ├── auth.py
│   │   ├── main.py
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │
│   ├── templates/
│   │
│   ├── __init__.py
│   ├── models.py
│   └── events.py
│
├── instance/
│   └── study_room.db
│
├── requirements.txt
├── run.py
└── README.md
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/StudySync.git
cd StudySync
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run Application

```bash
python run.py
```

---

## 5️⃣ Open in Browser

```text
http://localhost:5000
```

---

# 🎯 Use Cases

* Online Study Groups
* Exam Preparation
* Coding Communities
* Virtual Classrooms
* Productivity Tracking
* Peer Learning Sessions

---

# 🔮 Future Enhancements

* 🎥 Video Calling Integration
* 🤖 AI Study Assistant
* 📅 Shared Study Planner
* 📝 Collaborative Notes
* 📈 Advanced Analytics
* 🏆 Gamification & Leaderboards
* 🌙 Dark/Light Theme Support
* 📱 Mobile Application

---

# 👨‍💻 Developer

### Sonal Shrivastava

B.Tech – Computer Science Engineering

Areas of Interest:

* Software Development
* Artificial Intelligence
* Data Science
* Machine Learning
* Full Stack Development

GitHub:
https://github.com/shrivastavasonal62-oss

---

# ⭐ Support

If you found this project useful, please consider giving it a Star ⭐ on GitHub.
Thanks for visiting the repository!
