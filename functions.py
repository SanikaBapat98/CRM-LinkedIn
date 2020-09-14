import json
import time
import string
import csv

api_count = 0

def check_api_count():
    if api_count > 30:
        print(str(api_count) + " call have been made to the LinkedIn API")
        print('Pausing code to avoid rate limit')
        time.sleep(3600)
        print('pause ended, will resume code now')


with open('skills.json') as json_file:
    bio_terms = json.load(json_file)

with open('scores.json') as json_file:
    file = json.load(json_file)
    positions = file[1]
    skills_score = file[2]['skills_score']
    threshold = file[3]['threshold']



def add_df(idx, lists = None):
    idx = data.index(idx)
    print(idx)
    for i in lists:
        print(i)
        data.insert(idx + 1, i)
    lenght = len(lists)
    return idx+len(lists)+1

def getList(listD): 
    list = [] 
    for dic in listD:
        list.append(dic['name']) 
    return list

def relevanceSkills(skills, terms = set(bio_terms), score = skills_score):
    #return len(terms.intersection(skills)) * len(terms)) / 100.0
    #rev = len(terms.intersection(skills)) * 100 / len(terms)
    rev = len(terms.intersection(skills))
    #print(rev)
    if rev > 1:
        return score
    else:
        return 0

def relevanceTitle(title, terms = positions):
    #return len(terms.intersection(skills)) * len(terms)) / 100.0
    #rev = len(terms.intersection(skills)) * 100 / len(terms)
    title = title.translate(str.maketrans('', '', string.punctuation))
    title = title.lower().split()
    pos = set(terms.keys())
    roles = pos.intersection(title)
    if len(roles) > 0:
        print(roles)
        role = roles.pop()
        return positions[role]
    else:
        return 0

def linkPerson(person):
    return 'https://www.linkedin.com/in/' + person + '/'
    print(person)
    

def foundPerson(person, minimum = threshold):
    if person['score'] >= minimum:
        return True
    else:
        return False
    
    

def pretty_peoples(data):
    for i in data:
        name = i['firstName'] + " " + i['lastName']
        #industryName = i['industryName']
        company = i['company']
        title =  i['title']
        score = i['score']
        print("Name: " + name + "\n" + "Company: " + title + " at " + company + "\n" + "Score: " + str(score) + "\n")

#print(relevanceTitle('Director of product', terms = positions))
#print(linkPerson('mike-lucero-46087013'))
