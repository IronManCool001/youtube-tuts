import pymongo
from pymongo import MongoClient
import dns
import pyttsx3

speaker = pyttsx3.init()



client = pymongo.MongoClient("mongodb+srv://dev:1234@cluster1.iwxwo.mongodb.net/test?retryWrites=true&w=majority")

db = client['test']

collection = db['test']

print("Do you want to search something or add something ?")
info = input("If you want to add type 'add'\n or \nIf you want to search type 'search' \n\n")
if info == "add" or info.lower() == "add":
    add = str(input("Enter what to add \n"))
    print("Also add the answer")
    a = str(input("Enter the answer \n"))
    add_q = {'Q':add,'A':a}
    collection.insert_one(add_q)
    speaker.say("Successfuly Added")
    speaker.runAndWait()

if info == "search" or info.lower() == "search":
    q = str(input("Enter a question that you would like to search? \n"))
    results = collection.find({'Q':q})
    for result in results:
        r =  result['A']
        print(r)
        speaker.say(r)
        speaker.runAndWait()