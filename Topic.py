import pickle

class Topic:

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.avgScore = 0
        self.tested = False
        self.questions = []
        self.scores = []
        self.allQuestionsEntered = False

    def addQuestions(self, rewrite = False):
        end = False
        if rewrite:
            self.questions = []
        while end == False:
            question = input(self.category + ', ' + self.name + ": Enter the next question: ")
            if len(question) > 0:
                if question == 'delete':
                    self.questions = self.questions[:-1]
                elif question == 'restart':
                    self.questions = []
                else:
                    self.questions.append(question)
            else:
                end = True
                self.allQuestionsEntered = True

        self.save()

    def save(self):
        with open('Topics/TopicObjects/' + self.category + '/' + self.name + '.pickle', 'wb') as file:
            pickle.dump(self, file)

