# Creates a schema account_database and table accounts in SQL, if these do not already exist
# Updates table accounts by allowing users to put usernames and passwords into a GUI

import tkinter as tk # GUI
import pymysql # SQL


def main():
    # checks if the table has already been created
    # if the table has not been created, creates table
    # if the table has been created, does nothing
    must_check_table = True

    def create_table(cur):
        # create the database if it doesn't exist
        cur.execute('create database if not exists account_database;')
        # create this table in this database
        cur.execute('create table if not exists `account_database`.`accounts`(id int auto_increment,'
                    'username varchar(32),userpassword varchar(32),primary key (id));')
        
        nonlocal must_check_table
        must_check_table = False

    def enter_data():
        connection = pymysql.connect(
            host='127.0.0.1',
            # Enter the username here.
            user='',
            # Enter the password here.
            password=""
        )

        assert connection.user != '', "Please enter the username."
        assert connection.password != '', "Please enter the password."

        cursor = connection.cursor()

        # Remember: every SQL query must have its own execute

        if must_check_table:
            create_table(cursor)

        # gets data from username
        username_string = username_entry_box.get("1.0", "end-1c")
        # gets data from password
        password_string = password_entry_box.get("1.0", "end-1c")

        # these characters have to be replaced or else SQL strings will get confused
        replace_chars = {'\\': '\\\\',
                         '\n': '\\n',
                         '\t': '\\t',
                         "'": "\\'",
                         '"': '\\"'
                         }

        cursor.execute('use account_database;')
        cursor.execute(f'insert into `account_database`.`accounts`(username, userpassword) values'
                       f'(\'{username_string}\',\'{password_string}\');')
        cursor.execute('select * from accounts')

        connection.commit()

        rows = cursor.fetchall()

        for row in rows:
            print(row)

        print('Rows should have been printed.')
        connection.close()

    # initialize tkinter frame
    root = tk.Tk()
    window = tk.Frame(root)
    window.pack()

    # Notes to Self:
    # say height/width in instantiation
    # use config to extend instantiation
    # say row/column in grid

    # background of entry box
    tk.Label(window).grid(row=0, column=0, rowspan=3)
    tk.Label(window).grid(row=0,column=1,columnspan=4)
    tk.Label(window).grid(row=0, column=4, rowspan=3)

    # username
    tk.Label(window, text="Username").grid(row=1, column=1)
    username_entry_box = tk.Text(window, height=1, width=20)
    username_entry_box.grid(row=1, column=2, columnspan=2)

    # password
    tk.Label(window, text="Password").grid(row=2, column=1)
    password_entry_box = tk.Text(window, height=1, width=20)
    password_entry_box.grid(row=2, column=2, columnspan=2)

    set_input_button = tk.Button(window, text="Enter", width=8, command=enter_data)
    set_input_button.grid(row=3, column=3)

    root.mainloop()


if __name__ == '__main__':
    main()
