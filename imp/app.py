from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

# Create a cursor
cursor = db.cursor()

# Create a table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS dummy_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    column1 VARCHAR(255),
    column2 VARCHAR(255)
)
"""
cursor.execute(create_table_query)

# Route to create data
@app.route('/create', methods=['GET', 'POST'])
def create_data():
    if request.method == 'POST':
        column1 = request.form['column1']
        column2 = request.form['column2']
        insert_data_query = "INSERT INTO dummy_table (column1, column2) VALUES (%s, %s)"
        cursor.execute(insert_data_query, (column1, column2))
        db.commit()
    return render_template('create.html')

# Route to show data
@app.route('/show')
def show_data():
    select_data_query = "SELECT * FROM dummy_table"
    cursor.execute(select_data_query)
    data = cursor.fetchall()
    return render_template('show.html', data=data)

# Route to delete data
@app.route('/delete/<int:id>')
def delete_data(id):
    delete_data_query = "DELETE FROM dummy_table WHERE id = %s"
    cursor.execute(delete_data_query, (id,))
    db.commit()
    return redirect(url_for('show_data'))

# Route to edit data
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_data(id):
    if request.method == 'POST':
        column1 = request.form['column1']
        column2 = request.form['column2']
        update_data_query = "UPDATE dummy_table SET column1 = %s, column2 = %s WHERE id = %s"
        cursor.execute(update_data_query, (column1, column2, id))
        db.commit()
        return redirect(url_for('show_data'))
    
    select_data_query = "SELECT * FROM dummy_table WHERE id = %s"
    cursor.execute(select_data_query, (id,))
    data = cursor.fetchone()
    return render_template('edit.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
