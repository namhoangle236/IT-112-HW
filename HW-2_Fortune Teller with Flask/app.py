from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def fortune():
    if request.method == "POST":

        username = request.form.get("username")
        color = request.form.get("color")
        number = request.form.get("number")
        fortune = None

        if color == 'red':
            if number == '1':
                fortune = "custom fortune red1"
            elif number == '2':
                fortune = "custom fortune red2"
            elif number == '3':
                fortune = "custom fortune red3"
            elif number == '4':
                fortune = "custom fortune red4"

        elif color == 'yellow':
            if number == '1':
                fortune = "custom fortune yellow1"
            elif number == '2':
                fortune = "custom fortune yellow2"
            elif number == '3':
                fortune = "custom fortune yellow3"
            elif number == '4':
                fortune = "custom fortune yellow4"

        elif color == 'blue':
            if number == '1':
                fortune = "custom fortune blue1"
            elif number == '2':
                fortune = "custom fortune blue2"
            elif number == '3':
                fortune = "custom fortune blue3"
            elif number == '4':
                fortune = "custom fortune blue4"

        elif color == 'green':
            if number == '1':
                fortune = "custom fortune green1"
            elif number == '2':
                fortune = "custom fortune green2"
            elif number == '3':
                fortune = "custom fortune green3"
            elif number == '4':
                fortune = "custom fortune green4"

        return render_template("fortune.html", username=username, color=color, number=number, fortune=fortune)
        
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)