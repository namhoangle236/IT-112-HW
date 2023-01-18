from flask import Flask, render_template

app = Flask(__name__)

#Default route and index route leads to same page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

#About route leads to 'about' page (note: /about/ doesn't work! No end slash)
@app.route('/about')
def aboutme():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)