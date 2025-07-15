import firebase_admin
from firebase_admin import credentials, auth, firestore
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

# Initialize Firebase Admin SDK
cred = credentials.Certificate(r"C:\Users\Adhithya K.THIRUMAL\Downloads\rolebasedaccess-eb1a7-firebase-adminsdk-fbsvc-a7bf146452.json")
firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()

# Create the main application window
window = tk.Tk()
window.title("Firebase User Management and Role-Based Access")
window.geometry("600x500")

# Frame to hold all sections
main_frame = tk.Frame(window)
main_frame.pack(pady=20)

# Function to show sections
def show_section(section_frame):
    for widget in main_frame.winfo_children():
        widget.pack_forget()
    section_frame.pack(fill="both", expand=True)

# Section Frames
user_creation_frame = tk.Frame(main_frame)
role_data_frame = tk.Frame(main_frame)
data_retrieval_frame = tk.Frame(main_frame)

# Function to create a user with a role
def create_user_with_role():
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    if not email or not password:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return
    try:
        user = auth.create_user(email=email, password=password)

        # Store the role in Firestore
        db.collection('users').document(user.uid).set({'email': email, 'role': role_var.get()})
        messagebox.showinfo("Success", f"User '{email}' created. UID: {user.uid}")
        uid_label.config(text=f"UID: {user.uid}")
    except Exception as e:
        messagebox.showerror("Error", f"Error creating user: {e}")

# Function to create role-specific data
def create_role_data():
    role = role_var.get().lower()
    data = data_entry.get("1.0", tk.END).strip()
    if not role or not data:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return
    try:
        db.collection('roles').document(role).set({'data': data})
        messagebox.showinfo("Success", f"Data for role '{role}' saved.")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving data: {e}")

# Function to retrieve data by UID
def retrieve_data():
    uid = uid_entry.get().strip()
    if not uid:
        messagebox.showwarning("Input Error", "Please enter a UID.")
        return
    try:
        user_doc = db.collection('users').document(uid).get()
        if user_doc.exists:
            role = user_doc.to_dict().get('role')
            role_data = db.collection('roles').document(role).get().to_dict()
            messagebox.showinfo("Data Retrieved", f"Role: {role}\nData: {role_data['data']}")
        else:
            messagebox.showerror("Error", "UID not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Error retrieving data: {e}")

# User Creation Section
tk.Label(user_creation_frame, text="Create User", font=("Arial", 14, "bold")).pack(pady=10)

# Role Selection
tk.Label(user_creation_frame, text="Select Role (admin/user):").pack(pady=5)
role_var = tk.StringVar(value="admin")
role_dropdown = ttk.Combobox(user_creation_frame, textvariable=role_var, values=["admin", "user"])
role_dropdown.pack(pady=5)
tk.Label(user_creation_frame, text="Email:").pack()
email_entry = tk.Entry(user_creation_frame, width=30)
email_entry.pack(pady=5)
tk.Label(user_creation_frame, text="Password:").pack()
password_entry = tk.Entry(user_creation_frame, show='*', width=30)
password_entry.pack(pady=5)
tk.Button(user_creation_frame, text="Create User", command=create_user_with_role, bg="blue", fg="white").pack(pady=10)
uid_label = tk.Label(user_creation_frame, text="UID:", font=("Arial", 12, "bold"), fg="green")
uid_label.pack(pady=5)

# Role Data Section
tk.Label(role_data_frame, text="Create Role Data", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(role_data_frame, text="Role (admin/user):").pack()
role_var = tk.StringVar(value="admin")
ttk.Combobox(role_data_frame, textvariable=role_var, values=["admin", "user"]).pack(pady=5)
tk.Label(role_data_frame, text="Data:").pack()
data_entry = tk.Text(role_data_frame, width=30, height=5)
data_entry.pack(pady=5)
tk.Button(role_data_frame, text="Save Data", command=create_role_data, bg="blue", fg="white").pack(pady=10)

# Data Retrieval Section
tk.Label(data_retrieval_frame, text="Retrieve Data by UID", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(data_retrieval_frame, text="Enter UID:").pack()
uid_entry = tk.Entry(data_retrieval_frame, width=30)
uid_entry.pack(pady=5)
tk.Button(data_retrieval_frame, text="Retrieve Data", command=retrieve_data, bg="blue", fg="white").pack(pady=10)

# Navigation Icons
icons_frame = tk.Frame(window)
icons_frame.pack(pady=10)

icons = ["create_user.png", "create_data.png", "retrieve_data.png"]
icon_labels = ["Create User", "Create Role Data", "Retrieve Data"]
frames = [user_creation_frame, role_data_frame, data_retrieval_frame]

for i, icon_path in enumerate(icons):
    img = Image.open(icon_path).resize((50, 50))
    img_tk = ImageTk.PhotoImage(img)
    btn = tk.Button(icons_frame, image=img_tk, command=lambda f=frames[i]: show_section(f))
    btn.image = img_tk
    btn.pack(side="left", padx=20)
    tk.Label(icons_frame, text=icon_labels[i]).pack(side="left", padx=10)

show_section(user_creation_frame)
window.mainloop()
