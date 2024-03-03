![65f4a1dd9c51265f49d0](https://github.com/isaquliyev/holbertonschool-AirBnB_clone/assets/64212177/1f3f0f13-a349-4ca9-aa62-7cefe26aff87)

## AirBnB Clone Console
The AirBnB Clone Console is a command-line interface (CLI) for managing AirBnB objects. It serves as the primary tool for interacting with the application, allowing users to create, retrieve, update, and delete various objects such as users, places, cities, and more.


## Compilation/installation

1. Clone the repository:
git clone `https://github.com/isaquliyev/holbertonschool-AirBnB_clone.git`

2. Navigate to the project directory:
`cd airbnb-clone`

3. Run the console:
`./console.py`

## Requirements
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Your code should use the pycodestyle (version 2.7.*)
- You have to use the unittest module
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`


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
But also in non-interactive mode:

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

![815046647d23428a14ca](https://github.com/isaquliyev/holbertonschool-AirBnB_clone/assets/64212177/573b83b0-b871-4fb4-88b2-943b2039b4db)

## Testing
python3 -m unittest discover tests

## Contributing
Feel free to contribute to the project by submitting bug reports, feature requests, or pull requests. Your contributions are highly appreciated!

## Authors :black_nib:
* **Aytaj Huseynli** <[aytachuseynli](https://github.com/aytachuseynli)>
* **Isa Guliyev** <[isaquliyev](https://github.com/isaquliyev)>


