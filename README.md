# to-do-list

## The 198123018902839291380912809312th to-do-list

### An application built with Python, Flask and Flask-SQLAlchemy.

A simple rest service that as opposed to other tons of similar repositories out there, 
avoids the use of tools like flask-restful. 
I use here only a few packages and this allowed me to keep almost all 
the relevant code in one not very long file.<br>
A good idea is to extend the app to one with tools like flask-restful and marshmallow,
adding probably some entities/endpoints/features and evaluating the trade-off. Pytest is also used here and thanks to the fixture decorator, we're able to test the app on
a different DB copy.

###### **Instructions**:

- git clone the repo in your local machine
- install the requirements - as usual, preferably in a virtual environment.
Please notice that the app was developed with Python 3.10, so that's the ideal version
before proceeding (although it will probably work also with Python 3.9)
- install sqlite3 in your local machine if it's not already there. You can check 
it just running "sqlite3" on a terminal.

Done. The app it's ready to use and there's already a couple of tasks-examples in your todo-list. 
(because the file todo.db was included as part of the repo). 
Execute python app.py and the server will listen on your localhost.

Supported routes (defined in app.py):

_/tasks_ ('GET' 'DELETE', 'POST') <br>
Respectively, get all the tasks, delete all the tasks, post a task. In this last case, the body 
(form) of the request needs to be with json format and to have one parameter:
_{"task_title":"<some_task>"}_

_/tasks/<task_id>_ ('GET', 'DELETE') <br>
Respectively, get a task, delete a task. 

_/tasks/done/<task_id>_ ('PUT') <br>
mark a task as done.
 
That's it. The app was done mainly as an exercise so issues would not be surprising. 
If you find such, I'd be happy if you reach out :) I'd also be glad to hear questions, suggestions, etc. <br><br>
Enjoy!
