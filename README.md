# IPTFINAL

Project Details:

This project is a RESTful API built using Flask, a Python web framework. It provides CRUD (Create, Read, Update, Delete) operations for managing data in a MySQL database. The API supports basic authentication for secure access to the endpoints.

Requirements:

Python 3.x
Flask
Flask-MySQLdb
MySQL database
Endpoints:

GET /tables - Retrieves a list of all tables in the MySQL database.

GET /tables/{table} - Retrieves all entries from a specific table.

GET /tables/{table}/{id} - Retrieves a specific entry from a table based on the provided ID.

POST /tables/{table}/{id} - Adds a new entry to the specified table. The request body should contain the necessary data in JSON format.

PUT /tables/{table}/{id} - Updates an existing entry in the specified table. The request body should contain the updated data in JSON format.

DELETE /tables/{table}/{id} - Deletes an entry from the specified table based on the provided ID.

Authentication:

Basic authentication is implemented using a username and password. Currently, the hardcoded username is "zhar" and the password is "2564". You need to include the authentication details in the request headers to access the protected endpoints.

Database Configuration:

The project is configured to connect to a MySQL database with the following credentials:

Host: 127.0.0.1
User: root
Password: [empty string]
Database: zhar
You may need to update these credentials in the code (app.config["MYSQL_HOST"], app.config["MYSQL_USER"], app.config["MYSQL_PASSWORD"], app.config["MYSQL_DB"]) to match your own database configuration.

Running the Application:

Ensure that you have all the required dependencies installed.
Set up a MySQL database and update the database credentials in the code if necessary.
Run the Python script to start the Flask server.
The server will run on http://127.0.0.1:5000/ by default.
You can use tools like cURL or Postman to make requests to the API endpoints.
Note: This project assumes you have basic knowledge of Flask, RESTful APIs, and MySQL.

----------------------------------------------------------------------------------------------------

Prerequisites:

Python 3.x installed on your system.
pip (Python package manager) installed.
Step 1: Clone the Project

Open a terminal or command prompt.
Change the current directory to the location where you want to clone the project.
Run the following command to clone the project repository:
git clone <repository_url>
Replace <repository_url> with the URL of the project repository.
Step 2: Set up the Virtual Environment

Change the current directory to the project folder:
cd project-folder
Replace project-folder with the actual folder name where the project was cloned.
Create a virtual environment:
python3 -m venv venv
Activate the virtual environment:
For Windows:
venv\Scripts\activate
For macOS/Linux:
source venv/bin/activate
Step 3: Install Dependencies

Make sure you are in the project folder and the virtual environment is activated.
Run the following command to install the required dependencies:
pip install -r requirements.txt
Step 4: Configure the MySQL Database

Make sure you have MySQL installed and running on your system.
Open the app.py file in a text editor.
Locate the database configuration section in the code (starts with app.config["MYSQL_"]).
Update the configuration values (MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB) with your own MySQL database credentials.
Step 5: Run the Flask Application

Make sure you are in the project folder and the virtual environment is activated.
Run the following command to start the Flask server:
python app.py
The Flask application will start running on http://127.0.0.1:5000/.
You can now use tools like cURL or Postman to make requests to the API endpoints mentioned in the previous response. Make sure to include the necessary authentication details in the request headers for the protected endpoints.

That's it! You have successfully installed and set up the Flask project.

-------------------------------------------
