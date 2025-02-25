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
### 🔹. Screenshot
Loging Page
<img width="689" alt="Capture d’écran 2025-02-25 à 13 06 21" src="https://github.com/user-attachments/assets/5fc25d2d-3863-40c6-8ba1-7ac4b350dbe4" />

User Registration
<img width="652" alt="Capture d’écran 2025-02-25 à 13 06 50" src="https://github.com/user-attachments/assets/0d3bf95f-c041-4069-88c9-812489440eaf" />

Profile Page
<img width="858" alt="Capture d’écran 2025-02-25 à 13 07 05" src="https://github.com/user-attachments/assets/6c85bac2-d4e4-4949-bb30-dda37f2b7241" />

## HOW To RUN ?

1- Configure and Active virtual env (python3 -m venv .venv)

2- Install flask (pip install flask)

3- install MongoDB and create a database name itmowadhw2 and collection : users

4- clone the repository of the project

5- navigate to the repository and run the command : python3 app.py

5- Reach the website on http://localhost:5000
