### Python Web API Application ###

My client requires an api built using flask-restful, flask-sqlalchemy, flask-JWT, running on Apache using mod_wsgi, and MySQL using celery to manage background tasks. Once the project is complete I will pay the full amount in a single Milestone.

## Requirements: ##
* 2 - 3 day completion time
* Apache virtual host conf file, & mod_wsgi with wsgi.py
* Example: https://github.com/carlostighe/apache-flask
* MySql, Redis
* Python Modules: flask-restful, flask-SQLAlchemy, flask-JWT, celery, redis
* API with CRUD operations for all models.
* Example: https://github.com/uysalemre/Python-Flask-Sqlite-RestApi-WebApp
* User registers and either provides a new company during registration or adds the company_id when
registering for a company that already exists.
* Users should be able to authenticate with a username and password. (The password will only be stored in the
database as a hash.)
* Once authentication is complete all other requests will require a JWT Auth Token in the header.
* The user will also be able to upload multiple large images and then the api will respond with an Image
received message.
* Once the api receives an image it will start a background task using celery and Redis where the task will
resize the image to fit in a box for multiple sizes, (ex. original size, 1080x1080px , 640x640px, 320x320px,
160x160px, & 80x80px).
* Users should be able to request the thumbnails by passing in the box size. If the image is not done
processing, return a message saying the image is not ready yet. If it is done processing, return the image.

## Delivery Requirements: ##
* Delivery via a github.com repository.
* ReadMe with all information to set up the server for apache, mysql, redis, and celery on a CentOs 7 server.
* Instructions on how to set up a celery worker to run on the server in a production environment.
* python should be using 3.6 in a virtual environment venv
* apache_vhost.conf
* wsgi.py


## Database MySQL Models Below: ##
--Models--
users
- id - Primary Key - AutoIncrement
- company_id - Foreign Key
- username
- password
- first_name
- last_name
- email
- active - boolean
- created_date - datetime - default(CURRENT_TIME)

companies
- id - Primary Key - AutoIncrement
- company_name
- description
- active - boolean
- created_date - datetime - default(CURRENT_TIME)

images
- id - Primary Key - AutoIncrement
- user_id - Foreign Key
- file_name
- file_size
- file_type
- created_date - datetime - default(CURRENT_TIME)

## API Endpoints Below: ##
-- End Points --
* /auth

* /users
* /user/<string:username>
* /user/company
* /user/images
* /user/register

* /companies
* /company/<string:company_name>
* /company/users

* /image/upload/<int:user_id>
* /image/<int:image_id> #Returns original image
* /image/<int:image_id>/<int:size> #Returns thumbnail size

The above Models and Endpoints are for reference. If you need to add, remove, or modify any of these to make the site work please do so.
