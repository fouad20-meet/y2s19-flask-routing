from databases import *
from flask import Flask, render_template, url_for,request
app = Flask(__name__)

@app.route('/student/<int:student_id>')
def display_student(student_id):
	return render_template("student.html",id_number=student_id, student=query_by_id(student_id))

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':

        return redirect(url_for('index'))

    # show the form, it wasn't submitted

    return render_template('home.html',ls=query_all())

if __name__ == '__main__':
    app.run(debug=True)
