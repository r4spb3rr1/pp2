import re

first_task = re.compile(r"ab*")
print(first_task.search("sdfsdfsrtasbabafds"))


second_task = re.compile(r"ab{2,3}")
print(second_task.search("hgfhfghgsabbbbasfadfader"))

third_task = re.compile(r"[a-z]+\_")
print(third_task.findall("nfldgdjfgh_ dfsfdsf_"))


forth_task = re.compile(r"[A-Z]{1}[a-z]+")
print(forth_task.findall("Abcdef Zxcvbbn Yayayayaay"))


fifth_task = re.compile(r"a.+b\Z")
print(fifth_task.search("ZXCZSSDfdfdhdtaUhnKItdbdFDfefrgfd"))


sixth_task = re.compile(r"[ ,.]")
text = "gfdjf,fhdsjh..fdskjf fjhgerj,. fds"
print(sixth_task.sub(":", text))


def snakeToCamel(text):
    camelCase=""
    pattern = re.compile(r"[_]")
    words=pattern.split(text)
    for i, word in enumerate(words):
        if i != 0:
            camelCase+=word.capitalize()
        else: 
            camelCase += word
    return camelCase
print(snakeToCamel("hello_world_wordle"))


def modify(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:  
            res += " " + word
        else:
            res += word
    return res
print(modify("OneTwoThree"))
    


def spaces(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:
            res += " " + word
        else:
            res += word
    return res
print(spaces("HelloWordlOneMoreTime"))



def camel_to_snake(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i == 0:
            res += word.casefold()
        else:
            res += "_" + word.casefold()
    return res


print(camel_to_snake("SnakeCaseVar"))






