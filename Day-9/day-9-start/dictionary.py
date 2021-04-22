programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

# print(programming_dictionary)

# Retrieveing items from Dictionary

print(programming_dictionary["Bug"])

# Adding items in dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

# Create an empty dictionary

empty_dictionary = {}

print(empty_dictionary)


# Edit an item in a dictionary

programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(programming_dictionary[key] , end="\n")

# Wipe an exisiting dictionary clean

programming_dictionary = {}

#############################################################################################################################

# Nesting 

capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
    "India" : "Delhi"
}

# Nesting a list in dictionary

travel_log = {
    "France" : ["Paris" , "Lille" , "Dijon"] ,
    "Germany" : ["Berlin", "Frankfurt" , "Munich"]
}

# Nesting a dictionary in dictionary

travel_log = {
    "France" : { "cities_visited" : ["Paris" , "Lille" , "Dijon"] , "total_visits" : "12" },
    "Germany" : { "cities_visited" : ["Berlin", "Frankfurt" , "Munich"] , "total_visits" : "9" }
}

# Nesting a dictionary in list

travel_log = [
    { 
        "country" : "France" ,
        "cities_visited" : ["Paris" , "Lille" , "Dijon"] , 
        "total_visits" : "12"
    },    
    {   "country" : "Germany" ,  
        "cities_visited" : ["Berlin", "Frankfurt" , "Munich"] , 
        "total_visits" : "9" 
    }
]
