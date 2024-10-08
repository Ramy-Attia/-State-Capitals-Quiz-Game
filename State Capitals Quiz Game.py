
#We create a dictionary in this code that contains all of the states and their capitals. Then, within a while loop, we check to see if the user input is q, in which case we exit, or if it is exactly as the capital of the chosen random state, in which case it is considered a correct answer, otherwise it is an incorrect answer. It keeps running and records both correct and incorrect answers. until q is entered by the user and the loop is broken The print statement then indicates the number of correct and incorrect answers.ered a correct answer, otherwise it is an incorrect answer. It continues to run and records both correct and incorrect answers. until the user input is q and the loop is broken The print statement then indicates how many correct and incorrect answers there were.
import random

capitals={
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona":"Phoenix",
    "Arkansas":"Little Rock",
    "California": "Sacramento",
    "Colorado":"Denver",
    "Connecticut":"Hartford",
    "Delaware":"Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinios": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Monies",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "St. Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Neveda": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakoda": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"  
} 

stateList=list(capitals.keys())

correct = 0
incorrect = 0

while(True):
    
    state=random.choice(stateList) 
    
    capital = capitals[state]
    
    answer = input("What is the capital of %s? (or enter q to quit): "%state )
    
    if answer.lower() == "q": 
        
        break
    
    elif answer.title() == capital:
        
        correct+=1
        
        print("That is correct.")
    
    else:
        incorrect+=1
        
        print("That is incorrect.")

print("You had {} correct responses and {} incorrect response.".format(correct,incorrect))
