import json
import string
import csv

with open('bio_terms.json') as json_file:
    bio_terms = json.load(json_file)

positions = {'head' : 3, 'vp' : 5, 'vice' : 5, 'president' : 5, 'director' : 4, 'cheif': 3}


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

def relevanceSkills(skills, terms = set(bio_terms)):
    #return len(terms.intersection(skills)) * len(terms)) / 100.0
    #rev = len(terms.intersection(skills)) * 100 / len(terms)
    rev = len(terms.intersection(skills))
    #print(rev)
    if rev > 1:
        return 2
    else:
        return 0

def relevanceTitle(title, terms = positions):
    #return len(terms.intersection(skills)) * len(terms)) / 100.0
    #rev = len(terms.intersection(skills)) * 100 / len(terms)
    title = title.translate(str.maketrans('', '', string.punctuation))
    title = title.split()
    #print(title)
    pos = set(terms.keys())
    #print(pos)
    roles = pos.intersection(title)
    if len(roles) > 0:
        print(roles)
        role = roles.pop()
        #print(positions[role])
        return positions[role]
    else:
        return 0

def foundPerson(person, title):
    if 'president' in title or 'vp' in title:
        if person['score'] > 5:
            print('found vp')
            return True
    elif 'director' in title:
        if person['score'] > 4:
            print('found director')
            return True
    elif 'cheif' in title:
        if person['score'] > 3:
            print('found cheif')
            return True
    return False
    

def pretty_peoples(data):
    for i in data:
        name = i['firstName'] + " " + i['lastName']
        #industryName = i['industryName']
        company = i['company']
        title =  i['title']
        score = i['score']
        print("Name: " + name + "\n" + "Company: " + title + " at " + company + "\n" + "Score: " + str(score) + "\n")

#relevanceTitle('Director of product', terms = positions)

'''
def filterPeople(people):
    filtered_names = filterPositions(people)
    if len(filtered_names) > 0:
        return filtered_names
    else:
        return people

def filterPositions(people):
    positions = {'head' : 3, 'vp' : 5, 'vice president' : 5, 'director' : 4, 'cheif': 3}
    for title in people[:]:
        print('in title')
        print(title['title'].lower())
        if title['title'].lower() not in positions.keys():
            print('removing')
            #print(title)
            title.remove(title)
        else:
            title['score'] = 

    return people
'''
#skills = ['Genomics', 'Matlab', 'Python', 'Computational Biology', 'Bioinformatics', 'Algorithms', 'Hadoop', 'NGS', 'AWS', 'DNA sequencing', 'Machine Learning', 'Data Mining', 'Django', 'Mathematical Modeling', 'DNA Sequencing']
#print(relevance(skills, terms = set(bio_terms)))