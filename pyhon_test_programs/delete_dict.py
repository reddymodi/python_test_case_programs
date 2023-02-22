#Python Program to delete a record from nested dictionary
  # people = {1: {'name': 'kohli', 'age': '35', 'profession': 'cricketer',"lastname":"virat"},
   #       2: {'name': 'rohit', 'age': '37', 'profession': 'cricketer',"lastname":"sharma"}}
def deleted(d):
    del d[1]['profession']
    return d
people = {1: {'name': 'kohli', 'age': '35', 'profession': 'cricketer',"lastname":"virat"},2: {'name': 'rohit', 'age': '37', 'profession': 'cricketer',"lastname":"sharma"}}
print(deleted(people))

