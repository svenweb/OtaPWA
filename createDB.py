import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create customers table
c.execute('''CREATE TABLE customers
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                phone_number TEXT NOT NULL,
                location TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                account_type TEXT NOT NULL,
                business_name TEXT,
                business_address TEXT,
                business_website TEXT,
                fb_password TEXT,
                craigslist_password TEXT,
                kijiji_password TEXT,
                ebay_password TEXT,
                pinkbike_password TEXT)''')

# Create bikes table
c.execute('''CREATE TABLE bikes
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                price REAL NOT NULL,
                photo_filenames TEXT,
                year INTEGER NOT NULL,
                bicycle_type TEXT NOT NULL,
                frame_material TEXT NOT NULL,
                frame_size TEXT NOT NULL,
                wheel_size TEXT NOT NULL,
                fork_travel TEXT NOT NULL,
                rear_travel TEXT NOT NULL,
                condition TEXT NOT NULL,
                description TEXT NOT NULL,
                fb_link TEXT,
                craigslist_link TEXT,
                kijiji_link TEXT,
                ebay_link TEXT,
                pinkbike_link TEXT,
                karrot_link TEXT,
                status TEXT,
                date_posted TEXT,
                table_type TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES customers(id))''')


c.execute('''CREATE TABLE bike_part
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                price REAL NOT NULL,
                photo_filenames TEXT,
                year INTEGER,
                material TEXT,
                frame_size TEXT,
                wheel_size TEXT,
                fork_travel TEXT,
                rear_travel TEXT,
                seatpost_diameter TEXT,
                seatpost_travel TEXT,
                shock_eye_to_eye TEXT,
                shock_stroke TEXT,
                shock_spring_rate TEXT,
                front_axle TEXT,
                rear_axle TEXT,
                condition TEXT NOT NULL,
                description TEXT NOT NULL,
                fb_link TEXT,
                craigslist_link TEXT,
                kijiji_link TEXT,
                ebay_link TEXT,
                pinkbike_link TEXT,
                karrot_link TEXT,
                status TEXT,
                date_posted TEXT,
                table_type TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES customers(id))''')


conn.commit()
conn.close()
