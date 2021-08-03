from bson import ObjectId
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
from db_connection import get_db
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def create():
    db = get_db()

    if request.method == 'GET':
        return render_template('home.html')

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']

        emp = {}

        emp['name'] = name
        if email != "":
            emp['email'] = email
        emp['phone'] = phone
        if address != "":
            emp['address'] = address

        db.emp_collection.insert(emp)
        return redirect(url_for('read'))


@app.route('/read', methods=['GET'])
def read():
    db = get_db()
    employees = list(db.emp_collection.find())
    return render_template('dashboard.html', employees=employees)


@app.route('/update/<_id>', methods=['GET', 'POST'])
def update(_id):
    db = get_db()

    if request.method == 'GET':
        employee = list(db.emp_collection.find({"_id": ObjectId(_id)}))[0]
        return render_template('update.html', employee=employee)

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']

        emp = {}

        emp['name'] = name
        if email != "":
            emp['email'] = email
        emp['phone'] = phone
        if address != "":
            emp['address'] = address

        find_values = list(db.emp_collection.find({"_id": ObjectId(_id)}))[0]

        replace_values = emp

        db.emp_collection.replace_one(find_values, replace_values)

        return redirect(url_for('read'))


@app.route('/delete/<_id>', methods=['GET', 'POST'])
def delete(_id):
    db = get_db()
    if request.method == 'GET':
        find_values = list(db.emp_collection.find({"_id": ObjectId(_id)}))[0]
        db.emp_collection.delete_one(find_values)
        return redirect(url_for('read'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
