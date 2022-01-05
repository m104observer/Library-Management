import sqlite3

def connect():
    conn=sqlite3.connect("library_management.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS library (id INTEGER PRIMARY KEY, membertype text, reference text, title text, firstname text, lastname text, address1 text, address2 text, zipcode text, mobile text, bookid text, booktitle text, author text, dateborrowed text, duedate text, daysonloan text, returnfine text, dateoverdue text, sellingprice text)")
    conn.commit()
    conn.close()


def insert(membertype, reference, title, firstname, lastname, address1, address2, zipcode, mobile, bookid, booktitle, author, dateborrowed, duedate, daysonloan, returnfine, dateoverdue, sellingprice):
    conn=sqlite3.connect("library_management.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO library VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(membertype, reference, title, firstname, lastname, address1, address2, zipcode, mobile, bookid, booktitle, author, dateborrowed, duedate, daysonloan, returnfine, dateoverdue, sellingprice))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("library_management.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM library")
    rows=cur.fetchall()
    conn.close()
    return rows


def search(membertype="", reference="", title="", firstname="", lastname="", address1="", address2="", zipcode="", mobile="", bookid="", booktitle="", author="", dateborrowed="", duedate="", daysonloan="", returnfine="", dateoverdue="", sellingprice=""):
    conn=sqlite3.connect("library_management.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM library WHERE membertype=? OR reference=? OR title=? OR firstname=? OR lastname=? OR address1=? OR address2=? OR zipcode=? OR mobile=? OR bookid=? OR booktitle=? OR author=? OR dateborrowed=? OR duedate=? OR daysonloan=? OR returnfine=? OR dateoverdue=? OR sellingprice=?", (membertype, reference, title, firstname, lastname, address1, address2, zipcode, mobile, bookid, booktitle, author, dateborrowed, duedate, daysonloan, returnfine, dateoverdue, sellingprice))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("library_management.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM library WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id, membertype, reference, title, firstname, lastname, address1, address2, zipcode, mobile, bookid, booktitle, author, dateborrowed, duedate, daysonloan, returnfine, dateoverdue, sellingprice):
    conn=sqlite3.connect("library_management.db")
    cur=conn.cursor()
    cur.execute("UPDATE library SET membertype=?, reference=?, title=?, firstname=?, lastname=?, address1=?, address2=?, zipcode=?, mobile=?, bookid=?, booktitle=?, author=?, dateborrowed=?, duedate=?, daysonloan=?, returnfine=?, dateoverdue=?, sellingprice=? WHERE id=?", (membertype, reference, title, firstname, lastname, address1, address2, zipcode, mobile, bookid, booktitle, author, dateborrowed, duedate, daysonloan, returnfine, dateoverdue, sellingprice, id))
    conn.commit()
    conn.close()


connect()



