# add 3 random letters to a word before andafter:
"""import random
lists=[]
liste=[]
for i in range(0,3):
    x=random.choice("abcdefghijklmnopqrstuvwxyz")
    lists.append(x)
    results="".join(lists)
print(results)
for i in range(0,3):
    x=random.choice("abcdefghijklmnopqrstuvwxyz")
    liste.append(x)
    resulte="".join(liste)
print(resulte)
user=str(input("enter "))
final=results+user+resulte
print(final)"""

# move first character to last
"""x="hello"
word=x[1:]+x[0]
print(word)"""
# random + move character
"""import random

lists = []
liste = []
x = "hello"
word = x[1:] + x[0]
for i in range(0, 3):
    x = random.choice("abcdefghijklmnopqrstuvwxyz")
    lists.append(x)
    results = "".join(lists)
for i in range(0, 3):
    y = random.choice("abcdefghijklmnopqrstuvwxyz")
    liste.append(y)
    resulte = "".join(liste)
final=results+word+resulte
print(final)
"""
# reverse
"""import random
lists = []
liste = []
x = "he"
word = x[::-1]
print(word)"""
# Mini Program  — Condition Test
"""word=str(input("enter word"))
if len(word)> 3:
    print("larger than 3")
else:
    print("shorter")"""
# Final Encoder Logic
"""import random

liste = []
lists = []


word = str(input("enter the word"))

if len(word) <= 3:
    new_word = word[::-1]
    print(new_word)
else:
    for i in range(0, 3):
        x = random.choice("abcdefghijklmnopqrstuvwxyz")
        lists.append(x)
        results = "".join(lists)
    for i in range(0, 3):
        y = random.choice("abcdefghijklmnopqrstuvwxyz")
        liste.append(y)
        resulte = "".join(liste)
    rand = word[1:] + word[0]
    final = results + rand + resulte

    print(final)
"""
# split sentence
"""user=str(input("enter sentence"))
words=user.split()
for word in words:
    print(len(word))"""
# mini project
import random

user = str(input("enter sentence"))
words = user.split()
encoded_words=[]

for i in words:
    word = i
    if len(word) <= 3:
        word = word[::-1]
        encoded_words.append(word)
        
        
    else:
        word=word[1:]+word[0]
        lists=[]
        liste=[]
        for k in range(0, 3):
            x = random.choice("abcdefghijklmnopqrstuvwxyz")
            lists.append(x)
            results = "".join(lists)
        for w in range(0, 3):
            y = random.choice("abcdefghijklmnopqrstuvwxyz")
            liste.append(y)
        resulte = "".join(liste)
        final=results+word+resulte
        encoded_words.append(final)
        
        
    
print("   ".join(encoded_words))
        
