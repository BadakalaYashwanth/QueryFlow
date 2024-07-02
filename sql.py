import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect("EMPLOYEESDeails.db")

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Drop the EMPLOYEES table if it already exists
cursor.execute("DROP TABLE IF EXISTS EMPLOYEES")

# Create the EMPLOYEES table

table_info = """

CREATE TABLE EMPLOYEES (
    EMPLOYEE_ID INT PRIMARY KEY,
    FIRST_NAME VARCHAR(50) NOT NULL,
    LAST_NAME VARCHAR(50) NOT NULL,
    EMAIL VARCHAR(100) UNIQUE NOT NULL,
    PHONE_NUMBER VARCHAR(20),
    HIRE_DATE DATE NOT NULL,
    JOB_ID VARCHAR(10) NOT NULL,
    SALARY DECIMAL(8, 2),
    COMMISSION_PCT DECIMAL(2, 2),
    MANAGER_ID INT,
    DEPARTMENT_ID INT,
    DATE_OF_BIRTH DATE,
    ADDRESS VARCHAR(200),
    GENDER CHAR(1),
    NATIONALITY VARCHAR(50)

);
"""
cursor.execute(table_info)  # Execute the SQL command to create the table

# Insert data into the employee  table
cursor.execute('''INSERT INTO EMPLOYEES VALUES(1, 'John', 'Doe', 'john.doe@example.com', '123-456-7890', '2022-01-15', 'DEV01', 60000.00, NULL, 5, 1, '1990-05-21', '123 Main St, Cityville', 'M', 'USA')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(2, 'Jane', 'Smith', 'jane.smith@example.com', '234-567-8901', '2020-03-22', 'QA01', 55000.00, NULL, 5, 2, '1992-07-10', '456 Oak St, Townsville', 'F', 'USA')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(3, 'Alice', 'Johnson', 'alice.johnson@example.com', '345-678-9012', '2019-07-30', 'PM01', 75000.00, NULL, 6, 3, '1988-12-01', '789 Pine St, Villageton', 'F', 'Canada')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(4, 'Bob', 'Lee', 'bob.lee@example.com', '456-789-0123', '2021-06-15', 'DEV02', 65000.00, NULL, 5, 1, '1991-04-17', '101 Maple St, Hamletburg', 'M', 'USA')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(5, 'Charlie', 'Brown', 'charlie.brown@example.com', '567-890-1234', '2018-11-05', 'MGR01', 85000.00, NULL, NULL, 4, '1985-08-25', '202 Birch St, Metropolis', 'M', 'UK')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(6, 'Diana', 'Prince', 'diana.prince@example.com', '678-901-2345', '2021-10-20', 'HR01', 58000.00, NULL, 5, 2, '1989-03-11', '303 Cedar St, Cosmopolis', 'F', 'USA')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(7, 'Eve', 'Taylor', 'eve.taylor@example.com', '789-012-3456', '2022-02-12', 'FIN01', 62000.00, NULL, 6, 5, '1994-11-19', '404 Elm St, Urbanville', 'F', 'Australia')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(8, 'Frank', 'Wright', 'frank.wright@example.com', '890-123-4567', '2020-05-08', 'IT01', 70000.00, NULL, 6, 6, '1987-09-05', '505 Spruce St, Ruston', 'M', 'USA')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(9, 'Grace', 'Hall', 'grace.hall@example.com', '901-234-5678', '2017-08-21', 'DEV03', 68000.00, NULL, 5, 1, '1993-06-25', '606 Fir St, Oldtown', 'F', 'Canada')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(10, 'Henry', 'Adams', 'henry.adams@example.com', '012-345-6789', '2019-11-29', 'QA02', 56000.00, NULL, 6, 2, '1995-01-30', '707 Redwood St, Uptown', 'M', 'USA')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(11, 'Ivy', 'Green', 'ivy.green@example.com', '123-456-7891', '2016-07-13', 'PM02', 77000.00, NULL, 6, 3, '1986-05-14', '808 Juniper St, Midcity', 'F', 'UK')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(12, 'Jack', 'Black', 'jack.black@example.com', '234-567-8902', '2022-03-04', 'DEV04', 69000.00, NULL, 5, 1, '1990-08-11', '909 Willow St, Suburbia', 'M', 'USA')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(13, 'Karen', 'White', 'karen.white@example.com', '345-678-9013', '2018-04-26', 'MGR02', 86000.00, NULL, NULL, 4, '1984-12-06', '1010 Ash St, Rivertown', 'F', 'Canada')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(14, 'Leo', 'King', 'leo.king@example.com', '456-789-0124', '2020-09-15', 'HR02', 59000.00, NULL, 5, 2, '1991-03-03', '1111 Poplar St, Capital City', 'M', 'Australia')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(15, 'Mia', 'Clark', 'mia.clark@example.com', '567-890-1235', '2019-02-18', 'FIN02', 63000.00, NULL, 6, 5, '1992-07-22', '1212 Beech St, Emerald City', 'F', 'USA')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(16, 'Nathan', 'Scott', 'nathan.scott@example.com', '678-901-2346', '2021-12-28', 'IT02', 71000.00, NULL, 6, 6, '1989-10-10', '1313 Magnolia St, Oceanview', 'M', 'Canada')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(17, 'Olivia', 'Baker', 'olivia.baker@example.com', '789-012-3457', '2017-06-07', 'DEV05', 70000.00, NULL, 5, 1, '1993-01-18', '1414 Palm St, Seaview', 'F', 'UK')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(18, 'Peter', 'Morris', 'peter.morris@example.com', '890-123-4568', '2020-11-14', 'QA03', 57000.00, NULL, 6, 2, '1994-02-09', '1515 Cedar St, Hillside', 'M', 'USA')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(19, 'Quinn', 'Wells', 'quinn.wells@example.com', '901-234-5679', '2021-05-22', 'PM03', 78000.00, NULL, 6, 3, '1987-04-06', '1616 Holly St, Lakeside', 'M', 'Australia')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(20, 'Rachel', 'Lopez', 'rachel.lopez@example.com', '012-345-6790', '2016-03-31', 'DEV06', 72000.00, NULL, 5, 1, '1990-09-23', '1717 Alder St, Mountainview', 'F', 'Canada')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(21, 'Sophia', 'Anderson', 'sophia.anderson@example.com', '345-678-9023', '2022-04-10', 'DEV07', 73000.00, NULL, 5, 1, '1988-11-30', '1818 Cherry St, Downtown', 'F', 'USA')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(22, 'Tom', 'Harris', 'tom.harris@example.com', '456-789-0134', '2019-06-24', 'HR03', 60000.00, NULL, 5, 2, '1991-02-14', '1919 Peach St, Suburb', 'M', 'UK')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(23, 'Uma', 'Norris', 'uma.norris@example.com', '567-890-1245', '2020-01-19', 'FIN03', 64000.00, NULL, 6, 5, '1987-12-21', '2020 Plum St, City Center', 'F', 'Canada')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(24, 'Victor', 'Scott', 'victor.scott@example.com', '678-901-2356', '2018-09-17', 'IT03', 72000.00, NULL, 6, 6, '1990-04-12', '2121 Grape St, Metropolitan', 'M', 'Australia')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(25, 'Wendy', 'Brown', 'wendy.brown@example.com', '789-012-3467', '2021-03-05', 'PM04', 79000.00, NULL, 6, 3, '1989-06-15', '2222 Orange St, Rural Area', 'F', 'USA')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(26, 'Xander', 'Green', 'xander.green@example.com', '890-123-4578', '2017-11-10', 'DEV08', 74000.00, NULL, 5, 1, '1992-08-20', '2323 Lemon St, Villagetown', 'M', 'Canada')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(27, 'Yvonne', 'Hall', 'yvonne.hall@example.com', '901-234-5689', '2022-08-22', 'QA04', 58000.00, NULL, 6, 2, '1993-11-04', '2424 Lime St, Urban Area', 'F', 'Australia')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(28, 'Zachary', 'King', 'zachary.king@example.com', '012-345-6791', '2020-10-28', 'DEV09', 75000.00, NULL, 5, 1, '1988-07-19', '2525 Fig St, Hamletburg', 'M', 'USA')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(29, 'Aaron', 'Long', 'aaron.long@example.com', '123-456-7801', '2019-05-15', 'IT04', 69000.00, NULL, 6, 6, '1989-01-27', '2626 Pine St, Township', 'M', 'UK')''')
cursor.execute('''INSERT INTO EMPLOYEES VALUES(30, 'Bella', 'Parker', 'bella.parker@example.com', '234-567-8903', '2021-12-19', 'HR04', 61000.00, NULL, 5, 2, '1990-03-09', '2727 Spruce St, Cityland', 'F', 'Canada')''')



print("The Inserted Records of the STUDENT are:  ")

data = cursor.execute('''Select * From EMPLOYEES''')

for row in data:
    print(row)

# Commit the transaction to save changes
connection.commit()

# Close the connection
connection.close()
