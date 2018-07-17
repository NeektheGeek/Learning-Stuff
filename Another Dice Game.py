"""
This game is first created by Ayastar. I've shortened it a bit. The link of Ayastar's code is provided in the comment section.
"""
import random
num=[random.randint(1,6) for i in range(4)]
you=num[0]+num[1]
bot=num[2]+num[3]
ups=chr(201)+chr(205)*11+chr(187)
l,O=chr(186),chr(254)
_O_=l + ' '*6 + O + ' '*5 + l
O__=l + ' '*2 + O + ' '*9 + l
__O=l + ' '*9 + O + ' '*2 + l
O_O=l + ' '*2 + O + ' '*6 + O + ' '*2 + l
dwn=chr(200)+chr(205)*11+chr(188)
___=l + ' '*12 + l

dice={
    1:[ups,___,___,_O_,___,___,dwn],
    2:[ups,O__,___,___,___,__O,dwn],
    3:[ups,__O,___,_O_,___,O__,dwn],
    4:[ups,O_O,___,___,___,O_O,dwn],
    5:[ups,O_O,___,_O_,___,O_O,dwn],
    6:[ups,O_O,___,O_O,___,O_O,dwn]}

print(*dice[num[0]],*dice[num[1]], sep='\n')
print('You have Rolled, %d + %d = %d'%(num[0],num[1],you))
print(*dice[num[2]],*dice[num[3]], sep='\n')
print('Bot have Rolled, %d + %d = %d'%(num[2],num[3],bot))
print(end='\nRESULT: ')
if you>bot:
    print('Congratulatons! You have WON the Game.')
elif you<bot:
    print('Oops! You have LOST the Game. Try Again...')
else:
    print('Aah! It\'s a TIE. Play Again...')