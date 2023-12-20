fieldsList = {'Wheel Size:':['16" or less','20"','24"','26"','27.5" / 650B','29"','650C','700C','Unknown'],'Frame Size:':['XS','S','M','L','XL'],'Material:':['Aluminium','Carbon Fiber','Chromoly','Steel','Titanium','Unknown'],
              'Rear Travel:':['0 mm (Hardtail)','80 mm','100 mm','110 mm','111 mm','120 mm','130 mm','135 mm','140 mm','143 mm','145 mm','150 mm','153 mm','155 mm','160 mm','170 mm','180 mm','190 mm','200 mm','215 mm','216 mm','254 mm','255 mm','Unknown'],
              'Fork Travel:':['0 mm (Rigid)','40 mm','60 mm','80 mm','90 mm','95 mm','100 mm','110 mm','120 mm','130 mm','140 mm','150 mm','160 mm','170 mm','175 mm','180 mm','190 mm','200 mm','203 mm','208 mm','Unknown'],
              'Front Axle:':['100 Lefty','100 QR','12 x 100 TA','15 x 100 TA','15 x 110 TA Boost','15 x 150 TA','20 x 110 TA','Unknown / Not Present'],'Rear Axle:':['10 x 130 QR','10 x 135 QR','10 x 141 QR','10 x 170 QR','12 x 135 TA','12 x 142 TA','12 x 148 TA','12 x 150 TA','12 x 157 TA','12 x 177 TA','Unknown / Not Present'],
              'Seatpost Diameter:':['25.4','26.2','26.8','27.2','30.0','30.9','31.6','34.9','Unknown'
],'Seatpost Travel:':['35 mm','65 mm','80 mm','85 mm','100 mm','110 mm','120 mm','125 mm','130 mm','140 mm','150 mm','160 mm','170 mm','175 mm','180 mm','185 mm','200 mm','210 mm','220 mm','Unknown'
],'Shock Eye to Eye:':['6.5"','7.25"','7.5"','7.875"','8.5"','8.75"','9.5"','10.5"','165 mm','185 mm','190 mm','200 mm','205 mm','210 mm','215 mm','216 mm','222 mm','225 mm','230 mm','240 mm','250 mm','Unknown'
],'Shock Stroke:':['1.5"','1.75"','1.875"','2.0"','2.25"','2.5"','2.75"','3.0"','3.5"','45 mm','50 mm','51 mm','52.5 mm','55 mm','57 mm','57.5 mm','60 mm','62.5 mm','63 mm','65 mm','70 mm','75 mm','76 mm','Unknown'
],'Shock Spring Rate:(lbs)':['200','225','250','275','300','325','350','375','400','425','450','475','500','525','550','575','600','650','700','Unknown']

}




pinkikeMegaData = {'All Mountain/Enduro Frames': ['Wheel Size:','Fork Travel:', 'Frame Size:', 'Material:', 'Rear Travel:'],
     'DJ/Street/Park Frames': ['Wheel Size:', 'Frame Size:', 'Material:'], 'XC Frames': ['Wheel Size:', 'Frame Size:', 'Material:', 'Rear Travel:'], 'Vintage Frames': [], 
     'Fork Parts / Springs': [], 'Single Crown Forks': ['Wheel Size:', 'Front Axle:','Fork Travel:'], 'Dual Crown Forks': ['Wheel Size:', 'Front Axle:','Fork Travel:'], 
     'Rear Shocks ( Air )': ['Shock Eye to Eye:', 'Shock Stroke:'], 'Rear Shocks ( Coil )': ['Shock Eye to Eye:', 'Shock Stroke:', 'Shock Spring Rate:(lbs)'], 'Rear Shock Parts': [],
    'Rear Shock Springs': ['Material:', 'Shock Spring Rate:(lbs)'], 'Brakes': [], 'Grips': [], 'Handle Bars ( 31.8 mm )': ['Material:'], 'Handle Bars ( 35 mm )': ['Material:'],
 'Headsets': [], 'Pedals ( Clipless)': [], 'Pedals ( Flat )': [], 'Saddles': [], 'Seatposts ( Dropper )': ['Seatpost Diameter:','Seatpost Travel:'], 
 'Seatposts ( Fixed )': ['Seatpost Diameter:'], 'Seatpost Parts': [], 'Stems': [], 'Bottom Brackets': [], 'Cassettes': [], 'Chains': [], 'Chain Guides': [], 'Chain Rings': [], 
 'Cranks': ['Material:'], 'Drivetrain Groupset': [], 'Hubs': ['Front Axle:', 'Rear Axle:'], 'Shifters/Derailleurs': [], 'Spokes': [], 'Tires': ['Wheel Size:'], 
 'Wheels ( with Hubs )': ['Wheel Size:', 'Material:', 'Front Axle:', 'Rear Axle:'], 'Wheels ( Rims only )': ['Wheel Size:'],
   'E-Bikes MTB': ['Wheel Size:', 'Frame Size:', 'Material:'], 'E-Bikes Urban/Commuter': ['Wheel Size:', 'Frame Size:'], 'E-Bikes Road/Gravel': ['Wheel Size:', 'Frame Size:'],
 'E-Bike Parts': [], 'Fat Bikes': ['Wheel Size:', 'Frame Size:'], 'Fat Bike Frames': ['Wheel Size:', 'Frame Size:'], 'Fat Bike Parts': [], 'BMX Bikes': ['Wheel Size:', 'Frame Size:'],
 'BMX Frames': ['Wheel Size:', 'Frame Size:'], 'BMX Forks/Headsets/Pegs': [], 'BMX Wheels/Rims/Tires': ['Wheel Size:'], 'BMX Seat/Post/Clamps': [], 'BMX Bars/Grips/Stems': [],
 'BMX Cranks/BBs/Chains': [], 'BMX Brakes': [], 'BMX Hubs': [], 'BMX Pedals': [], 'BMX Parts': [], 'Gravel/CX Bikes': ['Wheel Size:', 'Frame Size:', 'Material:'],
 'Gravel/CX Frames': ['Wheel Size:', 'Frame Size:', 'Material:'], 'Gravel/CX Parts': [], 'Road Bikes': ['Wheel Size:', 'Frame Size:', 'Material:'], 
'Road Frames': ['Wheel Size:', 'Frame Size:', 'Material:'], 'Road Parts': [], 'Trials Bikes': ['Wheel Size:', 'Frame Size:'], 'Trials Frames': ['Wheel Size:', 'Frame Size:'],
 'Trials Parts': [], 'Trucks/Cars': [], 'Ski': [], 'Snowboard': [], 'Skateboard': [], 'MX Bikes/Quads': [], 'Armour/Pads': [], 'Backpacks': [], 'Bike Bags': [], 'Bike Racks': [],
   'Clothes': [], 'Goggles/Shades': [], 'GPS/Speedometers': [], 'Helmets': [], 'Computers/Tech gear': [], 'Video/Photo gear': [], 'IPODs/Music Players': [], 'Music/Guitar/Amps': [],
     'Paintball': [], 'Other': [], 'Wanted Ads': [], 'Trades': [], 'Stolen Bikes/Parts': [], 'Lights': [], 'Shoes': [], 'Tools/Bike Stands': [], 'Trainers / Rollers': [], 
     'DH Frames': ['Wheel Size:', 'Frame Size:', 'Material:', 'Rear Travel:']}


'''CREATE TABLE bike_part
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                price REAL NOT NULL,
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
                photo_filenames TEXT,
                fb_link TEXT,
                craigslist_link TEXT,
                kijiji_link TEXT,
                ebay_link TEXT,
                pinkbike_link TEXT,
                status TEXT,
                date_posted TEXT,
                FOREIGN KEY (user_id) REFERENCES customers(id))''')

'''

<option value="Computers/Tech gear">Computers/Tech gear</option>
<option value="Video/Photo gear">Video/Photo gear</option>
<option value="IPODs/Music Players">IPODs/Music Players</option>
<option value="Music/Guitar/Amps">Music/Guitar/Amps</option>
<option value="Paintball">Paintball</option>
<option value="Lights">Lights</option>
<option value="Shoes">Shoes</option>
<option value="Wanted Ads">Wanted Ads</option>
<option value="Trades">Trades</option>
<option value="Trucks/Cars">Trucks/Cars</option>
<option value="Ski">Ski</option>
<option value="Snowboard">Snowboard</option>
<option value="Skateboard">Skateboard</option>
<option value="MX Bikes/Quads">MX Bikes/Quads</option>
<option value="Armour/Pads">Armour/Pads</option>
<option value="Backpacks">Backpacks</option>

<option value="Clothes">Clothes</option>
<option value="Helmets">Helmets</option>

'''