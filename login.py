# login.py
def login(username, password):
    # Sample credentials for demonstration
    valid_user = "admin"
    valid_pass = "password123"
    
    if username == valid_user and password == valid_pass:
        return "Login successful!"
    else:
        return "Invalid credentials."
