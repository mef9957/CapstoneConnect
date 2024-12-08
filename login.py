#!/usr/bin/python3
import cgi

print("Content-type: text/html\n\n")
name = '' # Initializing a variable for storing the name
def html_head(): # Function to print HTML head content
    print('''
    <!DOCTYPE HTML>
    <html>
    <head>
        <title>Login Confirmation</title>
        <link href="style.css" rel="stylesheet">
        <script>
            function showMessage(message, redirect, email) {
                alert(message);
                if (redirect) {
                    window.location.href = "viewmatches.py?email=" + encodeURIComponent(email); // Pass email as a URL parameter
                } else {
                    window.location.href = "login.html"; // Redirect to login page
                }
            }
        </script>
    </head>
    <body>
    </body>
    </html>
    ''')
# Function to check user credentials
def check_credentials(email, password):
    with open("student_database.txt", "r") as file: # Open the database file for reading
        for line in file:
            stored_email = line.strip().split(":")[0]
            stored_password = line.strip().split(":")[1]
            if email == stored_email and password == stored_password: # If email and password match
                name = line.strip().split(":")[2] # Get the name associated with the email
                return True # Return True indicating successful login
    return False # Return False indicating unsuccessful login

# Main function
def main():
    form_data = cgi.FieldStorage() # Get form data from CGI
    html_head()

    if 'email' in form_data and 'password' in form_data: # If email and password are in form data
        email = form_data['email'].value # Get the value of email from form data
        password = form_data['password'].value # Get the value of password from form data

        if check_credentials(email, password): # If credentials are valid
            print("<script>showMessage('Login successful!', true, '{}');</script>".format(email)) # Show success message
        else: # If credentials are invalid
            print("<script>showMessage('Invalid email or password!', false, '');</script>") # Show error message
    else:  # If email and password are not provided
        print("<script>showMessage('Email and password are required!', false, '');</script>") # Show error message

main()