# nosql-testable
python project for testable policy manager

##MongoDB

####dumping
mongoexport --db sfm --collection events --out sfm_events.json

####importing
mongoimport -d sfm_test -c events --file sfm_events.json
