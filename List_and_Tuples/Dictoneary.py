#Create a Dictionary and take input form the user and return the meaning for the word from the Dictionary

dic = {
       "help": " tho give support by any mean",
       "enjoy":" feeling of happines by doing somthing",
       "solve" : "put efforts to nutralize the problem",
       "team" : "people come together and complet the task",
       "subject" : {
           "phy" : 55,
           "chem" : 77,   #(nested dictionary) 
           "maths" : 98
       }
    }

text = input("Enter the word: ")
print(dic["subject"]["phy"])
print(dic[text])