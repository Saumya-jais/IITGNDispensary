from flask import Flask, render_template, jsonify, request, redirect, url_for
import pymysql
import config
from flask import Flask, redirect, url_for, session, request
from authlib.integrations.flask_client import OAuth
import re 
app = Flask(__name__)

# PyMySQL configurations
app.config['MYSQL_HOST'] = config.MYSQL_HOST
app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB
app.secret_key = 'a_temporary_secret_key'
# Initialize PyMySQL connection
def get_mysql_connection():
    connection = pymysql.connect(host=app.config['MYSQL_HOST'],
                                 user=app.config['MYSQL_USER'],
                                 password=app.config['MYSQL_PASSWORD'],
                                 db=app.config['MYSQL_DB'],
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

# OAuth Configuration
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='990087137993-38mh8ncf6j0hs0qirj3bhsg1u51mhl4c.apps.googleusercontent.com',
    client_secret='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',
    access_token_url='https://oauth2.googleapis.com/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    client_kwargs={'scope': 'openid email profile'},
)


@app.route('/login')
def login():
    new_email = request.args.get('email')
    password = request.args.get('password')
    authority = request.args.get('authority')
    print(new_email)
    print('Inside login')
    session['new_email'] = new_email  # Store the new email in the session
    session['password'] = password
    session['authority'] = authority
    return google.authorize_redirect(redirect_uri=url_for('authorize', _external=True))

@app.route('/login/callback')
def authorize():
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    print('Inside authorize')
    print(user_info)
    print(session.get('new_email'))
    # Check if the email matches the one from the registration form
    if 'email' in user_info and user_info['verified_email'] == True and user_info['email'] == session.get('new_email'):
        session['user_info'] = user_info
        return redirect(url_for('register', email=user_info['email'], password=session.get('password'), authority=session.get('authority')))
    else:
        return 'Unauthorized Email Domain', 401

@app.route('/registration', methods=['POST'])
def check():
    email = request.form['newEmail']
    password = request.form['newPassword']
    authority = request.form['authority']
    return redirect(url_for('login', email=email, password=password, authority=authority))


def validate_email(email):  
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
        return True  
    return False
@app.route('/')
def main():
    return render_template('login.html')
@app.route('/registration.html')
def reg():
    return render_template('registration.html')

@app.route('/index_p')
def index_main_p():
    return render_template('index_p.html')
@app.route('/doc_staff_p')
def doc_staff_p():
    return render_template('doc_staff_p.html')

@app.route('/emergency_p')
def emergency_p():
    return render_template('emergency_p.html')

@app.route('/med_purchase_p')
def med_purchase_p():
    return render_template('med_purchase_p.html')

@app.route('/insurance_p')
def insurance_p():
    email = request.args.get('email')
    return render_template('insurance_p.html', email=email)

@app.route('/doctor_p')
def doctor_p():
    return render_template('doctor_p.html')

@app.route('/staff_p')
def staff_p():
    return render_template('staff_p.html')

@app.route('/medical_test_p')
def medical_test_p():
    return render_template('medical_test_p.html')

@app.route('/hospital_p')
def hospital_p():
    return render_template('hospital_p.html')

@app.route('/supplier_p')
def supplier_p():
    return render_template('supplier_p.html')
@app.route('/opd_p')
def pat_opd_p():
    email = request.args.get('email')
    return render_template('opd_p.html',email=email)
@app.route('/pat_opd_p')
def opd_p():
    return render_template('pat_opd_p.html')

@app.route('/index_d')
def index_d():
    return render_template('index_d.html')

@app.route('/doc_staff_d')
def doc_staff_d():
    return render_template('doc_staff_d.html')

@app.route('/emergency_d')
def emergency_d():
    return render_template('emergency_d.html')

@app.route('/med_purchase_d')
def med_purchase_d():
    return render_template('med_purchase_d.html')

@app.route('/insurance_d')
def insurance_d():
    return render_template('insurance_d.html')

@app.route('/doctor_d')
def doctor_d():
    return render_template('doctor.html')

@app.route('/staff_d')
def staff_d():
    return render_template('staff_d.html')

@app.route('/medical_test_d')
def medical_test_d():
    return render_template('medical_test_d.html')

@app.route('/hospital_d')
def hospital_d():
    return render_template('hospital_d.html')

@app.route('/supplier_d')
def supplier_d():
    return render_template('supplier_d.html')
@app.route('/opd_d')
def pat_opd_d():
    return render_template('opd.html')

@app.route('/staff_main')
def staff_main():
    return render_template ('staff_main.html')

@app.route('/pat_main')
def pat_main():
    return render_template ('pat_main.html')

@app.route('/doc_main')
def doc_main():
    return render_template ('doc_main.html')

@app.route('/index')
def index_main():
    return render_template('index.html')

@app.route('/doc_staff')
def doc_staff():
    return render_template('doc_staff.html')

@app.route('/emergency')
def emergency():
    return render_template('emergency.html')

@app.route('/med_purchase')
def med_purchase():
    return render_template('med_purchase.html')

@app.route('/medical_report')
def medical_report():
    return render_template('med_report.html')

@app.route('/medical_report_p')
def medical_report_p():
    return render_template('med_report_p.html')

@app.route('/insurance')
def insurance():
    return render_template('insurance.html')

@app.route('/doctor')
def doctor():
    return render_template('doctor.html')

@app.route('/staff')
def staff():
    return render_template('staff.html')

@app.route('/medical_test')
def medical_test():
    return render_template('medical_test.html')

@app.route('/hospital')
def hospital():
    return render_template('hospital.html')

@app.route('/supplier')
def supplier():
    return render_template('supplier.html')

@app.route('/opd')
def pat_opd():
    return render_template('opd.html')

@app.route('/pat_opd')
def opd():
    return render_template('pat_opd.html')

@app.route('/loginForm', methods=['POST'])
def login_form():
    # Initialize failed login attempts counter in session if not already present
    if 'login_attempts' not in session:
        session['login_attempts'] = 0
        session['login_blocked'] = False

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        connection = get_mysql_connection()
        cur = connection.cursor()

        # Check if email exists in Authentication table
        sql = "SELECT * FROM Authentication WHERE email=%s"
        cur.execute(sql, (email,))
        user = cur.fetchone()

        if user:
            if user['Password'] == password:
                session['login_attempts'] = 0  # Reset login attempts counter on successful login
                session['login_blocked'] = False
                session.pop('login_attempts', None)  # Reset login attempts counter on successful login
                return redirect(url_for(user['redirect_to'], email=email))
            else:
                error = "Incorrect details"
                increment_login_attempts()  # Increment login attempts counter
        else:
            error = "Account doesn't exist"
        
        connection.close()
        return redirect(url_for('main'))

def increment_login_attempts():
    session['login_attempts'] += 1
    if session['login_attempts'] >= 3:  # If login attempts exceed 3
        session['login_blocked'] = True  # Set login blocked flag



# Route for registration page
@app.route('/registrationForm', methods=['GET', 'POST'])
def register():
    print('Inside register')
    # new_email = request.args.get('email')
    if 'user_info' not in session:
        print('User not verified')
        return redirect(url_for('login'))
    # print(request.method)
    # if request.method == 'POST':
    else:
        user_info = session.pop('user_info', None)  # Get verified user info and remove from session
        print( user_info)
        if user_info is None:
            return redirect(url_for('login'))
        
        email = request.args.get('email')
        print(user_info)
        password = request.args.get('password')
        authority = request.args.get('authority')
        connection = get_mysql_connection()
        cur = connection.cursor()

        try:
            # Check if email already exists
            sql = "SELECT * FROM Authentication WHERE email=%s"
            cur.execute(sql, (email,))
            existing_user = cur.fetchone()

            if existing_user:
                error = "User already exists"
                return redirect(url_for('main'), error=error)  # Assuming you handle the error in your main function

            redirect_to = 'index' if authority == 'Staff' else f'index_{authority[0].lower()}'
            # Insert new user into Authentication table
            sql = "INSERT INTO Authentication (email, password, redirect_to) VALUES (%s, %s, %s)"
            cur.execute(sql, (email, password, redirect_to))
            connection.commit()
            return redirect(url_for(redirect_to))

        except Exception as e:
            app.logger.error('Error adding user to database: %s', str(e))
        finally:
            connection.close()

    return redirect(url_for('main'))
@app.route('/get_doctor', methods=['GET'])
def get_doctor():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM doctor")
    doctors = cursor.fetchall()
    connection.close()
    return jsonify(doctors)

@app.route('/get_doctors', methods=['GET'])
def get_doctors():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    filter_clause=None
    column_name = request.args.get('column')
    filter_operator = request.args.get('operator')
    value = request.args.get('value')

    # Define a mapping of operators to SQL clauses
  

    print(column_name)
    print(value)
    print(filter_operator)
    filter_clause = f"{column_name} {filter_operator} '{value}'"
    # Construct the SQL query with parameterized values
    if (filter_clause):
        print(filter_operator)
        sql_query = f"SELECT * FROM doctor WHERE {filter_clause}"
        # print(sql_query)
        cursor.execute(sql_query)
    else:
        # If no filter is provided or operator is not recognized, fetch all doctors
        sql_query = "SELECT * FROM doctor"
        cursor.execute(sql_query)

    doctors = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(doctors)

@app.route('/rename_doctor', methods=['POST'])
def rename_doctor():
    connection = get_mysql_connection()
    cursor = connection.cursor()

    old_column_name = request.json.get('oldColumnName')
    new_column_name = request.json.get('newColumnName')

    try:
        # Rename the columns in the 'doctor' table
        cursor.execute(f"ALTER TABLE doctor CHANGE COLUMN `{old_column_name}` `{new_column_name}` VARCHAR(255);")
        connection.commit()
        return jsonify({'message': 'Columns renamed successfully'})
    except Exception as e:
        connection.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        connection.close()


@app.route('/get_staff', methods=['GET'])
def get_staff():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM staff" )
    staff = cursor.fetchall()
    connection.close()
    return jsonify(staff)

@app.route('/get_staffs', methods=['GET'])
def get_staffs():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    filter_clause=None
    column_name = request.args.get('column')
    filter_operator = request.args.get('operator')
    value = request.args.get('value')

    # Define a mapping of operators to SQL clauses

    filter_clause = f"{column_name} {filter_operator} '{value}'"
    # Construct the SQL query with parameterized values
    if (filter_clause):
        sql_query = f"SELECT * FROM staff WHERE {filter_clause}"
        # print(sql_query)
        cursor.execute(sql_query)
  
    else:
        # If no filter is provided or operator is not recognized, fetch all doctors
        sql_query = "SELECT * FROM staff"
        cursor.execute(sql_query)
    
    
    staffs = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(staffs)

@app.route('/rename_staff', methods=['POST'])
def rename_staff():
    connection = get_mysql_connection()
    cursor = connection.cursor()

    old_column_name = request.json.get('oldColumnName')
    new_column_name = request.json.get('newColumnName')

    try:
        # Rename the columns in the 'doctor' table
        cursor.execute(f"ALTER TABLE staff CHANGE COLUMN `{old_column_name}` `{new_column_name}` VARCHAR(255);")
        connection.commit()
        return jsonify({'message': 'Columns renamed successfully'})
    except Exception as e:
        connection.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        connection.close()


@app.route('/get_medical_report', methods=['GET'])
def get_medical_report():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("select p.prescription_id,p.patient_id,p.date,p.diagnosis,m.test_type,m.result from prescription p natural join med_report m where p.prescription_id = m.prescription_id" )
    medical_report= cursor.fetchall()
    connection.close()
    return jsonify(medical_report)


@app.route('/get_medical_reports', methods=['GET'])
def get_medical_reports():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    filter_clause=None
    column_name = request.args.get('column')
    filter_operator = request.args.get('operator')
    value = request.args.get('value')

    # Define a mapping of operators to SQL clauses
  

    print(column_name)
    print(value)
    print(filter_operator)
    column_name=column_name.lower()
    if column_name == 'prescription_id' or column_name == 'patient_id' or column_name == 'date' or column_name == 'diagnosis':
        filter_clause = f"p.{column_name} {filter_operator} '{value}'"

    elif column_name == 'test_type' or column_name == 'result':
        filter_clause = f"m.{column_name} {filter_operator} '{value}'"
    # Construct the SQL query with parameterized values
    if (filter_clause):
        print(filter_operator)
        sql_query = f"select p.prescription_id,p.patient_id,p.date,p.diagnosis,m.test_type,m.result from prescription p natural join med_report m where p.prescription_id = m.prescription_id and {filter_clause}"
        # print(sql_query)
        cursor.execute(sql_query)
    else:
        # If no filter is provided or operator is not recognized, fetch all doctors
        sql_query = "select p.prescription_id,p.patient_id,p.date,p.diagnosis,m.test_type,m.result from prescription p natural join med_report m where p.prescription_id = m.prescription_id" 
        cursor.execute(sql_query)

    medical_report = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(medical_report)


@app.route('/get_medical_tests', methods=['GET'])
def get_medical_tests():

    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM medical_test")
    doctors = cursor.fetchall()
    connection.close()
    return jsonify(doctors)

@app.route('/get_hospitals', methods=['GET'])
def get_hospitals():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hospital")
    hospital = cursor.fetchall()
    connection.close()
    return jsonify(hospital)

@app.route('/get_hospital', methods=['GET'])
def get_hospital():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    filter_clause = None
    column_name = request.args.get('column')
    filter_operator = request.args.get('operator')
    value = request.args.get('value')

    filter_clause = f"{column_name} {filter_operator} '{value}'"

    # Construct the SQL query with parameterized values
    if (filter_clause):
        sql_query = f"SELECT * FROM hospital WHERE {filter_clause}"
    else:
        # If no filter is provided or operator is not recognized, fetch all doctors
        sql_query = "SELECT * FROM hospital"

    cursor.execute(sql_query)
    hospital = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(hospital)

@app.route('/rename_hospital', methods=['POST'])
def rename_hospital():
    connection = get_mysql_connection()
    cursor = connection.cursor()

    old_column_name = request.json.get('oldColumnName')
    new_column_name = request.json.get('newColumnName')

    try:
        cursor.execute(f"ALTER TABLE hospital CHANGE COLUMN {old_column_name} {new_column_name} VARCHAR(255);")
        connection.commit()
        return jsonify({'message': 'Columns renamed successfully'})
    except Exception as e:
        connection.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        connection.close()


@app.route('/get_suppliers', methods=['GET'])
def get_suppliers():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM supplier")
    supplier = cursor.fetchall()
    connection.close()
    return jsonify(supplier)

@app.route('/get_patient_p', methods=['GET'])
def get_patient_p():
    email = request.args.get('email')
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM patient where email = %s", (email,))
    patients = cursor.fetchall()
    connection.close()
    return jsonify(patients)
@app.route('/get_patient', methods=['GET'])
def get_patient():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM patient")
    patients = cursor.fetchall()
    connection.close()
    return jsonify(patients)
@app.route('/get_opds', methods=['GET'])
def get_opds():
    opd_type = request.args.get('opd_type')
    doctor_id = request.args.get('doctor_id')
    print(doctor_id)
    # Connect to MySQL
    connection = get_mysql_connection()
    cursor = connection.cursor()

    if opd_type == 'today':
        # Fetch today's OPD data for the specified doctor
        query = "SELECT * FROM opd WHERE doctor_id = %s AND DATE(date) = CURDATE()"
        
    else:
        # Fetch total OPD data for the specified doctor
        query = "SELECT * FROM opd WHERE doctor_id = %s ORDER BY Date DESC, Serial_Number ASC"

    try:
        cursor.execute(query, (doctor_id,))
        opd_data = cursor.fetchall()
        for opd in opd_data:
            opd['Time'] = str(opd['Time'])
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        cursor.close()
        connection.close()
    return jsonify(opd_data)
@app.route('/get_opd', methods=['GET'])
def get_opd():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM opd ORDER BY Date DESC, Serial_Number ASC")
    opds = cursor.fetchall()
    connection.close()
    for opd in opds:
        opd['Time'] = str(opd['Time'])
    return jsonify(opds)

@app.route('/get_opd_p', methods=['GET'])
def get_opd_p():
    email = request.args.get('email')
    connection = get_mysql_connection()
    cursor = connection.cursor()
    try:
        # Retrieve patient_id using the provided email
        cursor.execute("SELECT * FROM patient WHERE email = %s", (email,))
        patient = cursor.fetchone()  # Assuming there is only one patient with the given email
        patient_id = patient['Patient_ID']
        print(patient_id)
        # Retrieve insurance number using the patient_id
        cursor.execute("SELECT * FROM opd where patient_id = %s ORDER BY Date DESC, Serial_Number ASC", (patient_id,))
        opds = cursor.fetchall()
        print(opds)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        cursor.close()
        connection.close()
    for opd in opds:
        opd['Time'] = str(opd['Time'])
    return jsonify(opds)

@app.route('/get_emergencies', methods=['GET'])
def get_emergencies():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM emergency ORDER BY date ASC")
    emergencies = cursor.fetchall()
    connection.close()
    # Convert timedelta objects to string
    for emergency in emergencies:
        emergency['Time'] = str(emergency['Time'])
    return jsonify(emergencies)

@app.route('/get_pres', methods=['GET'])
def get_pres():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("select * from prescription")
    pres = cursor.fetchall()
    connection.close()
    return jsonify(pres)

@app.route('/get_med', methods=['GET'])
def get_med():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM medicines_equipments")
    med = cursor.fetchall()
    connection.close()
    return jsonify(med)

@app.route('/get_purchase', methods=['GET'])
def get_purchase():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM purchase_order")
    purchase = cursor.fetchall()
    connection.close()
    return jsonify(purchase)


@app.route('/get_insurance_p', methods=['GET'])
def get_insurance_p():
    email = request.args.get('email')

    # Connect to MySQL
    connection = get_mysql_connection()
    cursor = connection.cursor()

    try:
        # Retrieve patient_id using the provided email
        cursor.execute("SELECT * FROM patient WHERE email = %s", (email,))
        patient = cursor.fetchone()  # Assuming there is only one patient with the given email
        patient_id = patient['Patient_ID']
        print(patient_id)
        # Retrieve insurance number using the patient_id
        cursor.execute("SELECT * FROM claimed_by WHERE patient_id = %s", (patient_id,))
        insurance = cursor.fetchone()
        insurance_number = insurance['Insurance_Number']
        print(insurance_number)
        # Retrieve insurance data using the insurance number
        cursor.execute("SELECT * FROM insurance WHERE Insurance_Number = %s", (insurance_number,))
        insurance_data = cursor.fetchall()
        print(insurance_data)
        return jsonify(insurance_data)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        cursor.close()
        connection.close()
@app.route('/get_insurance', methods=['GET'])
def get_insurance():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM insurance")
    insurance = cursor.fetchall()
    connection.close()
    return jsonify(insurance)

@app.route('/add_doctor', methods=['POST'])
def add_doctor():
    # Add logic to handle adding a doctor
    if request.method == 'POST':
        doctor_id = request.form['doctor_id']
        first_name = request.form['first_name']
        middle_name = request.form['middle_name']  # Middle name is optional
        last_name = request.form['last_name']
        dob = request.form['dob']
        gender = request.form['gender']
        email = request.form['email']
        phone_number = request.form['phone_number']
        specialization = request.form['specialization']
        experience = request.form['experience']
        street_number = request.form['street_number']
        street_name = request.form['street_name']
        apartment_number = request.form['apartment_number']  # Apartment number is optional
        city = request.form['city']
        pincode = request.form['pincode']
        day = request.form['day']
        time = request.form['Time']

        contact_numbers = [number.strip() for number in phone_number.split(",")]
        day_num = [number.strip() for number in day.split(",")]
        time_num = [number.strip() for number in time.split(",")]
        connection = get_mysql_connection()
        cur = connection.cursor()
        try:
            cur.execute("INSERT INTO doctor (doctor_id, First_Name, Middle_Name, Last_Name, DOB, Gender, Email, Specialization, Experience, Street_Number, Street_Name, Apartment_Number, City, Pincode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (doctor_id, first_name, middle_name, last_name, dob, gender, email, specialization, experience, street_number, street_name, apartment_number, city, pincode))
            
            for number in contact_numbers:
                cur.execute("INSERT INTO Doctor_Contact (Doctor_id, phone_number) VALUES (%s, %s)", (doctor_id, number))

            for number in range(len(time_num)):
                cur.execute("INSERT INTO Doctor_Availability (Doctor_id, day, time) VALUES (%s, %s,%s)", (doctor_id, day_num[number], time_num[number]))

            connection.commit()

            app.logger.info('Doctor added successfully: doctor_id - %s, Name - %s %s %s, DOB - %s, Gender - %s, Email - %s, Specialization - %s, Experience - %s, Address - %s %s %s, %s, %s',
                            doctor_id, first_name, middle_name, last_name, dob, gender, email, specialization, experience, street_number, street_name, apartment_number, city, pincode)
            return redirect(url_for('doctor'))
        except Exception as e:
            connection.rollback()
            app.logger.error('Error adding doctor to database: %s', str(e))
            return jsonify({'error':str(e)}),500
        finally:
            connection.close()

        


@app.route('/edit_doctor')
def edit_doctor():
    doctor_id = request.args.get('id')
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM doctor WHERE Doctor_ID = %s", (doctor_id,))
    doctor = cursor.fetchone()
    cursor.close()
    return render_template('edit_doctor.html', doctor=doctor)



@app.route('/update_doctor', methods=['POST'])
def update_doctor():
    # Retrieve form data
    doctor_id = request.form['doctor_id']
    first_name = request.form['first_name']
    middle_name = request.form['middle_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    gender = request.form['gender']
    email = request.form['email']
    specialization = request.form['specialization']
    experience = request.form['experience']
    street_number = request.form['street_number']
    street_name = request.form['street_name']
    apartment_number = request.form['apartment_number']
    city = request.form['city']
    pincode = request.form['pincode']

    # Update doctor information in the database
    connection = get_mysql_connection()
    cursor = connection.cursor()
    query = """UPDATE doctor SET 
               First_Name = %s, 
               Middle_Name = %s, 
               Last_Name = %s, 
               DOB = %s, 
               Gender = %s, 
               Email = %s, 
               Specialization = %s, 
               Experience = %s, 
               Street_Number = %s, 
               Street_Name = %s, 
               Apartment_Number = %s, 
               City = %s, 
               Pincode = %s 
               WHERE Doctor_ID = %s"""
    cursor.execute(query, (first_name, middle_name, last_name, dob, gender, email, specialization, experience, street_number, street_name, apartment_number, city, pincode, doctor_id))
    connection.commit()
    connection.close()


    # Redirect to doctor list page after update
    return redirect(url_for('doctor'))





@app.route('/delete_doctor', methods=['DELETE'])
def delete_doctor():
    doctor_id = request.json.get('id')
    if doctor_id is None:
        return jsonify({"error": "Doctor ID is missing"}), 400
    
    connection = get_mysql_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM doctor_contact WHERE doctor_id = %s", (doctor_id,))
        cursor.execute("DELETE FROM doctor_availability WHERE doctor_id = %s", (doctor_id,))
        cursor.execute("DELETE FROM doctor WHERE doctor_id = %s", (doctor_id,))
        connection.commit()
        return jsonify({"message": "Doctor deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()


@app.route('/edit_purchase', methods=['GET','POST'])
def edit_purchase():
    Bill_Number = request.args.get('id')
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM purchase_order WHERE Bill_Number = %s", (Bill_Number,))
    purchase_order = cursor.fetchone()
    connection.close()
    return render_template('edit_purchase_order.html', purchase_order=purchase_order)

@app.route('/update_purchase_order', methods=['POST'])
def update_purchase_order():
    # Retrieve form data
    Bill_Number = request.form['Bill_Number']
    Quantity = request.form['Quantity']
    Amount_Paid = request.form['Amount_Paid']

    # Update patient information in the database
    connection = get_mysql_connection()
    cursor = connection.cursor()
    query = """UPDATE purchase_order SET 
               Quantity = %s,
               Amount_Paid = %s
               WHERE Bill_Number = %s"""
    cursor.execute(query, (Quantity, Amount_Paid,Bill_Number))
    connection.commit()
    connection.close()
    
    # Redirect to a specific page after updating patient information
    # Adjust the URL as needed
    return redirect(url_for('med_purchase'))  # Update 'some_page' with the appropriate route


@app.route('/delete_purchase', methods=['DELETE'])
def delete_purchase():
    bill_number = request.json.get('id')
    if bill_number is None:
        return jsonify({"error": "bill_number is missing"}), 400
    
    connection = get_mysql_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM Ordered_by WHERE bill_number = %s", (str(bill_number),))
        cursor.execute("DELETE FROM supply_transaction WHERE bill_number = %s", (str(bill_number),))
        cursor.execute("DELETE FROM purchase_order WHERE bill_number = %s", (str(bill_number),))
        connection.commit()
        return jsonify({"message": "Bill deleted successfully"})
    except Exception as e:
        app.logger.error('Error deleting prescription entry from database: %s', str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

@app.route('/edit_emergency', methods=['GET','POST'])
def edit_emergency():
    patient_id = request.args.get('id')
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM emergency WHERE patient_id = %s", (patient_id,))
    emergency = cursor.fetchone()
    connection.close()
    return render_template('edit_emergency.html', emergency=emergency)

@app.route('/update_Emergency', methods=['POST'])
def update_emergency():
    # Retrieve form data
    patient_id = request.form['Patient_ID']
    License_Number = request.form['License_Number']
    Disease = request.form['Disease']
    date = request.form['date']
    time = request.form['Time']

    # Update patient information in the database
    connection = get_mysql_connection()
    cursor = connection.cursor()
    query = """UPDATE emergency SET 
               License_Number = %s,
               Disease = %s,
               date = %s,
               time = %s
               WHERE patient_id = %s"""
    cursor.execute(query, (License_Number, Disease, date, time,patient_id))
    connection.commit()
    connection.close()
    
    # Redirect to a specific page after updating patient information
    # Adjust the URL as needed
    return redirect(url_for('emergency'))  # Update 'some_page' with the appropriate route


@app.route('/delete_emergency', methods=['DELETE'])
def delete_emergency():
    patient_id = request.json.get('id')
    if patient_id is None:
        return jsonify({"error": "patient id is missing"}), 400
    
    connection = get_mysql_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM Referred_to WHERE patient_id = %s", (str(patient_id),))
        cursor.execute("DELETE FROM recommendation WHERE patient_id = %s", (str(patient_id),))
        cursor.execute("DELETE FROM emergency WHERE patient_id = %s", (str(patient_id),))
        connection.commit()
        return jsonify({"message": "Emergency deleted successfully"})
    except Exception as e:
        app.logger.error('Error deleting prescription entry from database: %s', str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()


@app.route('/edit_report')
def edit_report():
    prescription_id = request.args.get('id')
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("select p.prescription_id,p.patient_id,p.date,p.diagnosis,m.test_type,m.result from prescription p natural join med_report m where p.prescription_id = m.prescription_id and p.prescription_id = %s", (prescription_id,))
    report = cursor.fetchone()
    cursor.close()
    return render_template('edit_med_report.html', report=report)



@app.route('/update_report', methods=['POST'])
def update_report():
    # Retrieve form data
    result = request.form['Result']
    priscription_id = request.form['prescription_id']

    # Update doctor information in the database
    connection = get_mysql_connection()
    cursor = connection.cursor()
    query = """UPDATE med_report SET 
               result = %s
               WHERE prescription_id = %s"""
    cursor.execute(query, (result, priscription_id))
    connection.commit()
    connection.close()


    # Redirect to doctor list page after update
    return redirect(url_for('medical_report'))


@app.route('/edit_prescription', methods=['GET','POST'])
def edit_prescription():
    prescription_id = request.args.get('id')
    reason = request.args.get('reason')
    print(reason)
    connection = get_mysql_connection()
    cursor = connection.cursor()

    try:
        query = """UPDATE prescription SET 
                   reason = %s
                   WHERE Prescription_ID = %s"""
        cursor.execute(query, (reason, prescription_id))
        connection.commit()  # Commit the transaction after executing the query

        # Fetch the updated prescription
        cursor.execute("SELECT * FROM prescription WHERE Prescription_ID = %s", (prescription_id,))
        prescription = cursor.fetchone()
    except Exception as e:
        # Handle exceptions, log error messages, etc.
        print("Error updating prescription:", e)
        prescription = None  # Set prescription to None in case of an error

    connection.close()

    return render_template('edit_prescription.html', prescription=prescription)

@app.route('/update_prescription', methods=['POST'])
def update_prescription():
    # Retrieve form data
    Prescription_ID = request.form['Prescription_ID']
    Patient_ID = request.form['Patient_ID']
    Diagnosis = request.form['Diagnosis']
    date = request.form['Date']
    remarks = request.form['remarks']

    # Update patient information in the database
    if '<script>alert' in remarks:
        # If a potentially malicious script is found, display an alert
        return '''
            <script>
                alert("Hacked");
                window.history.back();
            </script>
        '''
    try:
        connection = get_mysql_connection()
        cursor = connection.cursor()
        query = """UPDATE prescription SET 
                Patient_ID = %s,
                Diagnosis = %s,
                date = %s,
                remarks = %s
                WHERE Prescription_ID = %s"""
        cursor.execute(query, (Patient_ID, Diagnosis, date, remarks,Prescription_ID))
        connection.commit()
        connection.close()
        print(1)
    except Exception as e:
        print("Error updating prescription:", str(e))
    # Redirect to a specific page after updating patient information
    # Adjust the URL as needed
    return redirect(url_for('emergency'))  # Update 'some_page' with the appropriate route



@app.route('/delete_pres', methods=['DELETE'])
def delete_pres():
    prescription_id = request.json.get('id')
    if prescription_id is None:
        return jsonify({"error": "prescription_id is missing"}), 400
    
    connection = get_mysql_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM prescribes WHERE prescription_id = %s", (str(prescription_id),))
        cursor.execute("DELETE FROM prescribed_to WHERE prescription_id = %s", (str(prescription_id),))
        cursor.execute("DELETE FROM medication WHERE prescription_id = %s", (str(prescription_id),))
        cursor.execute("DELETE FROM appointment WHERE prescription_id = %s", (str(prescription_id),))
        cursor.execute("DELETE FROM prescription WHERE prescription_id = %s", (str(prescription_id),))
        connection.commit()
        return jsonify({"message": "Emergency deleted successfully"})
    except Exception as e:
        app.logger.error('Error deleting prescription entry from database: %s', str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

@app.route('/edit_staff')
def edit_staff():
    staff_id = request.args.get('id')
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM staff WHERE Staff_ID = %s", (staff_id,))
    staff = cursor.fetchone()
    connection.close()
    return render_template('edit_staff.html', staff=staff)


@app.route('/update_staff', methods=['POST'])
def update_staff():
    # Retrieve form data
    Staff_ID = request.form['staff_id']
    First_Name = request.form['first_name']
    Middle_Name = request.form['middle_name']
    Last_Name = request.form['last_name']

    Join_Date = request.form['join_date']
    # Phone_Number = request.form['phone_number']
    DOB= request.form['dob']

    Street_Number = request.form['street_number']
    Street_Name = request.form['street_name']
    Apartment_Number = request.form['apartment_number']
    City = request.form['city']
    Pincode = request.form['pincode']

    Email = request.form['email']
    Gender = request.form['gender']
    Salary = request.form['Salary']

    # Update doctor information in the database
    connection = get_mysql_connection()
    cursor = connection.cursor()
    query = """UPDATE staff SET 
               First_Name = %s, 
               Middle_Name = %s, 
               Last_Name = %s, 
               Join_date = %s,
               DOB = %s, 
               Street_Number = %s, 
               Street_Name = %s, 
               Apartment_Number = %s, 
               City = %s, 
               Pincode = %s,
               Email = %s,
               Gender = %s,
               Salary = %s
               WHERE Staff_ID = %s"""
    cursor.execute(query, (First_Name, Middle_Name, Last_Name, Join_Date, DOB, Street_Number,Street_Name, Apartment_Number, City, Pincode, Email, Gender, Salary,Staff_ID))
    connection.commit()
    connection.close()

    # Redirect to doctor list page after update
    return redirect(url_for('staff'))


@app.route('/delete_staff', methods=['DELETE'])
def delete_staff():
    staff_id = request.json.get('id')
    if staff_id is None:
        return jsonify({"error": "Staff ID is missing"}), 400
    
    connection = get_mysql_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM staff_contact WHERE staff_id = %s", (staff_id,))
        cursor.execute("DELETE FROM staff WHERE staff_id = %s", (staff_id,))
        connection.commit()
        return jsonify({"message": "Staff deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()
@app.route('/edit_hospital', methods=['GET','POST'])
def edit_hospital():
    license_number = request.args.get('id')
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hospital WHERE license_number = %s", (license_number,))
    hospital = cursor.fetchone()
    connection.close()

    return render_template('edit_hospital.html', hospital=hospital)



@app.route('/update_hospital', methods=['POST'])
def update_hospital():
    # Retrieve form data
    license_number = request.form['License_Number']
    name = request.form['Name']
    street_number = request.form['street_number']
    street_name = request.form['street_name']
    apartment_number = request.form['apartment_number']  # Apartment number is optional
    city = request.form['city']
    pincode = request.form['pincode']
    
    # Update medical test information in the database
    connection = get_mysql_connection()
    cursor = connection.cursor()
    query = """UPDATE hospital SET 
               name = %s, 
               street_number = %s, 
               street_name = %s, 
               apartment_number = %s, 
               city = %s, 
               pincode = %s
               WHERE license_number = %s"""
    cursor.execute(query, (name, street_number, street_name, apartment_number, city, pincode, license_number))
    connection.commit()
    connection.close()
    return redirect(url_for('hospital'))



@app.route('/delete_hospital', methods=['DELETE'])
def delete_hospital():
    license_number = request.json.get('id')
    if license_number is None:
        return jsonify({"error": "License Number is missing"}), 400
    
    connection = get_mysql_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM hospital_contact WHERE license_number = %s", (license_number,))
        cursor.execute("DELETE FROM hospital WHERE license_number = %s", (license_number,))
        connection.commit()
        return jsonify({"message": "Hospital deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

@app.route('/edit_patient', methods=['GET','POST'])
def edit_patient():
    patient_id = request.args.get('id')
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM patient WHERE patient_id = %s", (patient_id,))
    patient = cursor.fetchone()
    connection.close()
    return render_template('edit_patient.html', patient=patient)

@app.route('/update_patient', methods=['POST'])
def update_patient():
    # Retrieve form data
    patient_id = request.form['patient_id']
    first_name = request.form['first_name']
    middle_name = request.form['middle_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    street_number = request.form['street_number']
    street_name = request.form['street_name']
    apartment_number = request.form.get('apartment_number', None)  # Optional field, use get() to handle absence
    city = request.form['city']
    pincode = request.form['pincode']
    gender = request.form['gender']
    email = request.form['email']

    # Update patient information in the database
    connection = get_mysql_connection()
    cursor = connection.cursor()
    query = """UPDATE patient SET 
               first_name = %s,
               middle_name = %s,
               last_name = %s,
               dob = %s,
               street_number = %s,
               street_name = %s,
               apartment_number = %s,
               city = %s,
               pincode = %s,
               gender = %s,
               email = %s
               WHERE patient_id = %s"""
    cursor.execute(query, (first_name, middle_name, last_name, dob, street_number, street_name, apartment_number, city, pincode, gender, email, patient_id))
    connection.commit()
    connection.close()
    
    # Redirect to a specific page after updating patient information
    # Adjust the URL as needed
    return redirect(url_for('pat_opd'))  # Update 'some_page' with the appropriate route

@app.route('/delete_patient', methods=['DELETE'])
def delete_patient():
    patient_id = request.json.get('id')
    if patient_id is None:
        return jsonify({"error": "patient id is missing"}), 400
    
    connection = get_mysql_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM patient_contact WHERE patient_id = %s", (patient_id,))
        cursor.execute("DELETE FROM patient_allergy WHERE patient_id = %s", (patient_id,))
        cursor.execute("DELETE FROM patient WHERE patient_id = %s", (patient_id,))
        connection.commit()
        return jsonify({"message": "Patient deleted successfully"})
    except Exception as e:
        app.logger.error('Error adding patient to database: %s', str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

@app.route('/edit_opd', methods=['GET', 'POST'])
def edit_opd():
    serial_number = request.args.get('serialNumber')
    date = request.args.get('date')
    
    if not serial_number or not date:
        return "Error: serialNumber and date are required parameters."
    
    connection = get_mysql_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM opd WHERE Serial_Number = %s AND Date = %s", (serial_number, date))
        opd = cursor.fetchone()
    except Exception as e:
        app.logger.error('Error retrieving OPD record from database: %s', str(e))
        return "Error retrieving OPD record from database."
    finally:
        connection.close()
    
    if opd is None:
        return "OPD record not found."
    
    # Assuming 'edit_supplier.html' template needs 'opd_record' as context
    return render_template('edit_opd.html', opd=opd)



@app.route('/update_opd', methods=['POST'])
def update_opd():
    # Retrieve form data
    serial_number = request.form['Serial_Number']
    date = request.form['Date']
    time = request.form['Time']
    patient_id = request.form['Patient_ID']
    doctor_id = request.form['Doctor_ID']
    case_type = request.form['Case_Type']

    # Update OPD information in the database
    connection = get_mysql_connection()
    cursor = connection.cursor()
    query = """UPDATE opd SET 
               Time = %s,
               Patient_ID = %s,
               Doctor_ID = %s,
               Case_Type = %s
               WHERE Serial_Number = %s AND Date = %s"""
    cursor.execute(query, (time, patient_id, doctor_id, case_type, serial_number, date))
    connection.commit()
    connection.close()
    
    # Redirect to a specific page after updating OPD information
    # Adjust the URL as needed
    return redirect(url_for('pat_opd'))

@app.route('/delete_OPD', methods=['DELETE'])
def delete_OPD():
    data = request.json
    serial_number = data.get('serialNumber')
    date = data.get('date')
    
    if not serial_number or not date:
        return jsonify({"error": "Serial number or date is missing"}), 400
    
    
    connection = get_mysql_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM opd WHERE Serial_Number = %s AND Date = %s", (serial_number, date))
        connection.commit()
        return jsonify({"message": "OPD deleted successfully"})
    except Exception as e:
        app.logger.error('Error deleting OPD entry from database: %s', str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

@app.route('/edit_test', methods=['GET','POST'])
def edit_test():
    test_type = request.args.get('id')
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM medical_test WHERE test_type = %s", (test_type,))
    test = cursor.fetchone()
    connection.close()
    return render_template('edit_medical_test.html', test=test)



@app.route('/update_test', methods=['POST'])
def update_test():
    # Retrieve form data
    
    test_type = request.form['Test_Type']
    lab_name = request.form['Lab_Name']
    
    # Update medical test information in the database
    connection = get_mysql_connection()
    cursor = connection.cursor()
    query = "UPDATE medical_test SET Lab_Name = %s WHERE Test_type = %s"
    cursor.execute(query, (lab_name, test_type))
    connection.commit()
    connection.close()
    return redirect(url_for('medical_test'))

@app.route('/delete_test', methods=['DELETE'])
def delete_test():
    test_name = request.json.get('id')
    if test_name is None:
        return jsonify({"error": "test name  is missing"}), 400
    
    connection = get_mysql_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM medical_test WHERE test_type = %s", (test_name,))
        connection.commit()
        return jsonify({"message": "Test deleted successfully"})
    except Exception as e:
        app.logger.error('Error deleting OPD entry from database: %s', str(e))       
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()


@app.route('/edit_supplier', methods=['GET','POST'])
def edit_supplier():
    supplier_id = request.args.get('id')
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM supplier WHERE supplier_id = %s", (supplier_id,))
    supplier = cursor.fetchone()
    connection.close()
    return render_template('edit_supplier.html', supplier=supplier)



@app.route('/update_supplier', methods=['POST'])
def update_supplier():
    # Retrieve form data
    supplier_id = request.form['Supplier_ID']
    agency_name = request.form['Agency_Name']
    street_number = request.form['street_number']
    street_name = request.form['street_name']
    apartment_number = request.form['apartment_number']  # Apartment number is optional
    city = request.form['city']
    pincode = request.form['pincode']
    account_number = request.form['Account_Number']
    bank_name = request.form['Bank_Name']  # Apartment number is optional
    IFSC_code = request.form['IFSC_Code']
    branch = request.form['Branch']

    
    # Update medical test information in the database
    connection = get_mysql_connection()
    cursor = connection.cursor()
    query = """UPDATE supplier SET 
               agency_name = %s, 
               street_number = %s, 
               street_name = %s, 
               apartment_number = %s, 
               city = %s, 
               pincode = %s,
               account_number = %s, 
               bank_name = %s, 
               IFSC_code = %s,
               branch = %s
               WHERE supplier_id = %s"""
    cursor.execute(query, (agency_name, street_number, street_name, apartment_number, city, pincode, account_number, bank_name, IFSC_code, branch,supplier_id))
    connection.commit()
    connection.close()
    return redirect(url_for('supplier'))

@app.route('/delete_supplier', methods=['DELETE'])
def delete_supplier():
    supplier_id = request.json.get('id')
    if supplier_id is None:
        return jsonify({"error": "supplier  is missing"}), 400
    
    connection = get_mysql_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM supplier_contact WHERE supplier_id = %s", (supplier_id,))
        cursor.execute("DELETE FROM supplier WHERE supplier_id = %s", (supplier_id,))
        connection.commit()
        return jsonify({"message": "Supplier deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()


@app.route('/edit_med', methods=['GET','POST'])
def edit_med():
    item_id = request.args.get('id')
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM medicines_equipments WHERE item_id = %s", (item_id,))
    medicines_equipments = cursor.fetchone()
    connection.close()
    return render_template('edit_medicine_equipment.html', medicines_equipments=medicines_equipments)

@app.route('/update_Medicines_Equipments', methods=['POST'])
def update_Medicines_Equipments():
    # Retrieve form data
    Item_ID = request.form['Item_ID']
    Medicine_name = request.form['Medicine_name']
    Expiry_date = request.form['Expiry_date']
    Stock = request.form['Stock']


    # Update patient information in the database
    connection = get_mysql_connection()
    cursor = connection.cursor()
    query = """UPDATE medicines_equipments SET 
               Medicine_name = %s,
               Expiry_date = %s,
               Stock = %s
               WHERE Item_ID = %s"""
    cursor.execute(query, (Medicine_name, Expiry_date, Stock,Item_ID))
    connection.commit()
    connection.close()
    
    # Redirect to a specific page after updating patient information
    # Adjust the URL as needed
    return redirect(url_for('med_purchase'))  # Update 'some_page' with the appropriate route


@app.route('/delete_med', methods=['DELETE'])
def delete_med():
    item_id = request.json.get('id')
    if item_id is None:
        return jsonify({"error": "Item_Id   is missing"}), 400
    
    connection = get_mysql_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM supply_transaction WHERE item_id = %s", (item_id,))
        cursor.execute("DELETE FROM medicines_equipments WHERE item_id = %s", (item_id,))
        connection.commit()
        return jsonify({"message": "Medicine deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

@app.route('/edit_insurance', methods=['GET','POST'])
def edit_insurance():
    insurance_number = request.args.get('id')
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM insurance WHERE insurance_number = %s", (insurance_number,))
    insurance = cursor.fetchone()
    connection.close()
    return render_template('edit_insurance.html', insurance=insurance)



@app.route('/update_insurance', methods=['POST'])
def update_insurance():
    # Retrieve form data
    Insurance_Number = request.form['insurance_Number']
    Issue_Date = request.form['Issue_Date']
    Expiry_Date = request.form['Expiry_Date']
    Wallet_Balance = request.form['Wallet_Balance']
    Reimbursement_Status = request.form['Reimbursement_Status']

    
    # Update medical test information in the database
    connection = get_mysql_connection()
    cursor = connection.cursor()
    query = """UPDATE insurance SET 
               Issue_Date = %s, 
               Expiry_Date = %s, 
               Reimbursement_Status = %s, 
               Wallet_Balance = %s
               WHERE Insurance_Number = %s"""
    cursor.execute(query, (Issue_Date, Expiry_Date, Reimbursement_Status, Wallet_Balance, Insurance_Number))
    connection.commit()
    connection.close()
    return redirect(url_for('insurance'))


@app.route('/delete_insurance', methods=['DELETE'])
def delete_ins():
    insurance_number = request.json.get('id')
    if insurance_number is None:
        return jsonify({"error": "Insurance Number  is missing"}), 400
    
    connection = get_mysql_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM claimed_by WHERE insurance_number = %s", (insurance_number,))
        cursor.execute("DELETE FROM claimed_for WHERE insurance_number = %s", (insurance_number,))
        cursor.execute("DELETE FROM insurance WHERE insurance_number = %s", (insurance_number,))
        connection.commit()
        return jsonify({"message": "Medicine deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

@app.route('/add_test', methods=['POST'])
def add_medical_test(): 
    if request.method == 'POST':
        Test_Type = request.form['Test_Type']
        Lab_Name = request.form['Lab_Name']
       
        app.logger.info('Received POST request to add test entry: Test_Type - %s, Lab_Name - %s', Test_Type,Lab_Name)
        connection = get_mysql_connection()
        cur = connection.cursor()
    try:
        cur.execute("INSERT INTO medical_test (Test_Type, Lab_Name) VALUES ( %s, %s)", (Test_Type, Lab_Name))
        connection.commit()
        app.logger.info('OPD Entry added successfully: Test_Type - %s, Lab_Name - %s ', Test_Type, Lab_Name)
        
    except Exception as e:
        app.logger.error('Error adding OPD entry to database: %s', str(e))
    finally:
        connection.close()
        
    return redirect(url_for('medical_test'))


@app.route('/add_staff', methods=['POST'])
def add_staff():
    # Add logic to handle adding an opd
    if request.method == 'POST':
        Staff_ID = request.form['Staff_ID']
        First_Name = request.form['First_Name']
        Middle_Name = request.form['Middle_Name']
        Last_Name = request.form['Last_Name']

        Join_Date = request.form['Join_Date']
        Phone_Number = request.form['Phone_Number']
        DOB= request.form['DOB']

        Street_Number = request.form['Street_Number']
        Street_Name = request.form['Street_Name']
        Apartment_Number = request.form['Apartment_Number']
        City = request.form['City']
        Pincode = request.form['Pincode']

        Email = request.form['Email']
        Gender = request.form['Gender']
        Salary = request.form['Salary']
        
        # Splitting phone numbers by comma and stripping whitespace
        Contact_Numbers = [number.strip() for number in Phone_Number.split(",")]

        app.logger.info('Received POST request to add Staff entry: Staff_ID - %d, First_Name - %s, Middle_Name - %s, Last_Name - %s, Join_Date- %d, Phone_Number - %s, DOB - %d, Street_Number - %d, Street_Name - %s, Apartment_Number - %d, City - %s, Pincode - %d, Email - %s, Gender - %s, Salary - %d', Staff_ID, First_Name, Middle_Name, Last_Name, Join_Date, Phone_Number, DOB, Street_Number, Street_Name, Apartment_Number, City, Pincode, Email, Gender, Salary)
        
        connection = get_mysql_connection()
        cur = connection.cursor()
    try:
        cur.execute("INSERT INTO staff (Staff_ID, First_Name, Middle_Name, Last_Name, Join_Date, DOB, Street_Number, Street_Name, Apartment_Number, City, Pincode, Email, Gender, Salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (Staff_ID, First_Name, Middle_Name, Last_Name, Join_Date, DOB, Street_Number, Street_Name, Apartment_Number, City, Pincode, Email, Gender, Salary))
        for number in Contact_Numbers:
            cur.execute("INSERT INTO staff_contact (Staff_ID, Phone_Number) VALUES (%s, %s)", (Staff_ID, number))

        connection.commit()
        app.logger.info('Staff entry added successfully: Staff_ID - %d, First_Name - %s, Middle_Name - %s, Last_Name - %s, Join_Date- %d, Phone_Number - %s, DOB - %d, Street_Number - %d, Street_Name - %s, Apartment_Number - %d, City - %s, Pincode - %d, Email - %s, Gender - %s, Salary - %d',  Staff_ID, First_Name, Middle_Name, Last_Name, Join_Date, Phone_Number, DOB, Street_Number, Street_Name, Apartment_Number, City, Pincode, Email, Gender, Salary)
        
    except Exception as e:
        app.logger.error('Error adding Staff entry to database: %s', str(e))
    finally:
        connection.close()
        
    return redirect(url_for('staff'))


@app.route('/add_new', methods=['POST'])
def add_patient_new():
    # Add logic to handle adding a doctor
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        first_name = request.form['first_name']
        middle_name = request.form['middle_name'] # Middle name is optional
        last_name = request.form['last_name']
        dob = request.form['dob']
        phone_number = request.form['phone_number']
        street_number = request.form['street_number']
        street_name = request.form['street_name']
        apartment_number = request.form['apartment_number']  # Apartment number is optional
        city = request.form['city']
        pincode = request.form['pincode']
        gender = request.form['gender']
        allergies = request.form['allergies']  # Allergies are optional
        email = request.form['email']
        Serial_Number = request.form['Serial_Number']
        Date = request.form['Date']
        Time = request.form['Time']
        Doctor_ID = request.form['Doctor_ID']
        Case_Type = request.form['Case_Type']

        # Splitting phone numbers by comma and stripping whitespace
        contact_numbers = [number.strip() for number in phone_number.split(",")]
        Allergies_num = [number1.strip() for number1 in allergies.split(",")]

        connection = get_mysql_connection()
        cur = connection.cursor()
        try:
            # Inserting patient details into the Patient table
            cur.execute("INSERT INTO Patient (patient_id, First_Name, Middle_Name, Last_Name, DOB, Street_Number, Street_Name, Apartment_Number, City, Pincode, Gender, Email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (patient_id, first_name, middle_name, last_name, dob, street_number, street_name, apartment_number, city, pincode, gender, email))
            cur.execute("INSERT INTO opd (Serial_Number, Date, Time, Patient_ID, Doctor_ID, Case_Type) VALUES ( %s, %s, %s, %s, %s, %s)", (Serial_Number, Date, Time, patient_id, Doctor_ID, Case_Type))
            

            # Inserting patient contact numbers into the Patient_Contact table
            for number in contact_numbers:
                cur.execute("INSERT INTO Patient_Contact (patient_id, phone_number) VALUES (%s, %s)", (patient_id, number))
            
            # Inserting patient contact numbers into the Patient_Allergies table
            for number1 in Allergies_num:
                cur.execute("INSERT INTO Patient_Allergy (patient_id, Allergy) VALUES (%s, %s)", (patient_id, number1))

            connection.commit()
            app.logger.info('Patient added successfully: Name - %s %s %s, DOB - %s, Address - %s %s %s, %s, %s, Gender - %s, Allergies - %s, Email - %s',
                            first_name, middle_name, last_name, dob, street_number, street_name, apartment_number, city, pincode, gender, allergies, email)
        except Exception as e:
            app.logger.error('Error adding patient to database: %s', str(e))
        finally:
            connection.close()
        return redirect(url_for('pat_opd'))
    
@app.route('/add_exist', methods=['POST'])
def add_patient_exist():
    # Add logic to handle adding a doctor
    if request.method == 'POST':
        patient_id = request.form['Patient_ID']
        Serial_Number = request.form['Serial_Number']
        Date = request.form['Date']
        Time = request.form['Time']
        Doctor_ID = request.form['Doctor_ID']
        Case_Type = request.form['Case_Type']

        connection = get_mysql_connection()
        cur = connection.cursor()
        try:
            # Inserting patient details into the Patient table
            cur.execute("INSERT INTO opd (Serial_Number, Date, Time, Patient_ID, Doctor_ID, Case_Type) VALUES ( %s, %s, %s, %s, %s, %s)", (Serial_Number, Date, Time, patient_id, Doctor_ID, Case_Type))
            
            
            connection.commit()
            # app.logger.info('Patient added successfully: Name - %s %s %s, DOB - %s, Address - %s %s %s, %s, %s, Gender - %s, Allergies - %s, Email - %s',
                            # first_name, middle_name, last_name, dob, street_number, street_name, apartment_number, city, pincode, gender, allergies, email)
        except Exception as e:
            app.logger.error('Error adding patient to database: %s', str(e))
        finally:
            connection.close()

        return redirect(url_for('pat_opd'))

@app.route('/add_hospital', methods=['POST'])
def add_hospital():
    if request.method == 'POST':
        license_number = request.form['license_number']
        name = request.form['name']
        phone_number = request.form['phone_number']
        street_number = request.form['street_number']
        street_name = request.form['street_name']
        apartment_number = request.form.get('apartment_number', '')  # Apartment number is optional
        city = request.form['city']
        pincode = request.form['pincode']

        contact_numbers = [number.strip() for number in phone_number.split(",")]

        # Check if pincode is within the specified range
        if not (100000 <= int(pincode) <= 999999):
            return "Error: Pincode should be between 100000 and 999999"

        connection = get_mysql_connection()
        cur = connection.cursor()
        try:
            cur.execute("INSERT INTO hospital (License_Number, Name, Street_Number, Street_Name, Apartment_Number, City, Pincode) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (license_number, name, street_number, street_name, apartment_number, city, pincode))
            for number in contact_numbers:
                cur.execute("INSERT INTO Hospital_Contact (License_Number, Phone_Number) VALUES (%s, %s)", (license_number, number))
            
            connection.commit()
            app.logger.info('Patient added successfully: License_Number - %s, Name - %s, Address - %s %s %s, %s, %s',
                            license_number, name, street_number, street_name, apartment_number, city, pincode)
            # Inserting patient contact numbers into the Hospital_Contact table
            
        except Exception as e:
            app.logger.error('Error adding patient to database: %s', str(e))
            return "Error adding patient to database: " + str(e)
        finally:
            connection.close()

        return redirect(url_for('hospital'))

@app.route('/add_supplier', methods=['POST'])
def add_supplier():
    if request.method == 'POST':
        Supplier_ID = request.form['Supplier_ID']
        Agency_Name = request.form['Agency_Name']
        Street_Number = request.form['Street_Number']
        Street_Name = request.form['Street_Name']
        Apartment_Number = request.form['Apartment_Number']
        City = request.form['City']
        Pincode = request.form['Pincode']
        Account_Number = request.form['Account_Number']
        Bank_Name = request.form['Bank_Name']
        IFSC_Code = request.form['IFSC_Code']
        Branch = request.form['Branch']
        Phone_Number = request.form['phone_number']

        contact_numbers = [number.strip() for number in Phone_Number.split(",")]

        connection = get_mysql_connection()
        cur = connection.cursor()
        try:
            cur.execute("INSERT INTO supplier (Supplier_ID, Agency_Name, Street_Number, Street_Name, Apartment_Number, City, Pincode, Account_Number, Bank_Name, IFSC_Code, Branch) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (Supplier_ID, Agency_Name, Street_Number, Street_Name, Apartment_Number, City, Pincode, Account_Number, Bank_Name, IFSC_Code, Branch))
            for number in contact_numbers:
                cur.execute("INSERT INTO Supplier_Contact (Supplier_ID, Contact_Number) VALUES (%s, %s)", (Supplier_ID, number))
            
            connection.commit()
            app.logger.info('Supplier added successfully: Supplier_ID - %s, Agency_Name - %s', Supplier_ID, Agency_Name)
        except Exception as e:
            app.logger.error('Error adding student to database: %s', str(e))
        finally:
            connection.close()
        
        return redirect(url_for('supplier'))


@app.route('/add_pres', methods=['POST'])
def add_pres():
    if request.method == 'POST':
        prescription_id = request.form['prescriptionID']
        patient_id = request.form['patientID']
        Doctor_ID = request.form['doctorID']
        Serial_Number = request.form['SerialNo']
        item_id = request.form['itemID']
        date = request.form['date']
        diagnosis = request.form['diagnosis']
        remarks =  request.form['remarks']
        is_emergency = request.form.get('emergency') == 'yes'
        is_test = request.form.get('test') == 'yes'

        if is_test:
            test_name = request.form['Test_Name']
            tests = [number.strip() for number in test_name.split(",")]

        else:
            test_name = None


        if is_emergency:
            license_number = request.form['licenseNumber']
            disease = request.form['disease']
            emergency_date = request.form['emergencyDate']
            time = request.form['time']
            
        else:
            license_number = None
            disease = None
            emergency_date = None
            time = None

        items = [number.strip() for number in item_id.split(",")]
        connection = get_mysql_connection()
        cur = connection.cursor()
        try:
            cur.execute("INSERT INTO prescription (Prescription_ID, Patient_ID, Date, Diagnosis,remarks) VALUES (%s, %s, %s, %s,%s)",
                        (prescription_id, patient_id, date, diagnosis,remarks))
            cur.execute("INSERT INTO appointment (Prescription_ID, Serial_Number,Date) VALUES (%s, %s, %s)",
                        (prescription_id, Serial_Number,date))

            for number in items:
                cur.execute("INSERT INTO medication (prescription_id, item_id) VALUES (%s, %s)", (prescription_id, number))
            
            cur.execute("INSERT INTO prescribed_to (Patient_ID,prescription_id) VALUES (%s,%s)",
                            (patient_id,prescription_id))
            cur.execute("INSERT INTO prescribes (prescription_id, doctor_id) VALUES (%s, %s)", (prescription_id, Doctor_ID))

            if test_name!=None:
                for number in tests:
                    cur.execute("INSERT INTO Med_report (prescription_id, test_type, result) VALUES (%s, %s,%s)", (prescription_id, number, 'Pending'))
            

            if license_number!=None:
                cur.execute("INSERT INTO emergency (Patient_ID,License_Number, Disease, Date, Time) VALUES (%s,%s, %s, %s, %s)",
                            (patient_id,license_number, disease, emergency_date, time))
                cur.execute("INSERT INTO Referred_to (Patient_ID, License_Number, Disease, Date, Time) VALUES (%s, %s, %s, %s, %s)", 
                            (patient_id, license_number, disease, emergency_date, time))
                # cur.execute("INSERT INTO urgent (Patient_ID, License_Number, Disease, Date, Time) VALUES (%s, %s, %s, %s, %s)", 
                #             (patient_id, license_number, disease, emergency_date, time))
                cur.execute("INSERT INTO recommendation(Doctor_ID,Patient_ID, License_Number, Disease, Date, Time) VALUES (%s,%s, %s, %s, %s, %s)", 
                            (Doctor_ID, patient_id, license_number, disease, emergency_date, time))

            connection.commit()
            app.logger.info('Emergency added successfully: Prescription_ID - %s, Patient_ID - %s, Date - %s, Diagnosis - %s, License_Number - %s, Disease - %s, Emergency_Date - %s, Time - %s',
                            prescription_id, patient_id, date, diagnosis, license_number, disease, emergency_date, time)
        except Exception as e:
            app.logger.error('Error adding emergency to database: %s', str(e))
        finally:
            connection.close()

        return redirect(url_for('emergency'))


@app.route('/add_bill', methods=['POST'])
def add_billentry():
    if request.method == 'POST':
        Staff_ID = request.form['staffID']
        Ordered_Date = request.form['orderedDate']
        Bill_Number = request.form['billNumber']
        Quantity = request.form['quantity']
        Amount_Paid = request.form['amountPaid']
        Item_ID = request.form['itemId']  # getlist for multiple entries
        Supplier_ID = request.form['supplierId']
        Does_not_have_entry = request.form['entry']
        item_id_new = request.form.getlist('itemIdNew')  # getlist for multiple entries
        Medicine_Name = request.form.getlist('medicineName')  # getlist for multiple entries
        Expiry_Date = request.form.getlist('expiryDate')  # getlist for multiple entries
        stock = request.form.getlist('stock')  # getlist for multiple entries

        items = [number.strip() for number in Item_ID.split(",")]

        app.logger.info('Received POST request to add bill entry...')
        connection = get_mysql_connection()
        cur = connection.cursor()
        try:
            if Does_not_have_entry == 'yes':
                for i in range(len(item_id_new)):
                    cur.execute("INSERT INTO Medicines_equipments (item_id, Medicine_Name, Expiry_Date, stock) VALUES (%s, %s, %s, %s)", (item_id_new[i], Medicine_Name[i], Expiry_Date[i], stock[i]))
            else:
                item_id_new = None  # getlist for multiple entries
                Medicine_Name = None  # getlist for multiple entries
                Expiry_Date = None  # getlist for multiple entries
                stock = None  # getlist for multiple entries

            cur.execute("INSERT INTO purchase_order (Bill_Number, Quantity, Amount_Paid) VALUES (%s, %s, %s)", (Bill_Number, Quantity, Amount_Paid))
            cur.execute("INSERT INTO Ordered_by (Bill_Number, Staff_ID, ordered_date) VALUES (%s, %s, %s)", (Bill_Number, Staff_ID, Ordered_Date))
            
            for i in range(len(items)):
                cur.execute("INSERT INTO supply_transaction (Bill_Number, Supplier_ID, Item_ID) VALUES (%s, %s, %s)", (Bill_Number,Supplier_ID,items[i]))
            
            connection.commit()
            app.logger.info('Bill Entry added successfully...')
        except Exception as e:
            app.logger.error('Error adding bill entry to database: %s', str(e))
        finally:
            connection.close()
    return redirect(url_for('med_purchase'))


@app.route('/add_insurance', methods=['POST'])
def add_insurance():
    if request.method == 'POST':
        Insurance_Number = request.form['Insurance_Number']
        Issue_Date = request.form['Issue_Date']
        Expiry_Date = request.form['Expiry_Date']
        Wallet_Balance = request.form['Wallet_Balance']
        Reimbursement_Status = request.form['Reimbursement_Status']
        Prescription_ID = request.form['Prescription_ID']
        Patient_ID = request.form['Patient_ID']

        
        connection = get_mysql_connection()
        cur = connection.cursor()
        try:
            cur.execute("INSERT INTO insurance (Insurance_Number, Issue_Date, Expiry_Date,Wallet_Balance, Reimbursement_Status) VALUES (%s, %s,%s,%s,%s)", (Insurance_Number, Issue_Date, Expiry_Date,Wallet_Balance, Reimbursement_Status))
            cur.execute("INSERT INTO Claimed_for (Insurance_Number, Prescription_ID) VALUES (%s,%s)", (Insurance_Number, Prescription_ID))
            cur.execute("INSERT INTO Claimed_by (Patient_ID, Insurance_Number) VALUES (%s,%s)", (Patient_ID, Insurance_Number))
            connection.commit()
            app.logger.info('Insurance added successfully: Insurance_Number - %s,Reimbursement_Status - %s', Insurance_Number, Reimbursement_Status)
        except Exception as e:
            app.logger.error('Error adding student to database: %s', str(e))
        finally:
            connection.close()
        
        return redirect(url_for('insurance'))



if __name__ == '__main__':
    app.run(debug=True)
