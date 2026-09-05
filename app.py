from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        temperature = float(request.form["temperature"])
        unit = request.form["unit"]

        if unit == "C":
            result = f"{temperature}°C = {(temperature * 9/5) + 32:.2f}°F"

        elif unit == "F":
            result = f"{temperature}°F = {(temperature - 32) * 5/9:.2f}°C"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)