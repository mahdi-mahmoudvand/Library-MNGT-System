import sqlite3 as sql

try:
    with sql.connect("library_db.db") as db_connect:
        db_cursor = db_connect.cursor()
        create_table_books_query = """CREATE TABLE Books( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            published_year INTEGER
        );"""
        db_cursor.execute(create_table_books_query)

        create_table_members_query = """CREATE TABLE Members( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            join_date TEXT
        );"""
        db_cursor.execute(create_table_members_query)

        create_table_loans_query = """CREATE TABLE Loans( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            member_id INTEGER,
            loan_date TEXT , 
            give_back_date TEXT,
            FOREIGN KEY (book_id) REFERENCES Books(id) ON DELETE CASCADE,
            FOREIGN KEY (member_id) REFERENCES Members(id) ON DELETE CASCADE
        );"""
        db_cursor.execute(create_table_loans_query)

        create_table_admins_query = """CREATE TABLE admins( 
            username TEXT PRIMARY KEY,
            password TEXT
        );"""
        db_cursor.execute(create_table_admins_query)

        
except: 
    print("Table alrdy exists")