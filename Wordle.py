import random as rnad
def start():
    m=[]
    print('''rules:-
     " "means neither correct letter nor correct position
     "{}"means correct letter but not correct position
     "[]"means correct letter and correct position''')
    for j in range(7):
        m.append(['_']*(len(d)))
    return m

def fill(m):
    for i in range(len(e)):
        for j in range(len(d)):
            if e[i]==d[i]:
                m[a][i]=[e[i]]
            elif e[i] in d:
                m[a][i]={e[i]}
            else:
                m[a][i]=(e[i])
    return m

def status(m):
    if e==d:
        return 'You Won'
    elif a==7:
        print(f'the word was: {d}')
        return 'Game Over'
    return 'continue'
        
a=0
dic=words= ['rainbow', 'computer', 'science', 'programming','python', 'mathematics', 'player', 'condition','reverse', 'water', 'board','fuck','nigga','nigger','bitch']
d=(rnad.choice(dic)).lower()
m=start()
for i in range(7):
    print(m[i])
print()
while True:
    e=input('Enter your guess: ')
    if len(e)==len(d):
        f=fill(m)
        for i in range(7):
            print(f[i])
        print()
        a+=1
        print(status(m))
    if status(m)=='Game Over' or status(m)=='You Won':
        break
    else:
        continue