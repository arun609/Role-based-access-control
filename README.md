
# 🛡️ Role-Based Access Control System (RBAC)

## 📖 Overview

This project implements a **Role-Based Access Control (RBAC)** system using Python, Firebase, and ipywidgets. The system allows administrators to create users, assign roles (like Admin, User, Guest), and control access to different parts of the application based on the user's role.

The project features a clean and interactive **GUI interface** using ipywidgets and integrates with **Firebase Realtime Database** for storing user credentials and role assignments.

This enables centralized control of user access, making it ideal for applications like:

- 🏢 Enterprise Admin Panels  
- 🎓 Educational Portals  
- 🏥 Healthcare Systems  
- 📊 Data Dashboards

---

## 🌟 Features

| Feature                     | Description |
|----------------------------|-------------|
| ✅ GUI-Based Login System      | Interactive login screen using ipywidgets |
| 🆔 User Registration & Roles   | Admins can create users and assign roles |
| 🔐 Role-Based Permissions     | Access is granted based on role (Admin/User/Guest) |
| 🔥 Firebase Integration       | Authenticates and stores user-role data |
| 📁 Modular Python Code        | Easy to extend or embed into larger systems |
| 📊 Role Logs & Access Output  | Can log who accessed what, based on role |
| 📦 Lightweight Deployment     | Runs in Jupyter Notebook, no web server needed |

---

## 🛠️ Technologies Used

| Technology     | Purpose                                               |
|----------------|--------------------------------------------------------|
| Python         | Core programming language                             |
| Firebase       | Authentication and data storage                       |
| ipywidgets     | GUI elements in Jupyter notebooks                     |
| firebase-admin | SDK for Firebase access                               |
| Jupyter Notebook | Interactive development and user interface         |

---

## 📦 Dependencies

Install via `requirements.txt` or run:

```bash
pip install firebase-admin
pip install ipywidgets
````

---

## 🔁 Workflow Steps

### 1️⃣ Set Up Firebase

* Create a Firebase project
* Enable Realtime Database and Email/Password Authentication
* Download `serviceAccountKey.json` and save in the project directory

### 2️⃣ Configure Firebase in Python

* Use `firebase_admin` SDK to initialize app
* Setup database references for user data and roles

### 3️⃣ Build the GUI

* Use `ipywidgets` to create:

  * Login form
  * Role selection
  * Success/error messages

### 4️⃣ Role Assignment

* Admin creates users and assigns roles
* Roles stored in Firebase and validated at login

### 5️⃣ Access Control

* After login, the system checks the user’s role
* Display or restrict access to UI based on role

### 6️⃣ Optional Logging and Visualization

* Log access attempts
* Display number of users per role (with pandas or matplotlib)



## 🔗 Useful Links

* Firebase Console: [https://console.firebase.google.com/](https://console.firebase.google.com/)
* ipywidgets Docs: [https://ipywidgets.readthedocs.io/](https://ipywidgets.readthedocs.io/)
* Firebase Admin SDK: [https://firebase.google.com/docs/admin/setup](https://firebase.google.com/docs/admin/setup)

---

## 👨‍💻 Author

**Arun M**
B.Tech in Artificial Intelligence and Data Science
[GitHub](https://github.com/yourusername) | [LinkedIn](https://linkedin.com/in/yourprofile)





