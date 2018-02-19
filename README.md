## myFlaskApp Project V1.0

### myFlaskApp

---

### To run the application

[Project Repo](https://github.com/markchen555/myFlaskApp)

Fork a copy from github or download the repository on your computer, unzip it and launch the terminal at the root directory of the folder.

1. Run `npm install` to install all dependency to your local machine.
2. Run `python app.py` to start your server.
3. Open another tab at your terminal.
4. Run `localhost:5000` on your browser to begin using our app.

---

### MySQL instruction

1. Run `mysqld` to start the MySQL database.
2. Run `mysql -u root` to access MySQL or `mysql -u root -p` if you have password.

MySQL query:
- `SHOW DATABASES;` (show dabases)
- `CREATE DATABASE database_name` (create new database)
- `USE database_name` (switch to database)
- `CREATE TABLE users(id INT(11) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100), username VARCHAR(30), password VARCHAR(100), register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);` (creating table with fields)
- `SHOW TABLES;` (show tables)
- `DESCRIBE databaes_name` (checking database fields)

---

### myFlaskApp V1.0 Info

The myFlaskApp uses python and flask for backend.

---

### Reference

- [Python3](https://www.python.org/)
- [Flask] ()
- [MySQL-Python] ()
- [Bootstrap4] ()
- [libMySQL] ()
- [Mysqlclient] ()
- [flask-mysqldb] ()
- [flask-wtf] ()
- [passlib] ()
- [Flask Snippets Decorators] (http://flask.pocoo.org/snippets/category/decorators/)

---

### License

The project is licensed under the [MIT license](license.txt).