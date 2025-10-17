# 🩺 AidConnect – SDG 1: No Poverty

AidConnect is a web-based platform designed to bridge the gap between **aid providers (donors, NGOs, organizations)** and **beneficiaries** in need.  
It aims to support **UN Sustainable Development Goal 1 – No Poverty**, by simplifying how individuals and organizations connect to offer or request assistance.

---

## 🌍 Project Overview

Poverty remains one of the most pressing challenges worldwide.  
AidConnect provides a **digital solution** that enables donors to identify and support verified beneficiaries, promoting transparency and efficiency in the aid distribution process.

> ⚙️ **Note:** This project is still under development.  
> Future improvements will include enhanced user roles, payment integrations, and better UI/UX.

---

## 🎯 Objectives

- To provide a digital platform for managing aid requests and offers.
- To create a transparent system linking donors and beneficiaries.
- To contribute towards **SDG 1 – Ending poverty in all its forms**.
- To demonstrate database-driven web development using Flask and MySQL.

---

## 🧱 Technologies Used

| Component | Technology |
|------------|-------------|
| Backend | Flask (Python) |
| Frontend | HTML5, CSS3, Jinja2 |
| Database | MySQL |
| ORM | Flask-MySQL / MySQL Connector |
| Other Tools | Bootstrap, VS Code, GitHub |

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/Hector10-Ck/AidConnect_mysql.git

# Navigate to the project folder
cd AidConnect_mysql

# Install dependencies
pip install -r requirements.txt

# Import database structure
mysql -u root -p < create_tables.sql

# Run the application

flask run
💡 Features

User registration and authentication (Donors & Beneficiaries)

Role-based dashboards

Aid request creation and management

Donor listing and response

MySQL database integration

Responsive user interface

🧩 Project Structure
AidConnect_mysql/
│
├── app.py                # Main Flask app
├── config.py             # Configuration settings
├── create_tables.sql     # Database schema
├── templates/            # HTML templates (Jinja2)
├── static/               # CSS, JS, and images
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation



🚀 Future Improvements

Integration of donation tracking system

Email notifications and verification

Improved UI design using Bootstrap 5

Enhanced security with password hashing and form validation

API endpoints for mobile integration

🧑‍💻 Author

Hector Karisa Charo
Developed as part of an academic project focusing on SDG 1 – No Poverty.

“Using technology to bridge the gap between hope and help.”


