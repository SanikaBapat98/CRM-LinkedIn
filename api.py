from linkedin_api import Linkedin
import functions as functions
from operator import itemgetter
import operator
import string
import json

# Authenticate using any Linkedin account credentials

email = "nikkibapat@me.com"
password = "tickles98"

#email = "esung@post.harvard.edu"
#password = "weezer"

api = Linkedin(email, password)
#profile = api.get_profile('madelinebradley')
#print(profile)
#profileN = api.get_profile('sanika-bapat-905405103')
#contact_info = api.get_profile_contact_info('madelinebradley')
#pep = api.search_people(keyword_company = '10X Genomics', keyword_title = 'CEO')
#rint(pep)
#Collect people data

bio_terms = ['Genomics', 'Computational Biology', 'Bioinformatics', 'DNA sequencing']

def functionalPosition(company, titles):
    people = []
    handledPeople = set()
    for title in titles:
        try:
            persons = api.search_people(keyword_company = company, keyword_title = title)
                #print("got people")
                #print("got " + len(persons) + " people")
                #print("now entering loop")
            for i in persons:
                #print("in loop")
                if i['public_id'] not in handledPeople:
                    try:
                        print()
                        handledPeople.add(i['public_id'])
                        print(i['public_id'])
                        print(i['headline'])
                        valid = verifyPerson(i['public_id'], company)
                        if valid[0]:
                            if functions.foundPerson(valid[1], title):
                                return [valid[1]]
                            else:
                                print('adding person')
                                people.append(valid[1])
                    except:
                        print('something went wrong')
                        continue
                else:
                    print('already founnd')
            print("out of loop")
            print(len(people))
        except KeyError:
            print("couldn't pull data")
    sorted_people = sorted(people, key=itemgetter('score'), reverse=True)
    return people[0] 
    #return people.sort(key=operator.itemgetter('score'), reverse=True)


def verifyPerson(person, company):
    try:
        peep = api.get_profile(person)
        #print(peep['experience'][0]['companyName'])
        relevant = verifyExp(company, peep['experience'])
        if relevant[0]:
            skills = functions.getList(peep['skills'])
            #print(skills)
            peep['score'] = functions.relevanceSkills(skills) + functions.relevanceTitle(relevant[2])
            print('score : ' + str(peep['score']))
            if peep['score'] >= 3:
                peep['skills'] = skills
                peep['id'] = person
                peep['company'] = relevant[1]
                peep['title'] = relevant[2]
                return [True, formatPerson(peep)]
        return [False]
    except KeyError:
        print('KeyError????')
        pass

def verifyExp(company, exp):
    #peep = api.get_profile('hilaryvance')
    #exp = peep['experience']
    for i in exp:
        if 'endDate' not in i['timePeriod']:
            #print('currently working at - ')
            #print(i['companyName'])
            #print(i['title'])
            comName = i['companyName'].translate(str.maketrans('', '', string.punctuation))
            if company.lower() == comName.lower():
                #print('company match to ' + company )
                #print(i['title'])
                return [True, i['companyName'], i['title'].lower()]
            #print('No match to ' + company )
    return [False]

def formatPerson(peep):
    person= {}
    entriesToKeep = ('company', 'firstName','lastName', 'title', 'headline','id', 'locationName','score','skills')
    for k in entriesToKeep:
        try:
            person[k] = peep[k]
        except KeyError:
            print('format person error. missing key - ')
            print(k)
            continue
    return person
    #peep['skills'] = skills
    

#functionalPosition(company, titles)
#print(verifyPerson('kumariyer', '23andMe'))
#print(verifyPerson('hilaryvance', '23andMe'))
#print(verifyPerson('hilaryvance', '10x Genomics'))
#print(verifyExp('23andMe'))
    
    

'''
dbList = []
p_list = json.load(open('links.json'))
p_list = p_list[1]


for p in p_list:
    dbList.append(api.get_profile(p))
    print(p)

json.dump(dbList, indent = 4)  
with open('people_data.json', 'w') as fp:
    json.dump(dbList, fp)

'''

