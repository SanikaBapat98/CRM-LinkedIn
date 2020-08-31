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

def search(company,roles):
    print('searching for people working in ' + company)
    people = api.functionalPosition(company, roles)
    #people = functions.filterPeople(people)
    print('people returned')
    print(people)
    print('printing len')
    print(len(people))
    return people


def run_search(num, first, jobs):
    first = first + 2
    last = first+num
    lists = []
    comps = {}
    step = 1
    for i in range(first, last, step):
        row = data[i]
        print(row[0])
        if row[0] not in comps:
            if row[0]:
                people = search(row[0], jobs)
                #comps[row[0]] = people
                lists.append(people)
                print(i)
                print("\n These are the people found \n")
                #functions.pretty_peoples(people)
                step = 1
            else:
                step = 3
                print('next bucket')
    return lists


if __name__ == '__main__':
    #globals()[sys.argv[1]](sys.argv[2], sys.argv[2] )
    value = input("If you want to search for a particular company and roles press 1, else if you want to run the search from the csv press 2 \n")
    print(f'You entered {value}')

    if value == '1':
        company = input("What is the company name? Be as accuracte as possible. \n")
        roles = input("Please enter of list of roles you're looking for at {company}, seperated by a space. \n")
        print('Running search now!')
        output = pd.DataFrame()
        people = search(company,roles.split())
        output = output.append(people,ignore_index=True)
        output.to_excel("output.xlsx")
    else :
        print('Invalid input')

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



