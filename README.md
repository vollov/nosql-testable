# nosql-testable
python project for testable policy manager

##Encryption
apt-get install build-essential libffi-dev python-dev
pip install bcrypt
pip install itsdangerous
pip install Flask-HTTPAuth==2.2.0
##MongoDB

####dumping
mongoexport --db sfm --collection events --out sfm_events.json

####importing
mongoimport -d sfm_test -c events --file sfm_events.json
