from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

DATABASE = 'tasks.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed BOOLEAN DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def home():
    init_db()
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    
    if request.method == "POST":
        task = request.form["task"]
        cur.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
    
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    conn.close()
    
    return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/complete/<int:id>")
def complete(id):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)