from flask import Flask, render_template
import psutil

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent(interval=1)  # Ensure it captures CPU usage
    mem_percent = psutil.virtual_memory().percent
    message = None

    if cpu_percent > 80 or mem_percent > 80:
        message = "High CPU or Memory Detected, scale up!!!"

    # Print values for debugging
    print(f"CPU: {cpu_percent}, Memory: {mem_percent}")

    return render_template("index.html", cpu_metric=cpu_percent, mem_metric=mem_percent, message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
from flask import Flask, render_template
import psutil

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent(interval=1)  # Ensure it captures CPU usage
    mem_percent = psutil.virtual_memory().percent
    message = None

    if cpu_percent > 80 or mem_percent > 80:
        message = "High CPU or Memory Detected, scale up!!!"

    # Print values for debugging
    print(f"CPU: {cpu_percent}, Memory: {mem_percent}")

    return render_template("index.html", cpu_metric=cpu_percent, mem_metric=mem_percent, message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
