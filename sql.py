import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    database="db_prac",
    user = "root",
    password = "19176012@Ja"
)

if connection.is_connected():
	db_Info = connection.get_server_info()
	print("Connected to MYSQL Server version ",db_Info)
	cursor = connection.cursor()
	cursor.execute("select database();")
	record = cursor.fetchone()
	print("You are connected to the database: ",record)

def print_table():
	cursor.execute("select * from demo;")
	for i in cursor:
		print(i)
	
def create():
	print ("creating table demo")
	cursor.execute("create table if not exists demo(id int primary key, name varchar(24));")
	print("Showing tables: ")
	cursor.execute("show tables;")
	for i in cursor:
		print(i)

def insert():
	print("Inserting 4 values in demo")
	cursor.execute("insert into demo values(101,'abc'),(102,'def'),(103,'ghi'),(104,'jkl');")
	connection.commit();

def update():
	print("Updating id 104 to 105")
	cursor.execute("update demo set id = 105 where id = 104;")
	connection.commit();
	
def delete():
	print("Deleting entry with id = 105")
	cursor.execute("delete from demo where id = 105;")
	connection.commit();
	
def main():
	while(True):
		print("-----------------------------------------------")
		print("1. Create")
		print("2. Insert")
		print("3. Update")
		print("4. Delete")
		print("5. Print Table")
		print("6. Exit")
		ch = int(input("Enter choice: "))
		if(ch == 1):
			create()
		if(ch == 2):
			insert()
		if(ch == 3):
			update()
		if(ch == 4):
			delete()
		if(ch == 5):
			print_table()
		if(ch == 6):
			break;
		print("-----------------------------------------------")

main()