class Definition:
    def __init__(self, text = "", part_of_speech = "n"):
        #part of speech
        self.pos = part_of_speech 
        self.text = text 

class Word:
    def __init__(self):
        self.word = ""
        self.definitions = [] 
        self.proficiency = 0.0
