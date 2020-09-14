import csv
import json
import pdb
import time
import timeit
import sys
import api as api
import pandas as pd
import functions as functions

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


def search(company):
    print('searching for people working in ' + company)
    people = api.functionalPosition(company)
    #people = functions.filterPeople(people)
    print('people returned')
    print(people)
    print('Number of people found')
    print(len(people))
    return people


def run_search():
    lists = []
    for i in data:
        row = i[0]
        print(row)
        people = search(row)
        lists.extend(people)
        print(i)
        print("\n These are the people found \n")
    return lists


if __name__ == '__main__':
    #globals()[sys.argv[1]](sys.argv[2], sys.argv[2] )
    
    value = input("If you want to search for a particular company and roles press 1, else if you want to run the search from the csv press 2 \n")
    print(f'You entered {value}')

    if value == '1':
        company = input("What is the company name? Be as accuracte as possible. \n")
        more = True

        print('Running search now!')
        output = pd.DataFrame()
        people = search(company)
        output = output.append(people,ignore_index=True)
        output.to_excel("output.xlsx")
        print('People found added to the excel file. Run the app again for another search!')
        print(str(functions.api_count) + " calls were made to the Linkedin API in this search")

    elif value == '2':
        print("Great, the app will look through the list of companies in the data.csv file. \n")
        more = True
        people = run_search()
        output = pd.DataFrame()
        output = output.append(people,ignore_index=True)
        output.to_excel("output.xlsx")

        print('People found added to the excel file. Run the app again for another search!')
        print(str(functions.api_count) + " calls were made to the Linkedin API in this search")
    
    else:
        print('Invalid Input')

'''
jobs = ['vice president product','vp product', 'director product', 'head product']
start = time.time()
people = run_search(5, 0, jobs)
#people = search('23andMe',jobs)
output = output.append(people,ignore_index=True)
output.head()
output.to_excel("output.xlsx") 
end = time.time()
print("Time consumed in working: ",end - start)
'''

#people = search('23andMe','Product')

#people = search('23andMe',jobs)

#print(functions.filterPeople(people))

#Loading and analysing data below
'''
with open('testing.json') as fp:
    data = json.load(fp)

for comp in data:
    if len(comp) > 1 :
        company = comp[0].get('company')
        print("\n" + company + "\n")
        for person in comp:
            print("Name : " + person.get('firstName') + " " + person.get('lastName'))
            print("ID : " + person.get('id'))
            print("Headline : " + person.get('headline'))
            print("Loaction : " + person.get('locationName'))
            print("List of skill : " )
            print(person.get('skills'))
            print()
    else:
        print("\n NO PEOPLE FOUND \n")
        
'''



