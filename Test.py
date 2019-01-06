import random
import pickle
import os
from Question import *
from Topic import *

class Test:

    def __init__(self):
        self.time = 0
        self.score = 0
        self.questions = []

    def selectTopics(self, mode='random', categories = ['physiology', 'physics', 'pharmacology', 'clinical'], numPerCategory = 2):
        topics = []
        for category in categories:
            pathToDir = 'Topics/TopicObjects/' + category
            categoryTopics = os.listdir(pathToDir)
            if mode == 'random':
                selected = random.sample(categoryTopics, numPerCategory)
                for topic in selected:
                    topics.append(os.path.join(pathToDir, topic))
            elif mode == 'worst':
                topicObjects = []
                for file in categoryTopics:
                    with open(os.path.join([pathToDir, file]), 'rb') as pickleFile:
                        topicObject = pickle.load(pickleFile)
                        topicObjects.append(topicObject)
                topicObjects.sort(key = lambda x: x.scores[-1:])
                for topic in topicObjects[:numPerCategory]:
                    topics.append(os.path.join(pathToDir, topic))


        return topics

    def populateQuestions(self):
        topics = self.selectTopics()
        for topic in topics:
            with open(topic, 'rb') as pickleFile:
                topicObj = pickle.load(pickleFile)
                questions = topicObj.questions
                self.questions.append(questions)

    def startTest(self):
        for topic in self.questions:
            for question in topic:
                input(question)
            print("----------------------------------")



test = Test()
test.populateQuestions()
test.startTest()