                         # Discover Thailand
## Introduction

Discover Thailand is a project which promotes information about traveling, culture and places to visit. Is also, provides possibility to buy some packages made special for Thailand travelers. The project has been buid with [Python] (https://www.python.org/) using [Django] (https://www.djangoproject.com/)
Text content is not intended for production.
A live version of this app is hosted [here](https://discover-thailand.herokuapp.com/)


## Description
The project was build after CodeInstitute skeleton.
Some of the key features of this web application are:

* Account: log in, authentication, profile
* A home app with information about Thailand
* A about app which is a guide regarding Thailand for travelers
* A blog app which use Disqus for comments
* A products app whit paypal payments
* A forum app
* A polls app
* A contact form

*__About__*
* It contains a short guide which provides information about Thailand

*__Account, register and authentication__*
* The email acts as username
* Once registered and logged in, the user can accesses his profile page where he can found basic information and can reset his password.
Also, the user can add a post in a blog, add threads or comment in forum

*__Blog__*
* Enables users to create articles about Thailand
* Any user can add or edit an article. Also they are allowed to add a picture.
* Any visitor can read articles and add a comment using **Disqus**.
* Each article shows number of visualization and tags.

*__Forum with polls__*
* Any user can create a **thread** in a subject.
* Each thread, contains a poll and posts.
* Only members can *create, edit and delete* a post.

*__Products__*
* There is a list of different packages that users can buy using paypal.

*__Contact__*
* A **form** that allows any visitor to ask question.

## Testing
* Has been tested manual for every feature
* Has been tested whit an online validator [w3.org](https://validator.w3.org/).
* Also, some of the apps have been tested using Django Framework.
* Blisk has been used to test the responsive part. Have yet to come across any undesired responsiveness issues.


## Technology used
* HTML5
* CSS3
* [Bootstrap] (https://www.http://getbootstrap.com//)
* [Django] (https://www.djangoproject.com/)
* Python
* JavaScript
* jQuery
* Relational database: MySQL/SQLite


## Instructions

* If you wish to test/develop this app locally, clone this repo and use the following guidelines:

Install:

* `pip install -r requirements.txt`

Set database:

* `python manage.py migrate`

Run project:

* `python manage.py runserver`

On your browser in the URL bar enter

* `http://127.0.0.1:8000`

Create a superuser

* `python manage.py createsuperuser`

Access admin account:

* `http://127.0.0.1:8000/admin/`


## Acknowledgments
- The text used in the project was retrieved from:

* https://www.nomadicmatt.com/travel-guides/thailand-travel-tips/
* http://www.statravel.co.uk/travel-thailand.htm
* http://thailand-uk.com/forums/
* https://www.tripadvisor.co.uk/
* https://www.lonelyplanet.com/thailand


