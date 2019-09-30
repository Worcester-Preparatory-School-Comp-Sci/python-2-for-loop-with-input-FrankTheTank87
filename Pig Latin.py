#Frank Carter 9/24
#takes a user inputted word and translates it into Pig Latin
myWord = input("Choose a word")
myList = ["a","e","i","o","u"]
if (myWord[0:1] in myList):
    print(myWord + "yay")
else:
    print(myWord[1:] + myWord[0:1] +"ay")




    
