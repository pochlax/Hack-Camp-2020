#SHELL- $pip install pymongo ==3.40

import pymongo
# SHELL - brew install mongodb (mac machine)
# SHELL - mongod

# ESTABLISHING A CONNECTION
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('mongodb://localhost:27017')

# change the attributes to database from SQL collections

db = client.pymongo_test

# Inserting usersPreference into the db 
# the draft when we got userinput

post = db.posts

post_data = {
  'title: userPrefences' ,#as the name of db, 
  'ClimateMatch':' ' ,
  'NGOMatch':' ',
  'SkillDict':' ',
  'InterestDict':' ',
  'NumDict':' ',
  'author':'Customer 1' 
}

saved_result = posts.insert_many([[post_data]])
print('Posts: ').format(saved_result.inserted_ids)

# Retrieving collections from the db



