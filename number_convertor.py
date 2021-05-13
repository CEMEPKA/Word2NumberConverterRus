import re


class NumberConvertor:
    def __init__(self) -> None:
        self.__numeric_regulars = {r"\b(н(оль|уль|оля|уля|олями|улями))\b": 0,
                                   r"\b(од(ин|ного|ному|ним|ной|ною|них|ними|ни|на|но|ну))\b": 1,
                                   r"\b(дв(ух|умя|ум|а))\b": 2,
                                   r"\b(тр(ех|емя|ем|и))\b": 3,
                                   r"\b(четыр(ех|ем|ьмя|е))\b": 4,
                                   r"\b(пят(и|ью|ь))": 5,
                                   r"\b(шест(и|ью|ь))": 6,
                                   r"\b(сем(и|ью|ь))\b": 7,
                                   r"\b(вос(емью|ьми|емь))\b": 8,
                                   r"\b(девят(и|ью|ь))\b": 9,
                                   r"\b(десят(и|ью|ь))\b": 10,
                                   r"\b(одиннадцат(и|ью|ь))\b": 11,
                                   r"\b(двенадцат(и|ью|ь))\b": 12,
                                   r"\b(тринадцат(и|ью|ь))\b": 13,
                                   r"\b(четырнадцат(и|ью|ь))\b": 14,
                                   r"\b(пятнадцат(и|ью|ь))\b": 15,
                                   r"\b(шестнадцат(и|ью|ь))\b": 16,
                                   r"\b(семнадцат(и|ью|ь))\b": 17,
                                   r"\b(восемнадцат(и|ью|ь))\b": 18,
                                   r"\b(девятнадцат(и|ью|ь))\b": 19,
                                   r"\b(двадцат(и|ью|ь))\b": 20,
                                   r"\b(тридцат(и|ью|ь))\b": 30,
                                   r"\b(сорок(а)?)\b": 40,
                                   r"\b(пят(ьдесят|идесяти|ьюдесятью))\b": 50,
                                   r"\b(шест(ьдесят|идесяти|ьюдесятью))\b": 60,
                                   r"\b(сем(ьдесят|идесяти|ьюдесятью))\b": 70,
                                   r"\b(вос(емьдесят|ьмидесяти|ьмьюдесятью))\b": 80,
                                   r"\b(девяност(а|о))\b": 90,
                                   r"\b(ст(а|о))\b": 100,
                                   r"\b(дв(ести|ухсот|умстам|умястами|ухстах))\b": 200,
                                   r"\b(тр(иста|ёхсот|ёмстам|емястами))\b": 300,
                                   r"\b(четыр(еста|ёхсот|ёмстам|ьмястами|ёхстах))\b": 400,
                                   r"\b(пят(ьсот|исот|истам|ьюстами|истах))\b": 500,
                                   r"\b(шест(ьсот|исот|истам|ьюстами|истах))\b": 600,
                                   r"\b(сем(ьсот|исот|истам|ьюстами|истах))\b": 700,
                                   r"\b(вос(емьсот|ьмисот|ьмистам|емьсот|емьюстами|ьмистах))\b": 800,
                                   r"\b(девят(ьсот|исот|истам|ьюстами|истах))\b": 900,
                                   r"\b(тысяч(ами|ей|а|и|е|у)?)\b": 10 ** 3,
                                   r"\b(миллион(ами|а|у|ом|е|ов)?)\b": 10 ** 6,
                                   r"\b(миллиард(ами|а|у|ом|е|ов)?)\b": 10 ** 9,
                                   r"\b(триллион(ами|а|у|ом|ов)?)\b": 10 ** 12,
                                   r"\b(триллиард(ами|а|у|ом|ов)?)\b": 10 ** 15
                                   }

    # Замена прописных цифр числами
    def convert(self, text: str) -> str:
        if not text:
            return ""
        for reg in reversed(self.__numeric_regulars):
            text = re.sub(pattern=reg, repl=str(self.__numeric_regulars[reg]), string=text, flags=re.I)
        return text

    # Замена прописных цифр группированными числами
    def convert_groups(self, text: str) -> str:
        if not text:
            return ""
        for reg in reversed(self.__numeric_regulars):
            text = re.sub(pattern=reg, repl=str(self.__numeric_regulars[reg]), string=text, flags=re.I)
        matches = list(re.finditer(r"\b(\d+)\b", text))
        pattern = re.compile(r"\S")
        start = 0
        shift = 0  # Накаплеваемое смещение при замене текста цифрами
        group = 0
        is_group = False
        for i in range(len(matches)):
            if is_group:
                if group < int(matches[i].group(0)):
                    group *= int(matches[i].group(0))
                else:
                    group += int(matches[i].group(0))
            if i != len(matches) - 1:
                chars_between = "".join(
                    text[j] for j in range(matches[i].end(0) - shift, matches[i + 1].start(0) - shift))
            else:
                chars_between = None
            if chars_between and len(list(pattern.finditer(chars_between))) == 0:
                if not is_group:
                    is_group = True
                    group += int(matches[i].group(0))
                    start = matches[i].start(0) - shift
            else:
                is_group = False
                end = matches[i].end(0) - shift
                if group != 0:
                    text = text[:start] + str(group) + text[end:]
                    shift += end - start - len(str(group))
                    group = 0
        return text
