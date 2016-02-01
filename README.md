Django Adventure
================
(built with Django 1.8)

This Django project allows you to build multiple text adventures by adding games, scenes, and commands to a PostgreSQL database. The player can then navigate through the scenes using commands that they type into an html form. 

The engine1 directory is where the app lives, and its `models.py` file contains a description of all the data (in this case, games, scenes, and commands) in the project. When you navigate to a url by clicking the link in the index page, it calls the "game" view - the engine of the text adventure. Check out the `views.py` file to see exactly how the "game" view works. 

Adding scenes and commands is easy using Django's built-in admin page - just navigate to localhost:8000/admin. So go ahead, make ZORK III. Or make an game about buying milk at the supermarket. Or fiddle with the /static/engine1/style.css file to make it look fabulous. Whatever you want! 

Check out an example at [https://djangoadventure.herokuapp.com/](https://djangoadventure.herokuapp.com/)
