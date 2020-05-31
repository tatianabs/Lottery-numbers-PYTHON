from random import randint
from time import sleep

lista=list()
sorteados=list()
print('-=' *30)
print('PLAYING LOTTERY')
print('-='*30)
qt=int(input('HOW MANY NUMBERS DO YOU WANT TO BET?: '))
print()
print('-=' * 3,f'DRAWING {qt} PLAYS','-=' *3)
sleep(1)
tot=1
while tot<=qt:
    cont=0
    while True:
        num=randint(1,60)
        if num not in sorteados:
          sorteados.append(num)
          cont+=1
        if cont>=6:
             break
    sorteados.sort()
    lista.append(sorteados[:])
    sorteados.clear()
    tot+=1
for c,l in enumerate(lista):
 sleep(1)
 print(f'PLAY {c+1}: {l}')
print('*'*5,f'GOOD LUCK!','*'*5)