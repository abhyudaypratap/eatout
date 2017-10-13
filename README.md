# eatout
 Django app that helps to decide where the team should dine.

App has the following features
User can search restaurants near him(count - 20)
User  will be able to add restaurant to Database from search results
User can view added restaurants and there information like address, name etc.
Each restaurant can be marked as visited
User can write reviews for each restaurant added and other user can comment on the same. 

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
