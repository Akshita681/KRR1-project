from flask import Flask, render_template, request
from orchestrator import decide_career

app = Flask(__name__)

def confidence_score(skill):
    return {
        "beginner": 60,
        "intermediate": 75,
        "advanced": 90
    }.get(skill, 50)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        interest = request.form["interest"]
        skill = request.form["skill"]
        preference = request.form["preference"]

        career = decide_career(interest, skill, preference)
        confidence = confidence_score(skill)
        status = "Suitable" if confidence >= 70 else "Not Suitable"

        result = {
            "career": career.replace("_", " ").title(),
            "confidence": confidence,
            "status": status
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
