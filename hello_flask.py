from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
    return """
    <p>Park: LOL (Laugh Out Loud)</p>
    <p>Sungmin: ASAP (As Soon As Possible)</p>
    <p>Tom: IDK (I Don't Know)</p>
    """

# Task 3
@app.route('/sungmin')
def my_page():
    acronym = "ASAP (As Soon As Possible)"
    return render_template('template.html', acronym=acronym)

# Task 4
@app.route('/image')
def image_page():
    return render_template('image.html')

