##Simple Web Application
The aim of this project is to develop a login system using simple web application. Application uses Python flask web framework, renders the HTML pages to allow users to login.

* Registered users are stored in in-memory and no database is involved.
* One user has been provided with credentials to login.
* Other users are not authorized to login to the portal.

###How the application was tested locally

```
To run the application locally
- Install JetBrains PyCharm IDE
- A simple flask application was created in PyCharm IDE
- Run `python3 app.py` on the terminal
- The server will be hosted on `http://localhost:5000`
```

###Package structure

```
azure-web-app
      |
      | --- static
      |       | --- style.css
      |
      | --- templates
      |       | --- layout.html
      |       | --- login.html
      |
      | --- app.py
```
