#pip install requests
#pip install certifi
from random import *
import requests
#import certifi

def isAlpha(string):
    s = string
    return (len(s) == 1) and (s.lower() >= "a" and s.lower() <= "z")

def only_letters(string):
    if string == None:
        return string
    else:
        return all(isAlpha(letter) for letter in string)

def has_letters(string):
    if string == None:
        return False
    else:
        count=0
        for letter in string:
            if isAlpha(letter): count = count + 1
        return count > 0

def purify_alpha(string, min_len = 2):
    if len(string) < min_len:
        return string
    else:
#        print(string)
#        print(f"{string[0]} {string[len(string)-1]}")
        if isAlpha(string[0]) and isAlpha(string[len(string)-1]):
#            print(string)
            return string
        elif isAlpha(string[0]):
            print(string)
            print(f"> {string[0]} {string[len(string)-1]}")
            print(string[0:len(string)-1])
            print(purify_alpha(string[0:len(string)-1], min_len))
            return purify_alpha(string[0:len(string)-1], min_len)
        elif isAlpha(string[len(string)-1]):
            print(string)
            print(f"< {string[0]} {string[len(string)-1]}")
            print(string[1:len(string)-1])
            print(purify_alpha(string[1:len(string)-1], min_len))
            return purify_alpha(string[1:len(string)-1], min_len)

try:
    print('Checking connection to Github...')
    test = requests.get('https://api.github.com')
    print('Connection to Github OK.')
except requests.exceptions.SSLError as err:
    print('SSL Error. Adding custom certs to Certifi store...')
    cafile = certifi.where()
    with open('certicate.pem', 'rb') as infile:
        customca = infile.read()
    with open(cafile, 'ab') as outfile:
        outfile.write(customca)
    print('That might have worked.')

kjv_scriptures_file = "https://raw.githubusercontent.com/beandog/lds-scriptures/master/text/kjv-scriptures.txt"
lds_scriptures_file = "https://raw.githubusercontent.com/beandog/lds-scriptures/master/text/lds-scriptures.txt"
kjv_scriptures = requests.get(url=kjv_scriptures_file, params={"owner":"beandog", "repo":"lds-scriptures", "path":"text/kjv-scriptures.txt", "ref":"master", "accept":"application/text"}, stream = True)
lds_scriptures = requests.get(url=lds_scriptures_file, params={"owner":"beandog", "repo":"lds-scriptures", "path":"text/lds-scriptures.txt", "ref":"master", "accept":"application/text"}, stream = True)
scriptures = f"{kjv_scriptures.text}\n{lds_scriptures.text}"
lines = scriptures.split("\n")
words = {}
min_len = 6
line_count=1
for line in lines:
    line_words = line.split(" ")
    for word in line_words:
        word = purify_alpha(word, min_len)
        if only_letters(word) and (len(word) >= min_len) and not(word in words.keys()):
            words[word] = True
        elif has_letters(word) and (len(word) >= min_len) and not(word in words.keys()):
            pass
#            print(word)
#    print(f"{line_count}  {line}")
#    line_count = line_count + 1
#print(words.keys())
#print(len(words.keys()))
r = Random()
r.seed
list = [*words.keys()]

for counter in range(5):
    print(r.choice(list))

print(purify_alpha("surrounded,"))
print(purify_alpha("-surrounded"))
print(purify_alpha("-surrounded,"))
