import random
from replit import db

DB_KEY="piropos"

def contains_key():
  return DB_KEY in db.keys()

def get_all_piropos():
  if contains_key():
    return db[DB_KEY]

def get_piropo():
  if contains_key():
    l=db[DB_KEY]
    return random.choice(l)

def add_piropo(piropo):
  if contains_key():
    l=db[DB_KEY]
    l.append(piropo)
    db[DB_KEY]=l
  else:
    db[DB_KEY]=[piropo]

def delete_piropo(index):
  cpy=[]
  if contains_key():
    l = db[DB_KEY]
    if len(l) > index :
      del l[index]
      db[DB_KEY] = l


