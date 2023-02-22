#Python Program to add a record to nested dictionary
  # people = {1: {'name': 'kohli', 'age': '35', 'profession': 'cricketer',"lastname":"virat"},
   #       2: {'name': 'rohit', 'age': '37', 'profession': 'cricketer',"lastname":"sharma"}}
def nest_key(t):
    t[1]['kesava']=24
    t[2]['modi']=23
t={1: {'name': 'kohli', 'age': '35', 'profession': 'cricketer',"lastname":"virat"}, 2: {'name': 'rohit', 'age': '37', 'profession': 'cricketer',"lastname":"sharma"}}
print(nest_key(t))
