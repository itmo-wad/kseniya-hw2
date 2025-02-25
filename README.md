# Flask Authentication System

In this project, I implemented a basic authentication feature for a web application using **Flask** and **MongoDB**.

## 🛠 **Technologies Used**
- **HTML, CSS** - Frontend design
- **Flask** - Backend framework
- **MongoDB** - Database for user authentication
- **Werkzeug** - Password hashing

---

## 📜 **Project Steps**

### 🔹 1. Authentication Form
- Created an **HTML template** to render the authentication form.
- Implemented a **Flask route** (`/`) to serve the login page when users access `http://localhost:5000/`.


### 🔹 2. Registrer User
- Implemented authentication logic in the `/` route to handle **form submissions**.
- Retrieved the **username and password** from the form.
- Queried the **MongoDB collection** to find the user and **verified the password**.

---

### 🔹 3. Handle Authentication
- Implemented user registration feature

---

### 🔹 4. Show Profile Page
- Created `profile.html` for authenticated users only.
- Implemented a **Flask route** (`/profile/<username>`) to serve the profile page.

---


## HOW To RUN ?

1- install flask (pip install flask)

2- install MongoDB and create a database name itmowadhw2 and collection : users

3- clone the repository of the project

4- navigate to the repository and run the command : python3 app.py

5- Reach the website on http://localhost:5000
