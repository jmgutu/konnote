# Konnote

Konnote is an application that helps you relate all the notes that you take down by tagging each note, and relating it to other notes with similar tags.

## What problem does it solve?

I love to take notes on everything, all the time! When it came time to using those notes, I had to search the different sites and files I had saved my notes on (Assuming that I find all of them, of course). So this tool is what I used to save my notes, then relate all topics e.g best practices, code smells, setup script, documentation, tricks etc.

## Installation

First, clone the repository.


```bash
$ git clone https://github.com/jmgutu/konnote.git
```

Create a virtual environment in a directory of your choosing. Use python 3.7 or python 3.8.


```bash
$ python -m venv <name_of_virtual_env>
```

Activate the virtual environment


```bash
$ source <name_of_virtual_env>/bin/activate
```

The name of the environment should appear on the leftmost of the prompt.

```bash
(<name_of_virtual_env>) $ source <name_of_virtual_env>/bin/activate
```

Navigate into konnote.

```bash
(<name_of_virtual_env>) $ cd konnote
```

Install the requirements into the newly created virtual environment.

```bash
(<name_of_virtual_env>) $ pip install wheel
(<name_of_virtual_env>) $ pip install -r requirements.txt
```

After the packages have been installed, you need migrate.

```bash
(<name_of_virtual_env>) $ python manage.py migrate
```

Once the migrations have been done, create a superuser.

```bash
(<name_of_virtual_env>) $ python manage.py createsuperuser
```

After successful creation of the super user, run the application.

```bash
(<name_of_virtual_env>) $ python manage.py runserver
```

## Entity Relationship
```
    Subject
    └── Level
        └── Chapter
             └── Topic
                  └── Post
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)