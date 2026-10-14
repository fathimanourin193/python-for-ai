10/5
10**5
my_long_string="""
good
I am nourin
have a good day
"""
print(my_long_string)

#-------------------------------------
is_true=True
age=19
can_vote=age>=18
print(can_vote)
print(age==19)
print(age!=20)

have_licencse=True
drive=age>=16 and have_licencse
print(drive)

day="saturday"
weekend=day=="saturday" or day=="sunday"
print(weekend)

adult=age>=18
child=not adult
print(child)

#------------------------------------
name="john"
print(f"My name is {name}")

sentence="I love python and java"
print(sentence.startswith("I"))
print(sentence.startswith("Q"))
print(sentence.find("python"))
print(sentence.count("python"))

#---------------------------------------------
#Data structures

#List
my_list=[name,day,have_licencse,"peter",18]
my_list[0]
my_list[-1]
my_list[-3]

#dictionaries
person={
    "name":"Alice",
    "age":18,
    "city":"New york"
}
person["age"]
person["name"]="David"
person["license"]=True
print(person)
del person["license"]
print(person)

print(person.values())
print(person.items())

#tuples
empty=()
colors=("red","black","blue")
colors[0]

#sets
empty_set=set()
new_set={"hello","one"}
fruits=set(["orange","grapes","apple"])
print(new_set)
print(fruits)

#-----------------------------------------------
#Functions
def greethelo():
    print("hello world")
greethelo()

#passing parameters
def greet(firstname,lastname):
    print(f"Hello,{firstname} {lastname}")
greet("Alice","john")
greet("Fathima","Nourin")

#return values
def add_return(a,b):
    return a+b
result=add_return(5,3)
print(result)
result+15

def min_max(numbers):
    return min(numbers),max(numbers)
mini,maxi=min_max([3,2,8,10])
print(f"min:{mini} max:{maxi}")

def numbers():
    num=[1,2,3]
    first_num=num[0]
    last_num=num[-1]
    return first_num,last_num
numbers()

#-------------------------------------------------
#packages
#built in packages

#pattern 1 import the whole module
import math
math.sqrt(25)

#pattern 2 import the specific item from a module
from math import sqrt, pi
sqrt(16)

import random
random.randint(1,10)
random.choice(["apple","grapes","banana"])

import datetime
date=datetime.date.today()
print(date)

import os
current_dir=os.getcwd()
print(current_dir)

import json
data={"name":["Alice","John"],"age":[18,17]}
result=json.dumps(data)
print(result)

import pandas as pd
df=pd.DataFrame(data)
print(df)


#API CALLS
import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()
print(response)
print(data["current"]["temperature_2m"])

#using a function

import requests
def get_weather(latitude,longitude):
  
  response=requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")
  data=response.json()
  return (data["current"]["temperature_2m"])

paris_temp=get_weather(48.85, 2.35)
london_temp=get_weather(51.50, -0.12)

print(f"Paris temp:{paris_temp}")
print(f"London temp:{london_temp}")


#--------------------------------------------------------
#Try and except
#Catch errors before they crash
try:
    age = int(input("Enter your age: "))
    print(f"In 10 years, you'll be {age + 10}")
except ValueError:
    print("Please enter a number")

#-------------------------------------
#classes
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# Create dog objects - using positional arguments
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Beagle")

# Or with named arguments (clearer)
dog3 = Dog(name="Charlie", breed="Poodle")

print(dog1.name)   # Buddy
print(dog2.breed)  # Beagle

#-----------------------------------------------------------
class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"

# Create different configurations
# Using positional for required arg, named for optional
dev_config = APIConfig("sk-dev-key", max_tokens=50)

# Using all named arguments (clearest)
prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)

# Access the configuration
print(dev_config.model)        # gpt-3.5-turbo
print(prod_config.model)       # gpt-4
print(prod_config.max_tokens)  # 1000

#------------------------------------------------------------
#methods and classes
class DataValidator:
    def __init__(self):
        self.errors = []
    
    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True
    
    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False
        return True
    
    def get_errors(self):
        return self.errors

# Use the validator
validator = DataValidator()

# Notice: we don't pass self, just the email
validator.validate_email(email="bad-email")
validator.validate_age(age=200)

# Or using positional arguments
validator.validate_email("another-bad-email")
validator.validate_age(150)

print(validator.get_errors())
# ['Invalid email: bad-email', 'Invalid age: 200', 'Invalid email: another-bad-email']



#-------------------------------------------------------------------------
#inheritance

# Parent class - general animal
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"

# Child class - specific animal
class Dog(Animal):
    def bark(self):
        return f"{self.name} says woof!"

# Create a dog - using positional argument
my_dog = Dog("Buddy")
# Or with named argument
my_dog2 = Dog(name="Max")

# Dog can do animal things (inherited)
print(my_dog.eat())    # Buddy is eating
print(my_dog.sleep())  # Buddy is sleeping

# Dog can also do dog things
print(my_dog.bark())   # Buddy says woof!

#-------------------------------------------------------------------------------
#method chaining

# Class bundles data and methods
class TextProcessor:
    def __init__(self, text):
        self.text = text
    
    def clean(self):
        self.text = self.text.strip().lower()
        return self
    
    def remove_punctuation(self):
        self.text = self.text.replace(".", "").replace(",", "")
        return self

# Chain methods on object
processor = TextProcessor(text="  Hello, World.  ")
result = processor.clean().remove_punctuation().text

#---------------------------------------------------------------------

