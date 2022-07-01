# 0x00. AirBnB clone - The console #
<img src="https://user-images.githubusercontent.com/69850751/175876062-f252cc1b-bd44-46b3-9ddb-a7692b2eede4.png" />

## This is a command interpreter to manage AirBnB objects 
### What's a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Requierements
* Python interpreter `python3 version 3.8.5`
* Python code use `pycodestyle (version 2.8.*)`
* Tested on `Ubuntu 20.04 LTS`

## Python Unit Tests
* All your test files should be inside a folder `tests`
* You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* All your test files should be python files (extension: .py)
* All your test files and folders should start by test_

## Execution
Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`

## Usage examples
**Launch the console**
```
$ ./console.py
(hbnb) 
```

**Creating a new object**
```
(hbnh) create
** class name missing **
(hbnb) create User
796d8678-df45-4a62-ba97-082ff116b4fd
```

**Show an object**
```
(hbnb) show User
** instance not found **
(hbnb) show User 796d8678-df45-4a62-ba97-082ff116b4fd
[User] (796d8678-df45-4a62-ba97-082ff116b4fd) {'id': '796d8678-df45-4a62-ba97-082ff116b4fd', 'created_at': datetime.datetime(2022, 7, 1, 13, 36, 48, 407416), 'updated_at': datetime.datetime(2022, 7, 1, 13, 36, 48, 407527)}
```

**Update an object**
```
(hbnb) update
** class name missing **
(hbnb) update User
** instance id missing **
(hbnb) update User 796d8678-df45-4a62-ba97-082ff116b4fd
** attribute name missing **
(hbnb) update User 7b8c7a8b-f45a-4484-b6e2-aaed70cdac61 name Javi
(hbnb) all
["[User] (796d8678-df45-4a62-ba97-082ff116b4fd) {'id': '796d8678-df45-4a62-ba97-082ff116b4fd', 'created_at': datetime.datetime(2022, 7, 1, 13, 40, 8, 489607), 'updated_at': datetime.datetime(2022, 7, 1, 13, 40, 8, 489622)}", "[User] (1fa18511-0fea-4a3c-a424-cea1f8ee01cc) {'id': '1fa18511-0fea-4a3c-a424-cea1f8ee01cc', 'created_at': datetime.datetime(2022, 7, 1, 13, 40, 17, 45444), 'updated_at': datetime.datetime(2022, 7, 1, 13, 40, 17, 45560), 'name': 'Javi'}"]
```

**Destroy an object**
```
(hbnb) destroy
** class name missing **
(hbnb) destroy User
** instance id missing **
(hbnb) destroy User 796d8678-df45-4a62-ba97-082ff116b4fd
(hbnb)
```

**Exit the console**
```
(hbnb) quit
defrancescomartin@LAPTOP-RFLPL88P:~/holbertonschool-AirBnB_clone$
```

## Authors
* Mateo Arbini - [LinkedIn](https://www.linkedin.com/in/mateo-arbini-1493691a8/)
* Martin De Francesco - [LinkedIn](https://www.linkedin.com/in/martin-de-francesco-ivagnes-640a181b3/)