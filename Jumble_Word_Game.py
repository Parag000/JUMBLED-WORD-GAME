def jumble(listnum,word):#USED TO JUMBLE THE LETTERS OF THE WORD
    jumbledword=[]
    for n in range(len(listnum)):
        jumbledword.append(word[listnum[n]])
    output="".join(str(i) for i in jumbledword)
    return output

import random

def generateRandomIndexList(word):#THIS WILL RANDOMLY JUMBLE THE LETTERS IN ANY ORDER
    word_length=len(word)
    index_list=[]
    while len(index_list)<word_length:
        r=random.randint(0,word_length-1)
        if r not in index_list:
            index_list.append(r)
    return index_list

print("WELCOME TO PARAG'S JUMBLE GAME")
print("THERE ARE 10 QUESTIONS")
print("RULES OF THIS GAME ARE \n PLAYER IS AWARDED 1 POINT FOR EVERY CORRECT ANSWER \n PLAYER IS AWARDED -1 POINT FOR EVERY WRONG ANSWER")
usedWords=[]
point=0

list=['horse','arrow','hippo','happy','water','glass','apple','peach','black','white','car','bike','jet','yellow','green','orange','sad','dog','blue','lion','tiger','table','laptop','envelope','strange','angry']
for k in range(10):
    r=random.randint(0,len(list)-1)#THIS WILL CHOOSE ANY WORD FROM THE LIST
    while r in usedWords:
        r=random.randint(0,len(list)-1)
    usedWords.append(r)
    selected_word=list[r]

    il=generateRandomIndexList(selected_word)

    res2=jumble(listnum=il,word=selected_word)#GENERATES RANDOM INDEX FOR THE SELECTED WORD
    print("\nJUMBLED WORD IS",res2)

    correctword=input("ENTER CORRECT WORD\n")
    correctword=correctword.lower()
    if correctword==selected_word:
        point+=1
        print("YOU ARE RIGHT\n")
    else:
        print("YOU ARE WRONG")
        print("CORRECT ANSWER IS",selected_word)
        point-=1
print("\n\nYOUR TOTAL POINTS ARE\t",point)
