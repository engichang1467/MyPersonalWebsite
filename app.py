from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)


# more information: https://medium.com/@francescaguiducci/how-to-build-a-simple-personal-website-with-python-flask-and-netlify-d800c97c283d