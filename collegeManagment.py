import mysql.connector as mysql

# Connect to the MySQL server
db = mysql.connect(host="localhost", user="root", password="")

# Create the 'college' database if it doesn't exist
try:
    command_handler = db.cursor()
    command_handler.execute("CREATE DATABASE IF NOT EXISTS college")
    print("Database 'college' has been created or already exists.")
except Exception as e:
    print("Failed to create or access the 'college' database.")
    print(e)

# Close the connection to the MySQL server
db.close()

# Connect to the 'college' database
db = mysql.connect(host="localhost", user="root", password="", database="college")
command_handler = db.cursor(buffered=True)

def admin_session():
    while 1:
        print("")
        print("Admin Menu")
        print("1. Register new Student")
        print("2. Register new Teacher")
        print("3. Delete Existing Student")
        print("4. Delete Existing Teacher")
        print("5. Logout")

        user_option = input("Option : ")
        if user_option == "1":
            print("")
            print("Register New Student")
            username = input("Student username : ")
            password = input("Student password : ")
            query_vals = (username, password)
            command_handler.execute("INSERT INTO users (username, password, privilege) VALUES (%s, %s, 'student')", query_vals)
            db.commit()
            print(username + " has been registered as a student")
        
        elif user_option == "2":
            print("")
            print("Register New Teacher")
            username = input("Teacher username : ")
            password = input("Teacher password : ")
            query_vals = (username, password)
            command_handler.execute("INSERT INTO users (username, password, privilege) VALUES (%s, %s, 'teacher')", query_vals)
            db.commit()
            print(username + " has been registered as a teacher")
    
        elif user_option == "3":
            print("")
            print("Delete Existing Student Account")
            username = input("Student username : ")
            query_vals = (username, "student")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " has been deleted")

        elif user_option == "4":
            print("")
            print("Delete Existing Teacher Account")
            username = input("Teacher username : ")
            query_vals = (username, "teacher")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " has been deleted")

        elif user_option == "5":
            break
        else:
            print("No valid option selected")

def auth_admin():
    print("")
    print("Admin Login")
    print("")
    username = input("Username : ")
    password = input("Password : ")
    if username == "admin":
        if password == "password":
            admin_session()
        else:
            print("Incorrect password !")
    else:
        print("Login details not recognized") 

def main():
    while 1:
        print("Welcome to the college system")
        print("")
        print("1. Login as student")
        print("2. Login as teacher")
        print("3. Login as admin")

        user_option = input("Option : ")
        if user_option == "1":
            print("Student login")
        elif user_option == "2":
            print("Teacher login")
        elif user_option == "3":
            auth_admin()
        else:
            print("No valid option was selected")

if __name__ == "__main__":
    main()
