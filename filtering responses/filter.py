import pandas as pd
import numpy as np

responses = pd.read_excel('CSC 533 Privacy Survey (Responses).xlsx')

correct_link_2 = ['Researchers were able to request and collect passwords from unsuspecting users', 
'Eavesdrop on unsuspecting users']

correct_link_3 = ['The security flaw affects only amazon alexa', 
'Skill squatting is where 3rd party skills have similar names to activate them', 
'The link have videos explaining the problem']

link_2 = 'To make sure you have gone through the links, can you please check the most appropriate boxes related to the privacy issue demonstrated in link 2:'
link_3 = 'To make sure you have gone through the links, can you please check the most appropriate boxes related to the privacy issue demonstrated in link 3:'

res = 0
yes_counter = 0

for index, row in responses.iterrows():
    flag_2 , flag_3 = False, False
    checker_2 = row[link_2].split(",")
    checker_3 = row[link_3].split(",")

    for e in checker_2:
        if e in correct_link_2:
            flag_2 = True
            break
    for e in checker_3:
        if e in correct_link_3:
            flag_3 = True
            break
    
    if flag_3 and flag_2:
        res += 1
        if row['smaller'] == "Yes":
            yes_counter += 1

print("The filtered count of responses:", res)
print("The percentage of people whose perception is changed:", yes_counter / res * 100)
