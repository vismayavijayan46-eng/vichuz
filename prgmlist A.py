#3a Generate positive list of numbers from a given list of integers
mylist=[23,58,-12,90,-45,81,49,-36]
print("First list:",mylist)
newlist=[x for x in mylist if x>0]
print("New List:",newlist)