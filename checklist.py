# hello world
print("Hello World")
checklist = list()
# I will work on this project later
# checklist = list()
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)

#create function 
def create(item):
    checklist.append(item)
#READ function
def read(index):
    return checklist[index]

#Update
checklist = ['Blue', 'Orange']
checklist[1] = 'Cats'
print(checklist)


    