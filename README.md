# Elbow Bumps 

Welcome to our first year team project, a friendship recommendation web application......

View the remote website here: https://condescending-brattain-49a2b0.netlify.app/

---

# Elbow Bumps Backend

## Introduction

This is the backend of the Elbowbump App, build with flask, Python 3.9.1 .

## Installation

### Virtual Environment Setup

## Linux
Use "source venv.sh" command or use following command under the root directory of this repo:

<pre>
pip3 install virtualenv

virtualenv venv

source ./venv/bin/activate

pip3 install -r requirements.txt
</pre>

After virtual environment setting is done,   
next time you can enter virtual environment simply with   
"source ./venv/bin/activate" or ". ./venv/bin/activate".

## Windows
The commands are slightly different on Windows to set up the virtual environment.  
Again, on the root directory of this repo:

<pre>
pip install virtualenv

python -m virtualenv venv

./venv/Scripts/activate

pip install -r requirements.txt
</pre>
### Test

Then you can try to run main.py on your local machine to test:

<pre>
python main.py
</pre>

to see if it works properly.

## Setting up your local database

[Instructions are now here for Linux](https://github.com/bioBean/elbowbumps-backend/blob/main/LOCAL_SETUP.md).

## Linking to the remote database

For the remote database to work when testing, you first need to add a .env file containing the Postgres URI. This can be found in the WhatsApp group.  

To set it up properly, you need to provide it with the relevant key and `import os` in main.py. To provide it with the right key, you need to enter `SQLALCHEMY_DATABASE_URI = [the database URI]` in the .env file, and change the ENV variable in the bottom of main.py to anything other than `dev`.


## Testing the API

To test the API easily, you need to download [Postman](https://www.postman.com/) or use the web-app. You simply need to add a request and point to the right endpoint with the right method, entering the correct parameters.

## Commit

You can simply use push.sh script to push, or use the following commands:

<pre>
git add .
git commit -m "commit info"
git push
</pre>

if use heroku CLI, use
<pre> git push heroku main </pre>

instead of general "git push", but shouldn't going to use that anymore.


---

# Elbow Bumps Frontend 

Can be found in  `elbow-bump-frontend` branch on this repository, built with Vue.js. 

# How to test our website locally with both the backend and frontend 

## Requirements before you carry on:

1. Set up the local database and view it (eg. using dbeaver). 
2. Be able to run the front-end locally
3. Be able to run the back-end locally 
4. Have both the front-end and the back-end in two different folders locally (you can git clone twice)

## How to do it!
Make sure you do it in this order
1. Navigate to `src/store.js` in the front end repository and change `isUsingRemote` to `false`
2. Navigate to `elbowbumps/_init_.py` in the back end repositry and set `ENV` to `'dev'`
3. Run the front end - `npm run serve` in the front end folder
4. Run the back end - `python3 main.py` in your back end folder
5. Using the local host front-end link, navigate through the website. Try registering a new user and confirm there is an entry in your local user_data table in dbeaver.

## Common issues 
- Something about the database/backend SQL being upset -> you probably need to delete your *local* tables in dbeaver and run `main.py` again because one of us restructured the database
- `npm run serve` saying it fails to compile -> run `npm install` in that directory and then run `npm run serve` again

## NOTE 
- DO NOT push `src/store.js` or `elbowbumps/_init_.py` unless you actually changed something in them
- It will break the deployed version of the site
- Faridz will not be happy with you 
