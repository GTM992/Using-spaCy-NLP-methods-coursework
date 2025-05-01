import spacy
nlp = spacy.load('fi_core_news_sm')
def give_name(name="finnish.txt"):
    return name
give_name(input("Enter the name of a text file\n"))
with open("finnish.txt", "r", encoding="utf-8") as file:
    my_text = file.read()

test_doc = nlp(my_text)
print("Components available: ", nlp.pipe_names)
def help_output():
    print('''This is a showcase of basic capabilites of spaCy's trained pipeline.
        Pick a ".txt" file or ignore the entry to choose the test one (finnish.txt).
        Add commands to the set and enter 'done' to execute them.''')
print(test_doc)
decisions = set()
print(f"{"-"*10}")
print(f'''Please enter the keyword to add specified tokens to the output list. 
{"-"*10}''')
while True:
    
    decision = input(f'''To proceed to results, type "done".\n{"-"*10}\n''')
    if decision == "punctuation":
        decisions.add(decision)
    elif decision == "numbers":
        decisions.add(decision)
    elif decision == "measure length":
        decisions.add(decision)
    elif decision == "stop words":
        decisions.add(decision)
    elif decision == "filter":
        dec1 = input("Type '1' if you want only to output filtered text. Type '2' if you want to filter the text. \nPlease note that the process is irreversible. \n")
        if dec1 == '1':
            decisions.add(decision)
        if dec1 == "2":
            import re
            dec2 = input("By default, stop words and punctuation are going to be filtered out. Type 'y' to proceed, type 'n' to configure these attributes\n")
            if dec2 == 'y':
                #test_doc = [token for token in test_doc if not token.is_stop and not token.is_punct]
                test_doc = nlp(re.sub(r'[\[,.-\]]', '', str([token for token in test_doc if not token.is_stop and not token.is_punct])))
                
            elif dec2 == 'n':
                dec3 = input("Enter '1' to filter out stop words only. Enter '2' to filter punctuation only. Enter '3' to filter both")
                if dec3 == '1':
                    test_doc = [token for token in test_doc if not token.is_stop]
                    test_doc = re.sub("[\]\[]", "", str(test_doc))
                    #print(test_doc)
                    test_doc = nlp(re.sub(r"(, )", ' ', test_doc))
                    print(test_doc)
                elif dec3 == '2':
                    #test_doc = [token for token in test_doc if not token.is_punct]
                    test_doc = nlp(re.sub(r'[\[,\-\.\]]', '', str([token for token in test_doc if not token.is_punct])))
                    print(test_doc)
                elif dec3 == '3':
                    test_doc = [token for token in test_doc if not token.is_punct and not token.is_stop]
                    test_doc = nlp(re.sub(r'[\[,\.\-\]]', '', str([token for token in test_doc if not token.is_stop and not token.is_punct])))
                    print(test_doc)
    elif decision == "hash values":
        decisions.add("hash values")
    elif decision == "lemmatise":
        decisions.add("lemmatise")
    elif decision == "uppercase tokens":
        decisions.add("uppercase tokens")
    elif decision == "help":
        decisions.add("help")
    elif decision == "tag POS":
        decisions.add("tag POS")
    elif decision == "visualize":
        decisions.add("visualize")
    elif decision == "display names":
        decisions.add("display named entities")
    elif decision == "match":
        decisions.add("match")
    elif decision == "phrase match":
        decisions.add("phrase match")
    elif decision == "compare tokens":
        decisions.add("compare tokens")
    if "help" in decisions:
        help_output()
        decisions.remove("help")
    elif decision == "done":
        break
    print(f"{"-"*10}")
print("Engaged commands:", decisions)

def punctuation(test_doc):
    for token in test_doc:
        if token.is_punct:
            print(token.text, f"token index in text: {token.i}", sep = "\t")
if "punctuation" in decisions:
    punctuation(test_doc)

def numbers(test_doc):
    for token in test_doc:
        if token.like_num:
            print(token.text, f"token index in text: {token.i}", sep = "\t")
if "numbers" in decisions:
    numbers(test_doc)

def measure_length(test_doc):
    test_doc_cleaned = [toke for toke in test_doc if not toke.is_stop and not toke.is_punct]
    print("Length of text with stop words: ", len(test_doc))
    print("Length of text with no stop words: ", len(test_doc_cleaned))

if "measure length" in decisions:
    measure_length(test_doc)

def stop_words(test_doc):
    test_doc_stop = [token for token in test_doc if token.is_stop == True]
    for stop_token in test_doc_stop:
        print(stop_token.text)
if "stop words" in decisions:
    print(stop_words(test_doc))

def filter(test_doc):
    test_doc_cleaned = [toke for toke in test_doc if not toke.is_stop and not toke.is_punct]
    return test_doc_cleaned
if "filter" in decisions:
    print(filter(test_doc))

def hash_value(test_doc):
    for token in test_doc:
        hash_value = test_doc.vocab.strings[token.text]
        print(token.text, hash_value, sep = "\t")
if "hash values" in decisions:
    hash_value(test_doc)

def lemmatise(test_doc):
    print(f'''{"-"*10} \nLemmatisation results:\n''')
    for token in test_doc:
        print(token.text, "  -  ", token.lemma_)
if "lemmatise" in decisions:
    lemmatise(test_doc)

def uppercase_tokens(test_doc):
    list_up = []
    for token in test_doc:
        if token.is_upper:
            print(token.text)
            list_up.append(token)
    if len(list_up) == 0:
        print("no uppercases found")
if "uppercase tokens" in decisions:   
    uppercase_tokens(test_doc)

def tag_pos(test_doc):
    for token in test_doc:
        print(token.text, token.pos_, token.tag_, sep =" --- ")
if "tag POS" in decisions:
    tag_pos(test_doc)

def visualize(test_doc):
    from spacy import displacy
    sentences = list(test_doc.sents)
    displacy.serve(sentences, style = "dep")
if "visualize" in decisions:
    visualize(test_doc)

def display_named_entities(test_doc):  #entity != token
    for e in test_doc.ents:
        print(e.text, e.label_, sep=" --- ")
if "display named entities" in decisions:
    display_named_entities(test_doc)

def match(test_doc):
    from spacy.matcher import Matcher
    matcher = Matcher(test_doc.vocab)
    pattern = []
    n = int(input("How many tokens are to be in the pattern?\n"))
    for i in range(n):
        dic = dict()
        print(f"token {i+1}. Configure key. 'help' for details")
        key = input()
        if key == "help":
            print('''LOWER - lowercase text
                  IS_LOWER - if a token is in lowercase
                  LIKE_NUM - if a token is a number
                  IS_PUNCT - if a token is a punctuation
                  IS_ALPHA - if a token consists of alphabet characters
                  POS - coarse-grained part of speech of a token
                  TAG - fine-grained part of speech of a token
                  SHAPE - formal structure of a word: letters are used as "X" and "x", digits - as "d"
                  HEAD - the syntactic parent of a token
                  LEMMA - word in base form
                  LENGTH - how many symbols are used in token
                  ENT_TYPE - type of a named entity''')
            key = input("Configure key.\n")
        
        value = input("Enter a requirement to the key. Please note that boolean key makes string value convert to either True or False. Leave entry empty to get False.\n")
        if key in ["IS_LOWER", "LIKE_NUM", "IS_PUNCT"]:
            value = bool(value)
        if key in ["LENGTH"]:
            value = int(value)
        dic[key] = value
        pattern.append(dic)
    matcher.add("CustomFinder", [pattern])
    concordances = matcher(test_doc)
    for match_id, start, end in concordances:
        print(test_doc[start:end])
if "match" in decisions:
    match(test_doc)

def compare_tokens(test_doc):
    option = input("Choose a way to obtain tokens: '1' if to type manually, '2' to get index from the text\n")
    if option == "1":
        token1 = nlp(input("enter token 1\n"))
        token2 = nlp(input("enter token 2\n"))
        print(token1.similarity(token2))
    elif option == "2":
        pos1 = int(input("enter index of token 1\n"))
        for token in test_doc:
            if token.i == pos1:
                token1 = token
                break
        pos2 = int(input("enter index of token 2\n"))
        for token in test_doc:
            if token.i == pos2:
                token2 = token
                break
        print(token1.text, token2.text, token1.similarity(token2))
if "compare tokens" in decisions:
    compare_tokens(test_doc)

def phrase_match(test_doc):
    from spacy.matcher import PhraseMatcher
    phm = PhraseMatcher(nlp.vocab)
    phrases = []
    n = int(input("How many phrases are to be engaged?"))
    for i in range(n):
        phrases.append(input(f"Enter phrase {i+1}\n"))
    patterns = [nlp(phrase) for phrase in phrases]
    phm.add("Custom Phrase Matcher", None, *patterns)
    phrasematch = phm(test_doc)
    for match_id, start, finish in phrasematch:
        print(test_doc[start:finish].text, f"on indices {start} - {finish}")
if "phrase match" in decisions:
    phrase_match(test_doc)


