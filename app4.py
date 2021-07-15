from flask import Flask
from flask import redirect, url_for, render_template


app = Flask(__name__)

student_ages = {"Naeemah": 25, "godwin": 26, "Thapelo": 47, "Jason": 23}

@app.route('/homepage')
def projects_page():
    return render_template('homepage.html', student_ages=student_ages)


@app.route('/times/<int:numbers>')
def times(numbers):
    return render_template('numbers_page.html', numbers=numbers)


if __name__ == '__main__':
    app.debug = True
    app.run()
