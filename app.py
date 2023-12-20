from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import hashlib
from werkzeug.utils import secure_filename
import os
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = "secret_key"
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

app.config['UPLOAD_FOLDER'] = 'static/images'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




# Customer Registration Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get user input
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        phone_number = request.form['phone_number']
        location = request.form['location']
        username = request.form['username']
        account_type = 'Customer'
        business_name = request.form['business_name']
        business_address = request.form['business_address']
        business_website = request.form['business_website']

        # Hash password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Check if email or username already exists
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM customers WHERE email=? OR username=?", (email, username))
        result = c.fetchone()
        if result:
            return "Email or username already exists"
        else:
            # Insert user input into database
            c.execute("INSERT INTO customers (first_name, last_name, email, password, phone_number, location, username, account_type, business_name, business_address, business_website) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (first_name, last_name, email, hashed_password, phone_number, location, username, account_type, business_name, business_address, business_website))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))

    return render_template('register.html')



# Login Page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get user input
        email_or_username = request.form['email_or_username']
        password = request.form['password']

        # Hash password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Check if user exists
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM customers WHERE (email=? OR username=?) AND password=?", (email_or_username, email_or_username, hashed_password))
        result = c.fetchone()
        if result:
            session['user_id'] = result[0]
            session['username'] = result[9]
            if result[3] == 'Customer':
                return redirect(url_for('poster'))
            elif result[3] == 'Worker':
                return redirect(url_for('listings'))
        else:
            return "Invalid email/username or password"

    return render_template('login.html')




# Customer Settings
@app.route('/settings')
def settings():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # Get user information from database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers WHERE id=?", (session['user_id'],))
    result = c.fetchone()
    conn.close()

    return render_template('settings.html', result=result)




# Poster Page
@app.route('/poster', methods=['GET', 'POST'])
def poster():
    fieldsList = {'Wheel Size:':['16" or less','20"','24"','26"','27.5" / 650B','29"','650C','700C','Unknown'],'Frame Size:':['XS','S','M','L','XL'],'Material:':['Aluminium','Carbon Fiber','Chromoly','Steel','Titanium','Unknown'],
              'Rear Travel:':['0 mm (Hardtail)','80 mm','100 mm','110 mm','111 mm','120 mm','130 mm','135 mm','140 mm','143 mm','145 mm','150 mm','153 mm','155 mm','160 mm','170 mm','180 mm','190 mm','200 mm','215 mm','216 mm','254 mm','255 mm','Unknown'],
              'Fork Travel:':['0 mm (Rigid)','40 mm','60 mm','80 mm','90 mm','95 mm','100 mm','110 mm','120 mm','130 mm','140 mm','150 mm','160 mm','170 mm','175 mm','180 mm','190 mm','200 mm','203 mm','208 mm','Unknown'],
              'Front Axle:':['100 Lefty','100 QR','12 x 100 TA','15 x 100 TA','15 x 110 TA Boost','15 x 150 TA','20 x 110 TA','Unknown / Not Present'],'Rear Axle:':['10 x 130 QR','10 x 135 QR','10 x 141 QR','10 x 170 QR','12 x 135 TA','12 x 142 TA','12 x 148 TA','12 x 150 TA','12 x 157 TA','12 x 177 TA','Unknown / Not Present'],
              'Seatpost Diameter:':['25.4','26.2','26.8','27.2','30.0','30.9','31.6','34.9','Unknown'
],'Seatpost Travel:':['35 mm','65 mm','80 mm','85 mm','100 mm','110 mm','120 mm','125 mm','130 mm','140 mm','150 mm','160 mm','170 mm','175 mm','180 mm','185 mm','200 mm','210 mm','220 mm','Unknown'
],'Shock Eye to Eye:':['6.5"','7.25"','7.5"','7.875"','8.5"','8.75"','9.5"','10.5"','165 mm','185 mm','190 mm','200 mm','205 mm','210 mm','215 mm','216 mm','222 mm','225 mm','230 mm','240 mm','250 mm','Unknown'
],'Shock Stroke:':['1.5"','1.75"','1.875"','2.0"','2.25"','2.5"','2.75"','3.0"','3.5"','45 mm','50 mm','51 mm','52.5 mm','55 mm','57 mm','57.5 mm','60 mm','62.5 mm','63 mm','65 mm','70 mm','75 mm','76 mm','Unknown'
],'Shock Spring Rate:(lbs)':['200','225','250','275','300','325','350','375','400','425','450','475','500','525','550','575','600','650','700','Unknown']}
    
    
    if 'user_id' not in session:
        return redirect(url_for('login'))

    postType = ''
    if request.method == 'POST':
        postType = request.form['formID']
        print(request.form['formID'])
        title = request.form['title']
        price = request.form['price']
        year = request.form['year']
        condition = request.form['condition']
        description = request.form['description']
        photos = request.files.getlist('photos[]')
        print(str(photos))
        
        if request.form['formID'] == 'bike':
            # Get user input
            bicycle_type = request.form['bicycle_type']
            frame_material = request.form['frame_material']
            frame_size = request.form['frame_size']
            wheel_size = request.form['wheel_size']
            fork_travel = request.form['fork_travel']
            rear_travel = request.form['rear_travel']
            table_type = 'bikes'

        elif request.form['formID'] == 'bike_part':
            # Get user input
                material = request.form['material']
                frame_size = request.form['frame_size']
                wheel_size = request.form['wheel_size']
                fork_travel = request.form['fork_travel']
                rear_travel = request.form['rear_travel']
                front_axle = request.form['front_axle']
                rear_axle = request.form['rear_axle']
                seatpost_diameter = request.form['seatpost_diameter']
                seatpost_travel = request.form['seatpost_travel']
                shock_eye_to_eye = request.form['shock_eye_to_eye']
                shock_stroke = request.form['shock_stroke']
                shock_spring_rate = request.form['shock_spring_rate']
                table_type = 'bike_part'

        date_posted = datetime.now().strftime('%Y/%m/%d')
        status = "Post - Pending"
        # Insert bike information into database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        if str(postType) == 'bike':
            c.execute("INSERT INTO bikes (user_id, title, price, year, bicycle_type, frame_material, frame_size, wheel_size, fork_travel, rear_travel, condition, description, status, date_posted, table_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (session['user_id'], title, price, year, bicycle_type, frame_material, frame_size, wheel_size, fork_travel, rear_travel, condition, description, status, date_posted, table_type))
        elif str(postType) == 'bike_part':
            c.execute("INSERT INTO bike_part (user_id, title, price, year, material, frame_size, wheel_size, fork_travel, rear_travel, front_axle, rear_axle, seatpost_diameter, seatpost_travel, shock_eye_to_eye, shock_stroke, shock_spring_rate, condition, description, status, date_posted, table_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (session['user_id'], title, price, year, material, frame_size, wheel_size, fork_travel, rear_travel, front_axle, rear_axle, seatpost_diameter, seatpost_travel, shock_eye_to_eye, shock_stroke, shock_spring_rate, condition, description, status, date_posted, table_type))     
        conn.commit()

        # Create folder for user if it doesn't exist
        c.execute("SELECT username FROM customers WHERE id=?", (session['user_id'],))
        result = c.fetchone()
        user_folder = os.path.join(app.config['UPLOAD_FOLDER'], result[0])
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)


        # Create folder for bike posting
        if str(postType) == 'bike':
            bike_id = c.lastrowid
            post_folder = os.path.join(user_folder, 'bikes', str(bike_id))
            if not os.path.exists(post_folder):
                os.makedirs(post_folder)
    
        elif str(postType) == 'bike_part':
            bike_part_id = c.lastrowid
            post_folder = os.path.join(user_folder, 'bike_part', str(bike_part_id))
            if not os.path.exists(post_folder):
                os.makedirs(post_folder)

        photo_names = []
        print('POST FOLDER: ' + post_folder)
        for photo in photos:
            if photo and allowed_file(photo.filename):
                photo_name = secure_filename(photo.filename)
                photo_path = os.path.join(post_folder, photo_name)
                photo.save(photo_path)
                photo_names.append(photo_name)

        photo_names_str = ','.join(photo_names)
        if str(postType) == 'bike':
            c.execute("UPDATE bikes SET photo_filenames=? WHERE id=?", (photo_names_str, c.lastrowid))
        elif str(postType) == 'bike_part':
            print('Getting Here')
            c.execute("UPDATE bike_part SET photo_filenames=? WHERE id=?", (photo_names_str, c.lastrowid))
        conn.commit()
        conn.close()
    

    return render_template('poster.html', fieldsList=fieldsList)






# Listings Page
@app.route('/listings', methods=['GET', 'POST'])
def listings():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # Get bike information from database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT bikes.id, bikes.date_posted, bikes.status, bikes.photo_filenames, bikes.table_type, customers.username, bikes.title, bikes.price, bikes.year, bikes.bicycle_type, bikes.frame_material, bikes.frame_size, bikes.wheel_size, bikes.fork_travel, bikes.rear_travel, bikes.condition, bikes.description FROM bikes INNER JOIN customers ON bikes.user_id=customers.id WHERE bikes.user_id=?", (session['user_id'],))
    bike_result = c.fetchall()
    c.execute('SELECT bike_part.id, bike_part.date_posted , bike_part.status, bike_part.photo_filenames, bike_part.table_type, customers.username, bike_part.title, bike_part.price, bike_part.year FROM bike_part INNER JOIN customers ON bike_part.user_id=customers.id WHERE bike_part.user_id=?', (session['user_id'],))
    part_result = c.fetchall()
    conn.close()
    
    temp_result = bike_result + part_result
    sorted_result = sorted(temp_result, key=lambda x: x[1], reverse=True)
    print(sorted_result)
    if not bike_result and not part_result:
        print("No postings found in the database")
    try:
        filePreFix = 'images/' + sorted_result[0][5]
    except Exception as e:
        print(e)
        filePreFix = 'images/'  

    return render_template('listings.html', result=sorted_result, filePrefix=filePreFix)

# Worker Listings Page
@app.route('/worker_listings', methods=['GET', 'POST'])
def worker_listings():
    if 'worker_id' not in session:
        return redirect(url_for('worker_login'))

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT bikes.id, bikes.date_posted, bikes.status, bikes.photo_filenames, bikes.table_type, customers.username, bikes.title, bikes.price, bikes.year, bikes.bicycle_type, bikes.frame_material, bikes.frame_size, bikes.wheel_size, bikes.fork_travel, bikes.rear_travel, bikes.condition, bikes.description FROM bikes INNER JOIN customers ON bikes.user_id=customers.id")
    bike_result = c.fetchall()
    c.execute('SELECT bike_part.id, bike_part.date_posted , bike_part.status, bike_part.photo_filenames, bike_part.table_type, customers.username, bike_part.title, bike_part.price, bike_part.year FROM bike_part INNER JOIN customers ON bike_part.user_id=customers.id')
    part_result = c.fetchall()
    conn.close()
    
    temp_result = bike_result + part_result
    sorted_result = sorted(temp_result, key=lambda x: x[1], reverse=True)
    print(sorted_result)
    if not bike_result and not part_result:
        print("No postings found in the database")
    try:
        filePreFix = 'images/' + sorted_result[0][5]
    except Exception as e:
        print(e)
        filePreFix = 'images/'  

    return render_template('worker_listings.html', result=sorted_result, filePrefix=filePreFix)

# Individual Bike Page
@app.route('/listing/<string:listing_type>/<int:listing_id>')
def listing(listing_type, listing_id):
    # Check if user is logged in
    if 'user_id' not in session:
        return redirect(url_for('worker_login'))

    # Get bike information from database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    query = f"SELECT customers.username, {listing_type}.* FROM {listing_type} INNER JOIN customers ON {listing_type}.user_id=customers.id WHERE {listing_type}.id={listing_id}"
    c.execute(query)

    result = c.fetchone()
    conn.close()

    # Check if bike exists and belongs to current user

    if not result or result[2] != session['user_id']:
        return redirect(url_for('listings'))

    filePreFix = 'images/'
    try:
        filePreFix = 'images/'+result[0]+'/'+listing_type+'/'+str(listing_id)+'/'
    except Exception as e:
        print(e)
    
    bikes_titles = {'Bike ID':1, 'Title':3, 'Price':4, 'Year':5, 'Bicycle Type':6, 'Frame Material':7, 'Frame Size':8, 'Wheel Size':9, 'Fork Travel':10, 'Rear Travel':11, 'Condition':12, 'Description':13, 'Status':15, 'Date Posted':16}
    bike_part_titles = {'Bike Part ID':1, 'Title':3, 'Price':4, 'Year':6, 'Material':7, 'Frame Size':8, 'Wheel Size':9, 'Fork Travel':10, 'Rear Travel':11, 'Front Axle':12, 'Rear Axle':13, 'Seatpost Diameter':14, 'Seatpost Travel':15, 'Shock Eye to Eye':16, 'Shock Stroke':17, 'Shock Spring Rate':18, 'Condition':19, 'Description':20, 'Status':27, 'Date Posted':28}
    if listing_type == 'bikes':
        return render_template('listing.html', result=result, filePrefix=filePreFix, listing_titles=bikes_titles)
    elif listing_type == 'bike_part':
        return render_template('listing.html', result=result, filePrefix=filePreFix, listing_titles=bike_part_titles)


# Individual Bike Page
@app.route('/worker_listing/<string:listing_type>/<int:listing_id>', methods=['GET', 'POST'])
def worker_listing(listing_type, listing_id):
    # Check if user is logged in
    if 'worker_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Get user input
        fb_link = request.form['fb_link']
        craigslist_link = request.form['craigslist_link']
        kijiji_link = request.form['kijiji_link']
        ebay_link = request.form['ebay_link']
        pinkbike_link = request.form['pinkbike_link']
        status = request.form['status']

        # Update bike information in database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        query = f"UPDATE {listing_type} SET fb_link=?, craigslist_link=?, kijiji_link=?, ebay_link=?, pinkbike_link=?, status=? WHERE id=?"
        c.execute(query, (fb_link, craigslist_link, kijiji_link, ebay_link, pinkbike_link, status, listing_id))
        conn.commit()
        conn.close()

        return redirect(url_for('worker_listings'))

    # Get bike information from database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    query = f"SELECT customers.username, {listing_type}.* FROM {listing_type} INNER JOIN customers ON {listing_type}.user_id=customers.id WHERE {listing_type}.id={listing_id}"
    c.execute(query)

    result = c.fetchone()
    conn.close()

    # Check if bike exists and belongs to current user
    if 'worker_id' not in session:
        if not result or result[2] != session['user_id']:
            return redirect(url_for('listings'))

    filePreFix = 'images/'
    if result[13]:
        filePreFix = 'images/'+result[0]+'/'+ listing_type+'/'+str(listing_id)+'/'

    bikes_titles = {'Bike ID':1, 'Title':3, 'Price':4, 'Year':5, 'Bicycle Type':6, 'Frame Material':7, 'Frame Size':8, 'Wheel Size':9, 'Fork Travel':10, 'Rear Travel':11, 'Condition':12, 'Description':13, 'Status':15, 'Date Posted':16, 'fb_link':15, 'craigslist_link':16, 'kijiji_link':17, 'ebay_link':18, 'pinkbike_link':19, 'karrot_link':20}
    bike_part_titles = {'Bike Part ID':1, 'Title':3, 'Price':4, 'Year':6, 'Material':7, 'Frame Size':8, 'Wheel Size':9, 'Fork Travel':10, 'Rear Travel':11, 'Front Axle':12, 'Rear Axle':13, 'Seatpost Diameter':14, 'Seatpost Travel':15, 'Shock Eye to Eye':16, 'Shock Stroke':17, 'Shock Spring Rate':18, 'Condition':19, 'Description':20, 'Status':27, 'Date Posted':28, 'fb_link':21, 'craigslist_link':22, 'kijiji_link':23, 'ebay_link':24, 'pinkbike_link':25, 'karrot_link':26}
    if listing_type == 'bikes':
        return render_template('worker_listing.html', result=result, filePrefix=filePreFix, listing_titles=bikes_titles)
    elif listing_type == 'bike_part':
        return render_template('worker_listing.html', result=result, filePrefix=filePreFix, listing_titles=bike_part_titles)


# Worker Login Page
@app.route('/worker_login', methods=['GET', 'POST'])
def worker_login():
    if request.method == 'POST':
        # Get user input
        email = request.form['email']
        password = request.form['password']

        # Check if user exists
        if email == 'sven@analysis.net' and password == 'pickle':
            session['worker_id'] = 3200
            return redirect(url_for('worker_listings'))
        else:
            return "Invalid email or password"

    return render_template('worker_login.html')


# Delete Bike
@app.route('/delete_listing', methods=['POST'])
def delete_bike():
    # Get bike ID from request data
    listing_table_type = request.json['table_type']
    listing_id = request.json['id']
    print("WE GOT HERE")


    # Check if user is logged in
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # Check if bike belongs to current user
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    query = f"SELECT user_id FROM {listing_table_type} WHERE id={listing_id}"
    c.execute(query)
    result = c.fetchone()
    conn.close()

    if not result or result[0] != session['user_id']:
        return "You are not authorized to delete this listing"

    # Update bike status to "Delete - Pending"
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    query = f"UPDATE {listing_table_type} SET status=? WHERE id=?"
    c.execute(query, ("Delete - Pending", listing_id))
    conn.commit()
    conn.close()

    return "Bike status updated to 'Delete - Pending' successfully"




# Logout Page
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)    
