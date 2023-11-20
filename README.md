# Where to Go
Interactive map with points of interest in Moscow.

See project in action [here](https://mrdave.pythonanywhere.com/)

## How to install
Download the project to your local machine.

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```commandline
pip install -r requirements.txt
```

Using virtual environment [virtualenv/venv](https://docs.python.org/3/library/venv.html) is recommended for project isolation.

Create SQLite database
```commandline
python manage.py migrate
```

Start a dev server
```commandline
python manage.py runserver
```

### env variables

To configure those settings, create a `.env` file in the root folder of the project and put in there the following:

- `SECRET_KEY` - database's security key
- `DEBUG` - True/False. If not set, defaults to True
- `ALLOWED_HOSTS` - [see Django docs](https://docs.djangoproject.com/en/4.2/ref/settings/#allowed-hosts)

## How to use
Open webpage in your browser. If using dev server it will be available at `localhost:8000`.

![index page view](https://i.imgur.com/st1Ehp3.png)

From here you can browse locations with additional info available by clicking on map markers.

Use Django Admin site to add or edit locations
![Django Admin site](https://i.imgur.com/dfaEazm.png)
Create a superuser account:
```commandline
python manage.py createsuperuser
```
Go to `localhost:8000/admin`. Log in and navigate to Places. From there you can add new places, edit their info and attach images.

Alternatively, if you have valid data in JSON format, it can be added to the database using `load_place command`. Several links can be used at once when separated with a space.
```commandline
python manage.py load_place http://file/address.json

python manage.py load_place link1 link2 link3
```


How the data should look:
```json
{
    "title": "Title",
    "imgs": [
        "link1.jpg",
        "link2.jpg"
    ],
    "description_short": "Short description",
    "description_long": "<p>Longer description.</p>",
    "coordinates": {
        "lng": 12.345678,
        "lat": 34.567890
    }
}
```
## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).  
Demo data was taken from [KudaGo](https://kudago.com).