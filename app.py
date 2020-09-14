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
    print('Number of people found ' + str(len(people)))
    return people


def run_search():
    lists = []
    for i in data:
        row = i[0]
        print(row)
        people = search(row)
        lists.extend(people)
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

