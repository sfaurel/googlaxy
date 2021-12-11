import re

from .Roman import Roman
from ..models import Items, Numerals
from django.core import serializers


class GalacticInterpreter:
    items = {}
    values = {}
    currency = "Credits"

    @staticmethod
    def readValue(entry):
        value, symbol = re.search('(\w*) is ([IVXLCDM])', entry).groups()
        numeral = Numerals(name=value, roman=symbol)
        numeral.save()
        return f"{value} stored as: {symbol}"

    @classmethod
    def readItem(cls, entry):
        galactic = []
        name = ""
        price = 0
        count = 1
        values = Numerals.objects.all().values_list('name', flat=True)
        for word in entry.split():
            if word in values:
                galactic.append(word)
            else:
                name = word
                break
        count = Roman.roman2dec(cls.galactic2roman(galactic))
        price = int(re.search(f'(\d*) {cls.currency}', entry).group(1))
        item = Items(name=name, price=price/count)
        item.save()
        return f"{name} stored whith price: {price/count}"

    @classmethod
    def getPrice(cls, entry):
        galactic = []
        item = ""
        value = 0
        values = Numerals.objects.all().values_list('name', flat=True)
        items = Items.objects.all().values_list('name', flat=True)
        for word in entry.split():
            if word in values:
                galactic.append(word)
            elif word in items:
                item = word
        roman = cls.galactic2roman(galactic)
        value = Roman.roman2dec(roman)
        if value:
            price = value * Items.objects.filter(name=item).first().price
            return f"{' '.join(galactic)} {item} is {price} {cls.currency}"
        else:
            return "galactic number can't be translated"

    @staticmethod
    def galactic2roman(galactic):
        roman = []
        for key in galactic:
            roman += Numerals.objects.filter(name=key).first().roman
        return roman

    @classmethod
    def interpretateEntry(cls, entry):
        values = Numerals.objects.all()
        if "?" in entry:
            if cls.currency in entry:
                return cls.getPrice(entry)
            else:
                match = re.search("how much is ([a-zA-Z\s]*)?", entry)
                if match:
                    galactic = match.group(1)
                    roman = cls.galactic2roman(galactic.split())
                    value = Roman.roman2dec(roman)
                    return f"{galactic} is {value}"
                else:
                    return "Some error ocurred, please check the sentense."
        for symbol in Roman.numerals:
            if f"is {symbol}" in entry:
                return cls.readValue(entry)
        for value in values:
            if value.name in entry:
                return cls.readItem(entry)
        return "Some error ocurred, please check the sentense."
