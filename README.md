# Smartservices

A web-based Service Booking and Management System developed using **Django** that connects customers with service providers through a simple and efficient platform. Users can register, browse available services, book service providers, track bookings, and manage payments, while administrators can monitor and manage the entire system.

## 🚀 Features

* User Registration and Login
* Role-Based Access Control (Customer, Service Provider, Admin)
* Service Provider Management
* Service Booking System
* Booking Approval Workflow
* Payment Tracking and Management
* Customer Feedback System
* Responsive User Interface
* Admin Dashboard
* CRUD Operations for Services and Bookings

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* Bootstrap
* JavaScript

### Backend

* Python
* Django

### Database

* SQLite3

## 📂 Project Structure

```bash
Smartservices/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
│
├── Smartservices/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── ...
│
├── templates/
├── static/
└── media/
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Smartservices
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements file is unavailable:

```bash
pip install django
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Server

```bash
python manage.py runserver
```

### 8. Open in Browser

```text
http://127.0.0.1:8000/
```

Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

## 👥 User Roles

### Customer

* Register/Login
* Search Services
* Book Services
* Track Bookings
* Submit Feedback

### Service Provider

* Manage Profile
* View Booking Requests
* Approve/Reject Bookings
* Manage Service Details

### Admin

* Manage Users
* Manage Service Providers
* Monitor Bookings
* Manage Payments

## 🔄 Project Workflow

1. User registers and logs in.
2. Customer searches for required services.
3. Customer selects a service provider.
4. Booking request is submitted.
5. Service provider approves or rejects the request.
6. Payment details are recorded.
7. Customer provides feedback after service completion.

## 🎯 Key Learning Outcomes

* Django Framework Development
* Authentication & Authorization
* Database Management with SQLite
* CRUD Operations
* MVC/MVT Architecture
* Form Handling and Validation
* Service Booking Workflow Management

## 📸 Screenshots

Add project screenshots here:

```text
screenshots/
├── homepage.png
├── login.png
├── booking.png
└── admin-dashboard.png
```

## 🔮 Future Enhancements

* Online Payment Gateway Integration
* Email & SMS Notifications
* Real-Time Booking Updates
* Mobile Application Support
* GPS-Based Service Tracking
* Ratings and Reviews System
* Chat Support Feature

## 📄 License

This project is developed for educational and learning purposes.

## 👨‍💻 Author

**Vinay B K**

GitHub: Add your GitHub profile link here.
