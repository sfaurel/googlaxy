class Roman:
    symbols = ["I", "V", "X", "L", "C", "D", "M"]
    values = [1, 5, 10, 50, 100, 500, 1000]
    numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

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
            # check if key is summable
            if symbolPosition % 2 == 0:
                # if not last symbol check if can be substracted
                if index + 1 < len(roman) and \
                   cls.numerals[key] < cls.numerals[roman[index+1]] and \
                   cls.numerals[key] <= cls.numerals[roman[index+1]]*10:
                    if lastSummableSymbol == key:
                        return None
                    else:
                        lastValue = -cls.numerals[key]
                        dec += lastValue
                elif index != 0 and \
                     cls.numerals[key] > lastValue and lastValue >= 0:
                    return None
                else:
                    if key == lastSummableSymbol:
                        if summableCount >= 3 and lastValue > 0:
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
            elif index != 0 and \
                 cls.numerals[key] >= lastValue and \
                 lastValue >= 0:
                return None
            else:
                summableCount = 0
                lastSummableSymbol = ""
                lastValue = cls.numerals[key]
                dec += lastValue
        return dec
