# eatout
 Django app that helps to decide where the team should dine.

App has the following features:
<ul>
<li>User can search restaurants near him(count - 20).</li>
<li>User  will be able to add restaurant to Database from search results.</li>
<li>User can view added restaurants and there information like address, name etc.</li>
<li>Each restaurant can be marked as visited.</li>
<li>User can write reviews for each restaurant added and other user can comment on the same.</li>
</ul> 

Used [Google Places API](https://developers.google.com/places/) for searching restaurants.(1500 API call)<br>
Used [Materialize](http://demo.geekslabs.com/materialize/v2.2/layout03/index.html) for frontend development

# Setup

### Install backend dependencies
* [postgres (version>= 9.4)](https://www.postgresql.org/)
* [virtualenv](https://virtualenv.pypa.io/en/stable/)

## Database Setup
* Create a db `eatoutdb`

## Backend Setup

### Update db details 
change your db details in `eatout_app/settings/dev.py`

### setup env files
Add `.env` files having relative config into `eatout_app/settings/` directory.

### virtualenv setup
* `vitualenv venv`
* `source venv/bin/activate`

### install requirements
`pip install -r requirements/dev.txt`
