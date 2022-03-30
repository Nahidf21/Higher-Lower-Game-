
from game_data import data
import random
length=len(data)
def name_01(x):
        name_new=data[x]["name"]
        print(name_new)

def follower_01(x):
        follower_new=data[x]["follower_count"]
        return follower_new
def description_01(x):
        description_new=data[x]["description"]
        print(description_new)
def Country_01(x):
        Country_new=data[x]["Country"]
        print(Country_new)

def random_01(start):
    if start=="yes":
        for _ in range(0,1):
            y=random.randint(0,length-1)
    else:
        print("Stop")
    
    return y
    
start= input("Yes or no : ")
if start=="yes":
    x=random_01("yes")
    name_01(x)
    print(follower_01(x))
    description_01(x)
    Country_01(x)
else:
    print("Game stop")



    
