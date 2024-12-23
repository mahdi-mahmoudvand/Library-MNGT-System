insert_query_table_books = """INSERT INTO Books(title , author , published_year) VALUES(?,?,?)"""
insert_query_table_members = """INSERT INTO Members(name , join_date) VALUES(?,?)"""
insert_query_table_loans = """INSERT INTO Loans(book_id , member_id , loan_date , give_back_date) VALUES(?,?,?,?,?)"""
insert_query_table_admins = """INSERT INTO admins(username , password) VALUES(?,?)"""

update_query_table_books = """UPDATE Books SET (?) = (?) WHERE (?) , (?)"""
update_query_table_members = """UPDATE Members SET (?) = (?) WHERE (?) , (?)"""
update_query_table_loans = """UPDATE Loans SET (?) = (?) WHERE (?) , (?)"""
update_query_table_admins = """UPDATE admins SET (?) = (?) WHERE (?) , (?)"""