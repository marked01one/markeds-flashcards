<div align="center">
  <h1>Marked's Flashcards</h1>

  A full-stack Django-based web app that will help you ace your next test!
</div>

<h2 align="center">Getting Started</h2>

All files within this repository are necessary to run both the server-side and client-side aspects of the server.
In addition, you will also need to download:
<ul>
  <li>
    <a href="https://www.python.org/downloads/">Python</a> (3.10 or above)
  </li>
  <li>
    <a href="https://www.djangoproject.com/download/">Django</a> (check the link for more details)
  </li>
</ul>

<h2 align="center">Running the App</h2>

To run the app, locate the program's directory (where the program folder was located). Mine looked like this, but of course yours will look different:
```
C:\Documents\Flashcard-App
```
Open PowerShell and change your current directory to the program's directory:
```
cd C:\Documents\Flashcard-App
```
<h3>1. Setting up a virtual environment</h3>
<ul>
  <li>Activate a virtual environment to host your application by typing: <code>./venv/Scripts/Activate.ps1</code></li>
  <li>You should get something like this:</li>
</ul>

```
(venv) PS <C:\Documents\Flashcard-App> 
```

<h3>2. Activate the application</h3>
<ul>
  <li>Activate the server-side of the application by typing: <code>python manage.py runserver</code></li>
  <li>After waiting a for a few seconds, you should receive:</li>
</ul>

```
System check identified no issues (0 silenced).
October 22, 2022 - 23:48:41
Django version 4.0.4, using settings 'flashcard.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK. 
```

<ul>
  <li>Open the HTTP link in your browser of choice and voila! You've done it!</li>
</ul>



