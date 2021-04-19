# NLU_Assignment_1
My repository for the assignment

Download spacy with the following commands:

`pip install -U pip setuptools wheel`

`pip install -U spacy`

Download and use a pre-trained model:

`python -m spacy download en_core_web_sm`

`nlp = spacy.load("en_core_web_sm")`

I ran all the tasks with this piece of text:

```
text = "I saw the man with a telescope."
```
## Dependency path from root to token:
This task is carried out by using the `task_1` function. Substantially, the input text is transformed into a spacy doc object; then, for each of the tokens in the document, it is possible to extract its path to the root and store it into some kind of data structure (e.g. a list). Then, all the elements in the list are reversed via the `.reverse` operation so that one ends up with the plain path from the root to a token. The use of a `dummyTokens` variable is necessary in order to update the head of the token. The output will be the following:
```
['--> Root: ROOT-->saw', 'nsubj-->I']
['--> Root: ROOT-->saw', 'dobj-->man', 'det-->the']
['--> Root: ROOT-->saw', 'dobj-->man']
['--> Root: ROOT-->saw', 'prep-->with']
['--> Root: ROOT-->saw', 'prep-->with', 'pobj-->telescope', 'det-->a']
['--> Root: ROOT-->saw', 'prep-->with', 'pobj-->telescope']
['--> Root: ROOT-->saw', 'punct-->.']
End of task one...`
```

## Extract subtree of a dependents given a token:
For this task, a subtree for each token is extracted via the `task_2` function. It is possible to acces to the subtree of a token by simply the `.subtree` command. All the subtrees are stored in `subtreeList`, and are then printed to output:

```
['I']
['I', 'saw', 'the', 'man', 'with', 'a', 'telescope', '.']
['the']
['the', 'man']
['with', 'a', 'telescope']
['a']
['a', 'telescope']
['.']
End of task two...
```

## Check if a given list of tokens forms a subtree:
This task is performed by running the `task_3` function. It simply receives as an input a couple of text. The first one is processed using `nlp(text)`, and then each subtree of each token is extracted and stored in `subtreeList`. Furthermore, each subtree is then sorted in order to carry out a comparison between the segment of text that one wants to verify (`match`) and the given text (`text`). The output will either be `True` if a match is found, or `False`. For example, passing the text "I saw the man with a telescope." and the match "with a telescope", the output will be the following:

```
Match found...
End of task three
```

Note that the match to verify is previously converted from string format to list via the `Convert(string)` function.

## Identify head of a span, given its tokens
This task simply requires to find the head of a span. An input text is processed by using the `nlp(doc)` functionality, and then a `span` object is created, specifying the starting token position and the end token position. Since spacy comes with a "span" object, it is easy to get the head of a span by simply taking a look at the `span.root` property.

For example, for the input text `I saw the man with a telescope.`, starting from the second token ("the") we will get the following:

```
print(task_4(text, 2, (len(text)+1)))
```

Which will give us:

```
man
```

But we could also form a span which comprises the entire lenght of the sentence:

```
print(task_4(text, 0, (len(text)+1)))
```

For which the root will be:

```
saw
```

## Extract sentence subject, direct object and indirect object spans
This task consisted in accessing the pos tagging properties of the various tokens in the sentence. It is performed by the `task_5` function. For every token in the sentence, its `.dep_` property is verified. If it matches one of the various requests, it is stored in one of the three specific list, them being:

```
subjList = []
dobjList = []
iobjList = []
```

Once all the items are extracted, the lists are put into a dictionary, for which the keys indicate its matching pos tagging. Referring to the text `I saw the man with a telescope`, we'll have the following output:

```
{'subj': ['I'], 'dobj': ['the man'], 'iobj': []}
End of task five...
```

### Simone Luchetta, 223716