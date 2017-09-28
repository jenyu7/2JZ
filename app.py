'''
Helen Ye, Jen Yu, Jennifer Zhang
SoftDev1 pd7
HW05 -- Jinja Tuning
2017-09-27
'''

from flask import Flask, render_template
from util import occupations

app = Flask(__name__)

#Add a landing page
@app.route("/")
def home():
    return '<a href="/occupations">Occupations?</a>'

#Process occupations csv
coll = occupations.read_occupations("data/occupations.csv")
@app.route("/occupations")
def display_template():
    # Generate a random profession
    prof = occupations.random_profession(coll)
    # Render the page with the random profession
    return render_template('temp1.html', collection = coll, rand = prof, link = coll[prof][1] )

if __name__ == "__main__":
    app.debug = True
    app.run()
