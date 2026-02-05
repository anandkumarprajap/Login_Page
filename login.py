from flask import Flask , request, redirect, url_for, session , Response

app = Flask(__name__)
app.secret_key = "supersecret"

#Homepage Login Page 
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Simple authentication logic (for demonstration purposes only)
        if username == "admin" and password == "123":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials. Please try again.", mimetype="text/plain")
    return '''
        <h2>Login Page</h2>
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

# welcome page after login
@app.route("/welcome")
def welcome():
    if 'user' in session:
        return f'''
            <h2>Welcome, {session['user']}!</h2>
            <a href={url_for('logout')}>Logout</a>
        '''
    return redirect(url_for("login"))

# Logout route
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
    