from void_scribe import MarkovGenerator
import pandas as pd
import random

import os
this_dir, this_filename = os.path.split(__file__)
default_path = this_dir + r"\data\names.csv"

def load(filepath="names.csv"):
    df = pd.read_csv(
        filepath,
        # sep=",",
        engine="python",
        encoding="latin1",
        # index_col=0
        )
    # df.info()
    # print(df)
    return df

__df__ = load(default_path)

def parse(parsee="names example"):
    ret = parsee.split(' ')
    # print(ret)
    return ret

def listGeneratedNames(repeatCount = 10):
    # for item in df.examples:
    #     print(parse(item))
    generatedContent = []
    # print(df.values[0][0])
    for i in range(len(__df__)):
        # print(df.values[i][0])
        for j in range(repeatCount):
            txt = parse(__df__.values[i][1])
            print(txt)
            generatedContent.append([__df__.values[i][0], MarkovGenerator.generate(txt, order = 3)])
        # print()
    
    # txt = parse(names['test'])
    # MarkovGenerator(txt, order=2)
    for item in generatedContent:
        print(item)

def getNames(
        Name_Type = 'americanForenames', 
        amount = 3, 
        seed = None):
    random.seed(seed)
    ret = []
    for i in range(amount):
        potentials = __df__[__df__['nameType'] == Name_Type].examples.values[0]
        potentials = parse(potentials)
        ret.append(random.choice(potentials))
    return ret

def MarkovName(
        Name_Type = 'americanForenames', 
        amount = 3, 
        order = 3, 
        maxlength = 10, 
        seed = None):
    # print(df.values)
    txt = parse(__df__[__df__['nameType'] == Name_Type].examples.values[0])
    ret = (MarkovGenerator.generate(txt, amount, order, maxlength, seed))
    # print(ret)
    return ret

def getNameTypes():
    return __df__.nameType
    

# listGeneratedNames(3)
# MarkovName(Name_Type = 'werewolfForenames')
