
import math

# __Question 1
# Sort the list and find the min and max age

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages[0])
print(ages[len(ages)-1])

print(ages)

# Add the min age and the max age again to the list

ages.append(19)
ages.append(26)
ages.sort()
print(ages)

# Find the median age
print(ages[int(len(ages)/2)])
print(ages)

# Find the average age
print(sum(ages)/len(ages))
print(ages)

# Find the range of the ages
print(ages[int(len(ages)-1)]-ages[0])
print(ages)

print()

# __Question 2

# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary

dog.update({"name": "Winston", "color": "White", "legs": "4", "age": "9"})

print(dog)
# Create a student dictionary and add first_name, last_name, gender, age, marital_status,
# skills, country, city and address as keys for the dictionary

student = {"first_name": "Powell", "last_name": "Medlock", "gender": "M", "age": "22", "marital_status": "single",
           "skills": [], "country": "USA", "city": "Odessa", "address": "308 Negra Arroyo Lane"}

# Get the length of the student dictionary

print(len(student))


# Get the value of skills and check the data type, it should be a list

print(type(student["skills"]))


# Modify the skills values by adding one or two skills


student.update({"skills": ["Coding", "screaming into the void"]})

print(student)

# Get the dictionary keys as a list

student_list = list(student.keys())
print(student_list)

# Get the dictionary values as a list

value_list = list(student.values())

print(value_list)

print()

# _Question 3_

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

sisters = ("Reagan",  "Avail",)

brothers = ("Hunter", "Riley", "Lucas", "Mikey")

# Join brothers and sisters tuples and assign it to siblings

siblings = brothers + sisters

print(siblings)
# How many siblings do you have?

print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members

parents = ("Karen", "Scott")

family_members = parents + siblings

print(family_members)

print()

# _Question 4_

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies

print(len(it_companies))


# Add 'Twitter' to it_companies

it_companies.add("Twitter")

print(it_companies)

# Insert multiple IT companies at once to the set it_companies
added_companies = {"Open AI", "HP", "Dell"}
it_companies.update(added_companies)

print(it_companies)

# Remove one of the companies from the set it_companies

it_companies.remove("Facebook")
print(it_companies)

# What is the difference between remove and discard

# Answer: if used while the input value doesn't exist in the set, remove will throw a Key error where discard will not

# Join A and B

A.update(B)

print(A)

# Find A intersection B

print(A.intersection(B))

#Is A subset of B

print(A.issubset(B))

# Are A and B disjoint sets

print(A.isdisjoint(B))

# Join A with B and B with A

A.update(B)
print(A)
B.update(A)
print(B)

# What is the symmetric difference between A and B

C = A.symmetric_difference(B)

print(C)

# Delete the sets completely

A.clear()
B.clear()
print(A)
print(B)

# Convert the ages to a set and compare the length of the list and the set.

print("age list length: ", len(age), " age set length: ", len(set(age)))
print()

# -Question 5-
radius = 30

# Calculate the area of a circle and assign the value to a variable name of _area_of_circle_

area_of_circle = math.pi * (pow(radius, 2))
print(area_of_circle)

# Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_

circum_of_circle = 2*math.pi*radius
print(circum_of_circle)

# Take radius as user input and calculate the area.

new_radius = input("pick a radius for the circle: ")
print(math.pi * (pow(int(new_radius), 2)))
print()

# _Question 6_

# “I am a teacher and I love to inspire and teach people”
# How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

txt = "I am a teacher and I love to inspire and teach people"

x = set(txt.split())

print(x)
print()
# _Question 7_

# Use a tab escape sequence to get the following lines.
# Name      Age     Country     City
# Asabeneh  250     Finland     Helsinki

print("Name\t\t", "Age\t", "Country\t", "City")
print("Asabenah\t", 250, "\t", "Finland\t", "helsinki")
print()

# _Question 8_

# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# “The area of a circle with radius 10 is 314 meters square.”

radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius %d is %.2f.' % (radius, area))

# _Question 9_

# Write a program, which reads weights (lbs.) of N students into a list and convert these weights to
# kilograms in a separate list using Loop. N: No of students (Read input from user)

N = input("how many students are in the class: ")

weights = []
new_kg = []
for x in range(int(N)):
    howbig = input("what is the weight of this student in pounds: ")
    weights.insert(x, int(howbig))


for x in range(int(N)):
    new_kg.append(round(weights[x] * 0.453592, 2))

print(weights)
print(new_kg)


















