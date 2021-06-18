import sqlite3

# Query the database and return all request
def show_all():
    # connect to database
    conn = sqlite3.connect('customer.db')
    # create a cursor
    c = conn.cursor()

    # Create a table 
    # c.execute("CREATE TABLE customer (first_name text,last_name text,email text)") 

    # many_customers = [
    #                   ('john' , 'snow','john@gmail.com'),
    #                   ('joh' , 'sno','joh@gmail.com'),
    #                   ('jo' , 'sn','jo@gmail.com'),
    #               ]
    # c.executemany("INSERT INTO customer VALUES (?,?,?)",many_customers)
    # c.execute("DELETE FROM customer")

    c.execute("SELECT rowid,* FROM customer")
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()

    # close our connection
    conn.close()


#add a new record to the table
def add_one():
    var_F= input("enter your first name:")
    var_L=input("enter your last name:")
    var_email=input("enter your email address:")
    # connect to database
    conn = sqlite3.connect('customer.db')
    # create a cursor
    c = conn.cursor()
    #inserting new records
    c.execute("INSERT INTO customer VALUES (?,?,?)",(var_F,var_L,var_email))
    #commit to save the insertion
    conn.commit()

    # close our connection
    conn.close()

#addmany records at once
def add_many():
    j=1
    while j==1:
        F=str(input('Add more?|Yes or No|:'))
        if F=='yes' or F=='YES' or F=='yES':
            A=str(input('enter FN:'))
            B=str(input('enter LN'))
            C=str(input('enter email:'))
            many=(A,B,C)
            # connect to database
            conn = sqlite3.connect('customer.db')
            # create a cursor
            c = conn.cursor()
            #inserting new records
            c.executemany("INSERT INTO customer VALUES (?,?,?)",(many,))
            #commit to save the insertion
            conn.commit()
            # close our connection
            conn.close()
        else:
            j+=1
            break

#delete a record to the table
def delete_one(Rid):
    # delete_this=(Fd,Ld,Ed)
    # connect to database
    conn = sqlite3.connect('customer.db')
    # create a cursor
    c = conn.cursor()
    # first_name=(?) AND last_name=(?) AND email=(?) OR 
    c.execute("DELETE FROM customer WHERE rowid=? ",(Rid,))
    conn.commit()
    conn.close()

def where_record(Fn,Ln,En):
    # connect to database
    if Fn=="" and Ln=="" and En =="":
        print("Type Something")
    else:
        conn = sqlite3.connect('customer.db')
    # create a cursor
        c = conn.cursor()
        c.execute("SELECT rowid, * FROM customer WHERE first_name LIKE (?) OR last_name LIKE (?) OR email LIKE (?)",(Fn,Ln,En,))

        items=c.fetchall()

        for item in items:
            print("Your Search Result:",item)
        conn.commit()

    # close our connection
        conn.close()
    