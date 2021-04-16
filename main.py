# Simone Luchetta
# First assignment

#Basic imports
import spacy
import nltk
import copy

from spacy.symbols import nsubj, VERB

# Useful option if one wants to get advantage of the pretty print for trees
from nltk import Tree

# Loading a pre-trained model
nlp = spacy.load("en_core_web_sm")

text = "I saw the man with a telescope."

def task_1(text):
    doc = nlp(text)
    for tokens in doc:
        pathsContainer = []
        if(tokens.dep_ != "ROOT"):
            dummyTokens = tokens
            while(dummyTokens.dep_ != "ROOT"):
                pathsContainer.append(dummyTokens.dep_ + "-->" + dummyTokens.text)
                dummyTokens = dummyTokens.head
                if(dummyTokens.dep_ == "ROOT"):
                    pathsContainer.append("--> Root: " + dummyTokens.dep_ + "-->" + dummyTokens.text)
            pathsContainer.reverse()
            print(pathsContainer)
    

task_1(text)

