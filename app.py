# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/login_process', methods=['POST'])
# def login_process():
#     # Get the password from the form
#     password = request.form['password']

#     # Execute the Python script to check password strength
#     import subprocess
#     result = subprocess.run(['python', 'password_validator.py', password], capture_output=True, text=True)

#     if result.returncode == 0:
#     # Password is strong, redirect to the welcome page
#         return redirect(url_for('welcome'))
#     else:
#         return "Password does not meet the requirements."


# @app.route('/welcome')
# def welcome():
#     return render_template('welcome.html')

# @app.route('/logout')
# def logout():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login_process', methods=['POST'])
def login_process():
    # Get the password from the form
    password = request.form['password']

    # Execute the Python script to check password strength
    import subprocess
    result = subprocess.run(['python', 'password_validator.py', password], capture_output=True, text=True)

    if result.returncode == 0:
        # Password is strong, set it in the session and redirect to the welcome page
        session['password'] = password
        return redirect(url_for('welcome'))
    else:
        return "Password does not meet the requirements."

@app.route('/welcome')
def welcome():
    # Check if the password is set in the session
    if 'password' in session:
        return render_template('welcome.html')
    else:
        # Redirect to the index page if the user is not authenticated
        return redirect(url_for('index'))

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        # Clear the session to perform logout
        session.pop('password', None)
        return redirect(url_for('index'))
    else:
        # Handle GET request (if needed)
        return render_template('logout.html')  # Create a template for logout page if necessary


if __name__ == '__main__':
    app.run(debug=True)
