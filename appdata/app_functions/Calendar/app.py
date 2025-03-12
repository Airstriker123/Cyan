from flask import Flask, render_template, request, jsonify #Backend modules
import json
import webbrowser
import threading
import socket
from datetime import datetime
import calendar


app = Flask(__name__)

DATA_FILE = "data.json" #file name


def load_data(): #get data from data file
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data(data): #input data if user enters any
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


@app.route("/")
def home():  # display method also main page
    today = datetime.now().date()
    y, m = today.year, today.month
    assessments = load_data()
    assessment_dates = {a["date"] for a in assessments}
    cal = calendar.monthcalendar(y, m)
    colored_calendar = []

    for week in cal:
        row = []
        for day in week:
            if day == 0:
                row.append("")
                continue

            date_str = f"{day:02d}-{m:02d}-{y}"
            day_date = datetime(y, m, day).date()

            if date_str in assessment_dates:
                color = "cyan"
            elif day_date < today:
                color = "red"
            elif day_date == today:
                color = f"green"
            else:
                color = "yellow"

            row.append({"day": day, "color": color})
        colored_calendar.append(row)

    return render_template("index.html", calendar=colored_calendar, assessments=assessments) #html,css and js files to include


@app.route("/add", methods=["POST"])
def add_assessment():
    data = request.json
    try:
        datetime.strptime(data["date"], "%d-%m-%Y")  # Validate date format
        assessments = load_data()
        assessments.append(data)
        save_data(assessments)
        return jsonify({"message": "Assessment added!"}), 200
    except ValueError:
        return jsonify({"error": "Invalid date format! Use DD-MM-YYYY"}), 400

@app.route("/delete", methods=["POST"])
def delete_assessment(): #button to delete a certain assessment
    data = request.json
    assessments = load_data()
    assessments = [a for a in assessments if a["date"] != data["date"]]
    save_data(assessments)
    return jsonify({"message": "Assessment deleted!"}), 200

@app.route("/delete_all", methods=["POST"])
def delete_all(): #delete all assessments data function
    save_data([])
    return jsonify({"message": "All assessments deleted!"}), 200

def get_local_ip(): #for lan hosting
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)


def open_browser(): #opens url for user
    ip = get_local_ip()
    url = f"http://{ip}:5000/"
    webbrowser.open(url)

if __name__ == '__main__': #main 
    threading.Timer(1.5, open_browser).start()
    app.run(host="0.0.0.0", port=5000, debug=True)
