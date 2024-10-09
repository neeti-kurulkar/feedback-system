from flask import Flask, render_template, request, redirect, url_for
from database import create_table, insert_feedback, fetch_feedback

app = Flask(__name__)

@app.route('/')
def index():
    feedbacks = fetch_feedback()
    return render_template('index.html', feedbacks=feedbacks)

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    insert_feedback(name, email, message)
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():  # Create the table if it doesn't exist
        create_table()
    app.run(debug=True)
