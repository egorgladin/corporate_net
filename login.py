from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
import pandas as pd
from ast import literal_eval


app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

employees = pd.read_csv("Employees_skills.csv", index_col=0,
						converters={"skills": literal_eval})
employees_names = employees.name.tolist()

projects = pd.read_csv("Projects.csv", index_col=0,
						converters={"skills": literal_eval})


def iou(row, employee_skills):
	required_skills = row["skills"]
	intersection = len(set(employee_skills) & set(required_skills))
	union_ = len(set(employee_skills).union(required_skills))
	return intersection / union_

def proj_description(row):
	required_skills = ', '.join(row["skills"])
	return f"{row['project name']} requires skills: {required_skills}"

@app.route("/")
def home():
	return redirect(url_for("user"))

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		user = request.form["nm"]
		if user in employees_names:  # FIXME: else add flashing
			session.permanent = True
			session["user"] = user
			session["skills"] = employees.loc[employees['name'] == user].skills.iloc[0]
			return redirect(url_for("user"))
	if "user" in session:
		return redirect(url_for("user"))

	return render_template("login.html")

@app.route("/user")
def user():
	if "user" in session:
		user = session["user"]
		skills = session["skills"]
		projects["IoU"] = projects.apply(lambda x: iou(x, skills), axis=1)
		projects.sort_values(by="IoU", inplace=True, ascending=False)
		rec_projects = projects.iloc[:5].apply(proj_description, axis=1).tolist()
		return render_template("profile.html", name=user,
							   skills=', '.join(skills), projects=rec_projects)  # f"<h1>{user}</h1><br />Skills: {', '.join(skills)}"
	else:
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	session.pop("user", None)
	return redirect(url_for("login"))

if __name__ == "__main__":
	app.run(debug=True)
