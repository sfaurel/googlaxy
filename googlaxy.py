#!/bin/python3
import re
class Roman:
    symbols = ["I", "V", "X", "L", "C", "D", "M"]
    values = [1, 5, 10, 50, 100, 500, 1000]
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    @classmethod
    def dec2roman(cls, dec):
        pass

    @classmethod
    def roman2dec(cls, roman):
        lastSummableSymbol = ""
        summableCount = 0
        lastValue = 0
        dec = 0
        for index, key in enumerate(roman):
            symbolPosition = cls.symbols.index(key)
            #check if key is summable
            if symbolPosition % 2 == 0: 
                #if not last symbol check if can be substracted
                if index + 1 < len(roman) and \
                   cls.numerals[key] < cls.numerals[roman[index+1]] and \
                   cls.numerals[key] <= cls.numerals[roman[index+1]]*10:
                    if lastSummableSymbol == key:
                        print(key,roman,index,dec,"A")
                        return None
                    else:
                        lastValue = -cls.numerals[key]
                        dec += lastValue
                elif index != 0 and cls.numerals[key] > lastValue and lastValue >= 0:
                    print(key,roman,index,dec,"A")
                    return None
                else:
                    if key == lastSummableSymbol:
                        if summableCount >= 3 and lastValue > 0:
                            print(key,roman,index,dec,"B")
                            return None
                        else:
                            summableCount += 1
                            lastValue = cls.numerals[key]
                            dec += lastValue
                    else:
                        summableCount = 1
                        lastSummableSymbol = key
                        lastValue = cls.numerals[key]
                        dec += lastValue
            elif index != 0 and cls.numerals[key] >= lastValue and lastValue >= 0:
                print(key,roman,index,dec,"C")
                return None
            else:
                summableCount = 0
                lastSummableSymbol = ""
                lastValue = cls.numerals[key]
                dec += lastValue
        return dec

class GalacticInterpreter:
    items = {}
    values = {}
    currency = "Credits"

    def readValue(self, entry):
        # print(f"get value in: \"{entry}\"")
        value, symbol = re.search('(\w*) is ([IVXLCDM])',entry).groups()
        self.values[value] = symbol

    
    def readItem(self, entry):
        # print(f"item in: \"{entry}\"")
        galactic = []
        item = ""
        price = 0
        for word in entry.split():
            if word in self.values:
                galactic.append(word)
            else: 
                item = word
                break
        price = int(re.search(f'(\d*) {self.currency}',entry).group(1))  
        self.items[item] = price/Roman.roman2dec(self.galactic2roman(galactic))


    
    def getPrice(self, entry):
        # print(f"get price in: \"{entry}\"")
        galactic = []
        item = ""
        value = 0
        
        for word in entry.split():
            if word in self.values:
                galactic.append(word)
            elif word in self.items: 
                item = word
        roman = self.galactic2roman(galactic)
        value = Roman.roman2dec(roman)
        if value:
            print(f"{' '.join(galactic)} {item} is {int(value*self.items[item])} {self.currency}")
        else:
            print("galactic number can't be translated")

    def galactic2roman(self, galactic):
        roman = []
        for key in galactic:
            roman += self.values[key]
        return roman
    
    def interpretateFile(self, filename):
        with open(filename) as f:
            content = f.readlines()
            for entry in content:
                symbolEntry = False
                itemEntry = False
                if "?" in entry:
                    if self.currency in entry:
                        self.getPrice(entry)
                    else:
                        match = re.search("how much is ([a-zA-Z\s]*)?",entry)
                        if match:
                            galactic = match.group(1)
                            roman = self.galactic2roman(galactic.split())
                            value = Roman.roman2dec(roman)
                            print(f"{galactic} is {value}")
                        else:
                            print("I have no idea what you are talking about")
                    continue
                for symbol in Roman.numerals:
                    if f"is {symbol}" in entry:
                        self.readValue(entry)
                        symbolEntry = True
                        break
                if symbolEntry:
                    continue
                for value in self.values:
                    if value in entry:
                        self.readItem(entry)
                        itemEntry = True
                        break
                if itemEntry:
                    continue
                print("I have no idea what you are talking about")


