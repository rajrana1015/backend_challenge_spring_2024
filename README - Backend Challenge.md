
### Installation and Usage Guide for Flask and PostgreSQL CRUD Application

#### Introduction:
This document provides a step-by-step guide on installing dependencies and running a Flask and PostgreSQL CRUD (Create, Read, Update, Delete) application. The application allows managing volunteers' information stored in a PostgreSQL database.

#### Prerequisites:
- Python 3.x installed on your system.
- PostgreSQL database installed and running.
- Basic knowledge of Flask framework.
- Basic knowledge of SQL.

#### Installation:

1. **Flask Installation:**
   ```
   pip install Flask
   ```

2. **Psycopg2 Installation (PostgreSQL adapter for Python):**
   ```
   pip install psycopg2
   ```

3. **Clone the Application:**
   Clone or download the application code from the repository.

4. **Navigate to the Project Directory:**
   ```
   cd <project_directory>
   ```

#### Database Setup:

1. **Create Database:**
   - Open PostgreSQL command line or use a GUI tool like pgAdmin.
   - Create a new database named `dev`:
     ```
     CREATE DATABASE dev;
     ```
#### Running the Application:

1. **Configure Database Connection:**
   - Open `app.py` in a text editor.
   - Modify the database connection settings in the following lines:
     ```python
     DB_HOST = 'localhost'
     DB_NAME = 'dev'
     DB_USER = 'postgres'
     DB_PASSWORD = 'rrana9'
     DB_PORT = "5432"
     ```

2. **Run the Application:**
   ```
   python app.py
   ```

3. **Access the Application:**
   - Open a web browser and go to `http://localhost:5000/`.

#### Usage:

1. **Adding a Volunteer:**
   - Click on the "Add Volunteer" button on the home page.
   - Fill in the volunteer information in the form and click "Submit".

2. **Editing a Volunteer:**
   - Click on the "Edit" button next to the volunteer you want to edit.
   - Modify the volunteer information in the form and click "Update".

3. **Deleting a Volunteer:**
   - Click on the "Delete" button next to the volunteer you want to delete.
   - Confirm the deletion when prompted.

4. **Viewing All Volunteers:**
   - Click on the "View All Volunteers" button on the home page to see a list of all volunteers.

#### Conclusion:
This document has provided detailed instructions on installing dependencies and running the Flask and PostgreSQL CRUD application. Follow the steps outlined above to set up and use the application successfully.

#### Feedback:
If you encounter any issues or have suggestions for improvement, please feel free to reach out and provide feedback.

---

Ensure to replace `<project_directory>` with the actual directory where you have cloned the application. This document should serve as a comprehensive guide for users to set up and utilize the Flask and PostgreSQL CRUD application effectively.