import sqlite3

# Read DB and connect

# create db
db = sqlite3.connect("database.db")

# CREATE TABLES AND FIELDS

# you will create a table called skills that has name of the skill and the progress
# db.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")
# add data - every data is adjusted by the cursor
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")


# INSERTING DATA
cursor.execute("INSERT INTO users(user_id, name) VALUES(1, 'ali')")
cursor.execute("INSERT INTO users(user_id, name) VALUES(2, 'obad')")
cursor.execute("INSERT INTO users(user_id, name) VALUES(3, 'roby')")


# FETCH DATA FROM DB
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()
print(results)


#UPDATE DATA
cursor.execute("UPDATE users SET name = 'eyad' WHERE user_id = 1")

# DELETE DATA
cursor.execute("DELETE FROM users where user_id = 3")


# to save what you did in the db make
db.commit()




# close db
db.close()



def get_all_data():
  try:
    # connecntion to db
    db = sqlite3.connect("database.db")
    # setting up the cursor
    cursor = db.cursor()
    # fetch data from db
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    return results
  except sqlite3.Error as err:
    print(f"cound't connect to DB {err}")
  finally:
    if (db):
      db.close()

print(get_all_data())