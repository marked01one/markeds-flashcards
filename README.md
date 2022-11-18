<div align="center">

  # Marked's Flashcards

  <img src="static/images/flashcard_site_new.png" width="50%">
  
  _**A full-stack Django-based web app that will help you ace your next test!**_

  <hr width="50%">
  
  ### **Demo Website: [https://markeds-flashcards.up.railway.app](https://markeds-flashcards.up.railway.app)**

  _NOTE: If the website is current down, chances are I have ran out of credits on Railway :(_

  <hr width="50%">

</div>


<h2 align="center">Getting Started</h2>

### 1. Requirements:

Here is all the dependencies for the program, which can be found in `requirements.txt`. Ignore `gunicorn` and `Pillow` since those are for deployment purposes.

```
asgiref==3.5.2
Django==4.0.4
django-jquery==3.1.0
gunicorn==20.1.0
Pillow==9.1.0
sqlparse==0.4.3
tzdata==2022.5
whitenoise==6.2.0
```

In addition, you will also need to download:

* [Python](https://www.python.org/downloads/) (3.10 or more)
* [Django](https://www.djangoproject.com/download/) (check the link for more details)

<h2 align="center">Running the App</h2>

To run the app, locate the program's directory (where the program folder was located). Mine looked like this, but of course yours will look different:
```
C:\Documents\Flashcard-App
```
Open PowerShell and change your current directory to the program's directory:
```
cd C:\Documents\Flashcard-App
```

### 1. Setting up a virtual environment

* Activate a virtual environment to host your application by typing: `./venv/Scripts/Activate.ps1`
* You should get something similar to this:

```
(venv) PS <C:\Documents\Flashcard-App> 
```

### 1. Activate the application

* Activate the server-side of the application by typing: `python manage.py runserver`
* After waiting a for a few seconds, you should receive:

```
System check identified no issues (0 silenced).
October 22, 2022 - 23:48:41
Django version 4.0.4, using settings 'flashcard.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK. 
```

* Open the HTTP link in your browser of choice and voila! You've done it!



