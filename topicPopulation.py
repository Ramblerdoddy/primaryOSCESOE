import os
import pickle
from Topic import *

categories = ['physiology', 'physics', 'pharmacology', 'clinical']

def getTopicList(category):
    topicList = []
    with open('Topics/' + category + 'Topics.txt', 'r') as file:
        content = file.readlines()
    for line in content:
        fullStop = line.index('.')
        topic = line.replace(".", "").strip()
        topicList.append(topic)

    return topicList

def createTopics(category):
    topicList = getTopicList(category)
    for topic in topicList:
        newTopic = Topic(topic, category)
        newTopic.save()

def populateQuestions():
    for category in categories:
        path = 'Topics/TopicObjects/' + category
        for pickleFile in os.listdir(path):
            with open(path + '/' + pickleFile, 'rb') as file:
                topicObj = pickle.load(file)
            if not topicObj.allQuestionsEntered:
                topicObj.addQuestions()



populateQuestions()
# for category in categories:
#     path = 'Topics/TopicObjects/' + category
#     files = os.listdir(path)
#     for file in files:
#         with open(path + '/' + file, 'rb') as pickleFile:
#             topicObj = pickle.load(pickleFile)
#         topicObj.name = file.replace(".pickle", "")
#         topicObj.save()

# path = 'Topics/TopicObjects/clinical'
# file = "49 Burns and trauma.pickle"
# with open(path + '/' + file, 'rb') as pickleFile:
#             topicObj = pickle.load(pickleFile)
# print(topicObj.questions)
#
# topicObj.allQuestionsEntered = False
# topicObj.addQuestions()
