from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

DB_FILE = 'users.db'

@app.route('/')
def index():
    if 'username' in session:
        return f"Logged in as {session['username']} <br><a href='/logout'>Logout</a>"
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']
        pw_hash = hashlib.sha256(pw.encode()).hexdigest()

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password_hash=?", (user, pw_hash))
        result = cursor.fetchone()
        conn.close()

        if result:
            session['username'] = user
            return redirect('/')
        else:
            return "Login failed. <a href='/login'>Try again</a>"
    return render_template('login.html')

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))

    return render_template('register.html')

# SQL injection
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        name = request.form['username']

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{name}'"
        print("[VULNERABLE] Executing:", query)

        try:
            cursor.execute(query)
            result = cursor.fetchall()
        except Exception as e:
            result = []
            print("[Error]", e)

        conn.close()

        if result:
            users = [f"{row[0]} | {row[1]}" for row in result]
            return f"<p>Found user(s): <b>{'<br>'.join(users)}</b></p><a href='/search'>Try again</a>"

        else:
            return f"<p>No user found for input: <b>{name}</b></p><a href='/search'>Try again</a>"

    return '''
        <form method="POST">
            Search Username: <input name="username">
            <button type="submit">Search</button>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

if __name__ == '__main__':
    # HTTPS
    app.run(ssl_context=('cert.pem', 'key.pem'), debug=True)

    # HTTP
    # app.run(debug=True)
