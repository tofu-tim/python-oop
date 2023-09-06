# 1. Update values in dictionaries and lists

x = [ [5,2,3], [10,8,9] ] 

x[1][0] = 15
print("Problem 1: ")
print(x)
print()

# 2. Iterate Through a List of Dictionaries

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for student in students:
        print(f'first_name: {student["first_name"]}, last_name: {student["last_name"]}')

print("Problem 2:")
iterateDictionary(students)
print()

# 3. Get values from a list of dictionaries

def iterateDictionary2(key, students_list):
    values_list = []
    for student in students_list:
        if key in student:
            values_list.append(student[key])
    return values_list

first_names = iterateDictionary2('first_name', students)
last_names = iterateDictionary2('last_name', students)

print("Problem 3:")
print("Students first names: ", first_names)
print("Students last names: ", last_names)
print()

# 4. Iterate through a dictionary with list values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    print("Locations:")
    [print(location) for location in dojo['locations']]

    print("Instructors:")
    [print(instructor) for instructor in dojo['instructors']]

print("Problem 4:")
printInfo(dojo)