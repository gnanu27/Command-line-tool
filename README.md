# Command-line-tool
CLI using Python and MongoDB

# setup
pip install -r requirments.txt

python main.py <commands>

# 1. Add a record

python main.py --add "{json structure}"

eg. python main.py --add "{'_id': 1, 'name': 'Jim', 'Job': 'Sales Man', 'salary': 10000}"

use '_id' element as key for every records. As MongoDB stores id key as '_id'.

# 2. Delete a record or records by a key-value pair

python main.py --delete "{Json}"

eg. python main.py --delete "{'_id': 1}"

# 3. Find all the records which contain a particular value

python main.py --find "{json struct}"

eg. python main.py --delete "{'_id': 1}"
or
eg. python main.py --find "{'name': 'Pam'}"

python main.py --fetchAll "{json str}"

eg. python main.py --fetchAll "{'name': 'Pam'}" 

--fetchAll will return all the value that marches key and --find return just the find one that matchs the key/


# Should be able to select particular fields while finding a record(by default it should return all the fields)
python main.py --select "{json str with key}" --f ""

eg.
python main.py --select '{"_id": 1}' --f "name"





