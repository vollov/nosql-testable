# nosql-testable
python project for testable policy manager

##Encryption
apt-get install build-essential libffi-dev python-dev
pip install bcrypt

##MongoDB

####dumping
mongoexport --db sfm --collection events --out sfm_events.json

####importing
mongoimport -d sfm_test -c events --file sfm_events.json
