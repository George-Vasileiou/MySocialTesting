import sqlite3 as sql
import tkinter as tk


username = "boss"
password = "1234"
con = sql.connect("database.db")
cur = con.cursor()
statement = f"SELECT username from users WHERE username='{username}' AND Password = '{password}';"

def login():
 cur.execute(statement)
 if not cur.fetchone():  # An empty result evaluates to False.
     print("Login failed")
 else:
     print("Welcome")


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
e1 = tk.Entry()
e2 = tk.Entry()

slogan = tk.Button(frame,
                   text="Log in",
                   command=login)
slogan.pack(side=tk.LEFT)

root.mainloop()
