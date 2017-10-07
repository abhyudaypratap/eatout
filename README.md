# eatout
 Django app that helps to decide where the team should dine.


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
