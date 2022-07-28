###
# Class CmdProcessor is in charge of implementing all commands supported by WordleHelp
from typing import Dict
from WordChecker import WordChecker
from Scraper import Scraper


class CmdProcessor:
    ###
    # Class fields
    # _wordChecker: the "engine" in charge of storing and using all hints
    #               used for verifying words from the database

    ###
    # Class constructor
    def __init__(self):
        self._wordChecker = WordChecker()
        self._good = {}
        self._wrong = {}
        self._forbidden = []

    def processHelp(self):
        print("process command 'help'")

    def processAdd(self, args = None, dict : Dict = {}):
        print("Processing command 'add'...")
        input = args[4:]
        textread = Scraper(input)
        words = textread._text.split()
        length = len(dict)
        for x in words:
            origlength = len(x)
            word = ''.join(ch for ch in x if ch.isalpha() and ch != "'") 
            word = word.lower()
            if len(word)==5 and origlength == 5:
                if word in dict: dict[word]=dict[word]+1
                else: dict[word]=1
        print("Added {count} words to dictionary.".format(count=len(dict)-length))
        return dict

    def processMatch(self, args = None, dict : Dict = {}):
        val=0
        input = args[6:]
        for i in range(0, len(input)-1):
            if input[i].isalpha() == True:
                if i!=0 and input[i-1]=='~': 
                    self._wrong[input[i]].append(i-val)
                elif i!=0 and input[i-1]=='!': 
                    self._good[i-val]=input[i]
                else: self._forbidden.append(input[i])
            else: val=val+1
        for word, appearence in dict.items():
            ok = True
            counter = 0
            for pos, letter in self._good.items():
                if word[pos] != letter:
                    ok = False
                    break
            if ok == False: continue
            for letter, positions in self._wrong.items():
                for pos in positions:
                    if(word[pos]==letter):
                        ok = False
                        break
                if ok == False: break
            if ok == False: continue
            for letter in self._forbidden:
                if word.find(letter)!=-1: 
                    ok = False
                    break
            if ok == True: 
                print(word)
                counter = counter + 1
        print("Found ",counter," good matches.")
    
    def processReset(self, args = None):
        print("Process command 'reset'")

    def processStats(self, args = None):
        print("Process command 'stats'")

    def processConfig(self, args = None):
        print("Process command 'config'")

###
# CmdProcessor test code
if __name__ == "__main__":
    cmdP = CmdProcessor()
    cmdP.processHelp()