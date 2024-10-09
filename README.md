# Feedback Form System

This is a simple feedback form project built with Flask, HTML, CSS and MySQL. It allows users to submit feedback with their name, email address, and a message. The feedback is then stored in a MySQL database and displayed on the website.

## Overview of Technologies Used

* **HTML + CSS**: Used to create the user interface of the feedback form.
* **Flask**: A lightweight and flexible Python framework for building web applications. It's a great choice for small and medium-sized projects.
* **MySQL**: A relational database management system (RDBMS) used to store and manage the feedback data efficiently.
* **Flask-MySQLdb**: Integrates Flask with MySQL, making it easy to perform database operations like creating tables, inserting, and fetching data.

## Getting Started

### Prerequisites

* Python 3.9 or later installed on your system
* MySQL server installed and running on your system
* A MySQL database created for the project (e.g., `feedback_db`)

### How to Run the Project

#### 1. Clone the Repository
```bash
git clone https://github.com/neeti-kurulkar/feedback-system.git
cd feedback-system
```

#### 2. Create a Virtual Environment
```bash
python -m venv myenv
source myenv/bin/activate   # For Linux/MacOS
myenv\Scripts\activate    # For Windows
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Configure MySQL
Ensure that MySQL is running and create a database named `feedback_db`. Then, configure the connection settings in the `database.py` file as follows:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_mysql_username'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'feedback_db'
```

#### 5. Run the Application
```bash
python app.py
```
Navigate to `http://127.0.0.1:5000` in your web browser.

#### 6. Inserting Sample Data
You can run the `feedback_data.sql` file to insert sample data into the `feedback` table:

```bash
mysql -u your_mysql_username -p feedback_db < feedback_data.sql
```