from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []
completed = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form["task"]
        tasks.append(task)
        completed.append(False)
    return render_template("index.html", tasks=tasks, completed=completed)

@app.route("/delete/<int:index>")
def delete(index):
    tasks.pop(index)
    completed.pop(index)
    return redirect("/")

@app.route("/complete/<int:index>")
def complete(index):
    completed[index] = True
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)