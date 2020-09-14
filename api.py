from linkedin_api import Linkedin
import functions as functions
from operator import itemgetter
import operator
import string
import json

# Authenticate using any Linkedin account credentials

with open('scores.json') as json_file:
    file = json.load(json_file)
    positions = file[0]
    #jobs = [*positions]

with open('auth.json') as json_file:
    auth = json.load(json_file)
    email = auth['email']
    password = auth['password']

api = Linkedin(email, password)


def functionalPosition(company, titles = positions):
    people = []
    handledPeople = set()
    for title in titles:
        print('Searching for ' + title )
        try:
            functions.check_api_count()
            persons = api.search_people(keyword_company = company, keyword_title = title)
            functions.api_count += 1
            for i in persons:
                #print("in loop")
                if i['public_id'] not in handledPeople:
                    try:
                        print()
                        handledPeople.add(i['public_id'])
                        print(i.get('public_id'))
                        print(i.get('headline'))
                        valid = verifyPerson(i['public_id'], company)
                    
                        if valid[0]:
                            if functions.foundPerson(valid[1][0]):
                                people.extend(valid[1])
                    except:
                        print('something went wrong in pulling profile')
                        continue
                else:
                    print('already founnd')
        except KeyError:
            print("couldn't pull data - rate limit probably reached or linkedin has imposed other restrictions. Please try with another account.")
    #sorted_people = sorted(people, key=itemgetter('score'), reverse=True)
    return people 
    #return people.sort(key=operator.itemgetter('score'), reverse=True)


def verifyPerson(person, company):
    try:
        functions.check_api_count()
        peep = api.get_profile(person)
        functions.api_count += 1
        #print(peep['experience'][0]['companyName'])
        relevant = verifyExp(company, peep['experience'])
        #print(relevant)
        if relevant[0]:
            skills = functions.getList(peep['skills'])
            #print(skills)
            peep['score'] = functions.relevanceSkills(skills) + functions.relevanceTitle(relevant[2])
            print('score : ' + str(peep['score']))
            if peep['score'] >= 3:
                peep['skills'] = skills
                peep['id'] = functions.linkPerson(person)
                peep['company'] = relevant[1]
                peep['title'] = relevant[2]
                peep['timePeriod'] = relevant[3]
                return [True, formatPerson(peep, relevant[4])]
        return [False]
    except KeyError:
        print('KeyError????')
        pass

def verifyExp(company, exp):
    past = {}
    found = False
    for i in exp:
        comName = i['companyName'].translate(str.maketrans('', '', string.punctuation))
        title = i['title'].lower()
        if 'endDate' not in i['timePeriod']:
            if company.lower() == comName.lower():
                found = True
                present_title = i['title'].lower()
                timePeriod = i['timePeriod']['startDate']
        else:
            timePeriod = str(i['timePeriod']['startDate']['year']) + ' to ' + str(i['timePeriod']['endDate']['year'])
            past[comName] = [title, timePeriod]
    if found:
        return [True, company, present_title, timePeriod, past]
    return [False]

def formatPerson(peep, past):
    exp_person = []
    person= {}
    entriesToKeep = ('company', 'timePeriod', 'firstName','lastName', 'title', 'headline','id', 'locationName','score','skills')
    for k in entriesToKeep:
        try:
            person[k] = peep[k]
        except KeyError:
            print('format person error. missing key - ')
            print(k)
            continue
    exp_person.append(person)
    for key, value in past.items(): 
        print (key, value)
        old_exp = dict(person)
        old_exp['company'] = key
        old_exp['title'] = value[0]
        old_exp['timePeriod'] = value[1]
        exp_person.append(old_exp)

    return exp_person
    #peep['skills'] = skills
    

#functionalPosition(company, titles)
#print(verifyPerson('kumariyer', '23andMe'))
#print(verifyPerson('hilaryvance', '23andMe'))
#print(verifyPerson('mike-lucero-46087013', '10x Genomics'))
#print(verifyExp('23andMe'))
    

