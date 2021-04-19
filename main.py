# Simone Luchetta, Student ID: 223716
# First assignment

# Basic imports
import spacy
import nltk
import copy

from spacy.symbols import nsubj, VERB

# Useful option if one wants to get advantage of the pretty print for trees
from nltk import Tree

# Loading a pre-trained model
nlp = spacy.load("en_core_web_sm")

text = "I saw the man with a telescope."

#######################################################################################################

def task_1(text):
    doc = nlp(text)
    for tokens in doc:
        pathsContainer = []
        if(tokens.dep_ != "ROOT"):
            dummyTokens = tokens
            while(dummyTokens.dep_ != "ROOT"):
                pathsContainer.append(
                    dummyTokens.dep_ + "-->" + dummyTokens.text)
                dummyTokens = dummyTokens.head
                if(dummyTokens.dep_ == "ROOT"):
                    pathsContainer.append(
                        "--> Root: " + dummyTokens.dep_ + "-->" + dummyTokens.text)
            pathsContainer.reverse()
            print(pathsContainer)


task_1(text)
print("End of task one...")

#######################################################################################################

def task_2(text):
    doc = nlp(text)
    subtreeList = []
    for tokens in doc:
        subtree = [t.text for t in tokens.subtree]
        subtree = "/t".join(subtree)
        subtreeList.append(subtree.split("/t"))
    for n in range(len(subtreeList)):
        print(subtreeList[n])
    # Optionally, one could even return the subtree or the subtreeList
    # return subtreeList
    # return subtree


task_2(text)
print("End of task two...")

#######################################################################################################

match = "with a telescope"


def Convert(string):
    li = list(string.split(" "))
    return li


def task_3(text, match):
    doc = nlp(text)
    matchList = Convert(match)
    subtreeList = []
    matchList.sort()
    for tokens in doc:
        subtree = [t.text for t in tokens.subtree]
        subtree = "/t".join(subtree)
        subtreeList.append(subtree.split("/t"))
    for n in range(len(subtreeList)):
        subtreeList[n].sort()
        if(subtreeList[n] == matchList):
            print("Match found...")
            return True
    print("Match not found...")
    return False


task_3(text, match)
print("End of task three")

#######################################################################################################

def task_4(wordseq, startOfSpan, endOfSpan):
    doc = nlp(wordseq)
    span = doc[startOfSpan:endOfSpan]
    return span.root.text


# I saw the man with a telescope.
print(task_4(text, 2, (len(text)+1)))
print(task_4(text, 0, (len(text)+1)))
print("End of task four...")

#######################################################################################################

def task_5(text):
    doc = nlp(text)
    subjList = []
    dobjList = []
    iobjList = []
    for tokens in doc:

        if(tokens.dep_ == "nsubj" or tokens.dep_ == "csubj"):
            subtree = [t.text for t in tokens.subtree]
            subtree = " ".join(subtree)
            subjList.append(subtree)

        if(tokens.dep_ == "dobj"):
            subtree = [t.text for t in tokens.subtree]
            subtree = " ".join(subtree)
            dobjList.append(subtree)

        if(tokens.dep_ == "iobj"):
            subtree = [t.text for t in tokens.subtree]
            subtree = " ".join(subtree)
            iobjList.append(subtree)

    dictionary = {"subj": subjList, "dobj": dobjList, "iobj": iobjList}
    print(dictionary)
    # return dictionary


task_5(text)
print("End of task five...")

#######################################################################################################
