from flask import Flask,jsonify, render_template, request, redirect, url_for
import psycopg2
import uuid

app = Flask(__name__)

# Database configuration
DB_HOST = 'localhost'
DB_NAME = 'dev'
DB_USER = 'postgres'
DB_PASSWORD = 'rrana9'
DB_PORT = "5432"

# Connect to PostgreSQL database
conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
cur = conn.cursor()

# Create a table if it does not exists
cur.execute("""
    CREATE TABLE IF NOT EXISTS VOLUNTEERS (
        volunteer_id UUID PRIMARY KEY,
        first_name VARCHAR,
        last_name VARCHAR,
        email VARCHAR,
        date_of_birth DATE,
        address VARCHAR,
        skills VARCHAR,
        availability VARCHAR,
        date_joined DATE,
        background_check BOOLEAN
    )
""")
conn.commit()

@app.route('/')
def index():
    cur.execute("SELECT * FROM volunteers")
    volunteer_data = cur.fetchall()
    filter_parameter = request.args.get('filter')
    sort_parameter = request.args.get('sort')
    if not filter_parameter:
        filter_parameter = 'default_filter'
    if not sort_parameter:
        sort_parameter = 'default_sort'
    return render_template('index.html', volunteer_data=volunteer_data, filter=filter_parameter, sort=sort_parameter)

@app.route('/add', methods=['POST'])
def add_item():
    volunteer_id = str(uuid.uuid4())  
    background_check = bool(request.form.get('background_check', False))
    first_name = request.form.get('first_name','N/A')
    last_name = request.form.get('last_name', 'N/A')
    email = request.form.get('email', 'N/A')
    date_of_birth = request.form.get('date_of_birth')
    address = request.form.get('address', 'N/A')
    skills = request.form.get('skills', 'N/A')
    availability = request.form.get('availability', 'N/A')
    date_joined = request.form.get('date_joined')
    cur.execute("INSERT INTO volunteers (volunteer_id, first_name, last_name, email, date_of_birth, address, skills, availability, date_joined, background_check) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (volunteer_id, first_name, last_name, email, date_of_birth, address, skills, availability, date_joined, background_check))
    conn.commit()
    return redirect(url_for('index'))

@app.route('/delete/<uuid:volunteer_id>', methods=['POST'])
def delete_item(volunteer_id):
    cur.execute('DELETE FROM volunteers WHERE volunteer_id = %s',(str(volunteer_id),))
    conn.commit()
    return redirect(url_for('index'))

@app.route('/edit/<uuid:volunteer_id>', methods=['GET'])
def edit_item(volunteer_id):
    cur.execute("SELECT * FROM volunteers WHERE volunteer_id = %s", (str(volunteer_id),))
    volunteer = cur.fetchone()
    if volunteer:
        return render_template('edit.html', volunteer=volunteer)
    else:
        return "Volunteer not found", 404
    
@app.route('/update/<uuid:volunteer_id>', methods=['POST'])
def update_item(volunteer_id):
    background_check = bool(request.form.get('background_check', False))
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    date_of_birth = request.form['date_of_birth']
    address = request.form['address']
    skills = request.form['skills']
    availability = request.form['availability']
    date_joined = request.form['date_joined']
    cur.execute("UPDATE volunteers SET first_name=%s, last_name=%s, email=%s, date_of_birth=%s, address=%s, skills=%s, availability=%s, date_joined=%s, background_check=%s WHERE volunteer_id=%s", (first_name, last_name, email, date_of_birth, address, skills, availability, date_joined, background_check, str(volunteer_id)))
    conn.commit()
    return redirect(url_for('index'))

def get_volunteers_from_database(page, per_page, filter_by, filter_criteria, sort_by, sort_order):
    # Construct SQL query based on the provided options
    query = "SELECT * FROM volunteers"
    # Apply filtering if criteria are provided
    if filter_criteria:
        query += f" WHERE {filter_by} = '{filter_criteria}'"
    # Apply sorting
    query += f" ORDER BY {sort_by} {sort_order}"
    # Apply pagination
    offset = (page - 1) * per_page
    query += f" LIMIT {per_page} OFFSET {offset}"
    # Execute the query and retrieve the results from the database
    cur.execute(query)
    return cur.fetchall()

@app.route('/api/volunteers', methods=['GET'])
def get_volunteers():
    # Retrieve query parameters for pagination, filtering, and sorting
    page = request.args.get('page', default=1, type=int)
    page=page
    per_page = request.args.get('per_page', default=10, type=int)
    filter_by = request.args.get('filter_by', default=None, type=str)
    filter_criteria = request.args.get('filter_criteria', default=None, type=str)
    sort_by = request.args.get('sort_by', default='volunteer_id', type=str)
    sort_order = request.args.get('sort_order', default='asc', type=str)
    volunteers = get_volunteers_from_database(page, per_page, filter_by, filter_criteria, sort_by, sort_order)
    return render_template('index.html', volunteer_data=volunteers)

if __name__ == '__main__':
    app.run(debug=True)

