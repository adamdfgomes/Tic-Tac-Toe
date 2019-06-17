#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def clear():
    from IPython.display import clear_output
    clear_output()

def board(i):
    print('   |   |   \n {} | {} | {}  \n   |   |   \n-----------\n   |   |   \n {} | {} | {} \n   |   |   \n-----------\n   |   |   \n {} | {} | {} \n   |   |   '.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))

def startup():
    i=['1','2','3','4','5','6','7','8','9']
    P1=input('Would you like "X" or "O" to go first?\n').upper()
    while P1!='X' and P1!='O':
        P1=input('Please enter ONLY "X" or "O".\n').upper()
    print("Player 1 goes first as {}'s.".format(P1))
    if P1=='X':
        P2='O'
    else:
        P2='X'
    return (P1,P2,i)
        

def go(P,i,Px,x):
    here=input('Where would {} like to play?\n'.format(Px))
    while here not in ['1','2','3','4','5','6','7','8','9']:
        here=input('Please enter a number 1-9.\n'.format(Px))
    clear()
    ind=int(here)
    if i[(ind-1)]==' ':
        i[(ind-1)]=P
    else:
        x=x-1
        print('There is already a marker in this place, please pick another place to play.')
    return (i,x)

def status(i):
    x=combos(i)
    if x == 'win':
        return x
    else:
        if ' ' in i:
            return x
        else:
            return 'Draw.'

def combos(i):
    for n in ['012','036','258','678','345','048','246','147']:
        x=wins(i,n[0],n[1],n[2])
        if x == 'win':
            return x
    return x

def wins(i,a,b,c):
    a=int(a)
    b=int(b)
    c=int(c)
    if i[a]==i[b]==i[c]=='X' or i[a]==i[b]==i[c]=='O':
        return 'win'
    #if i[0]==i[1]==i[2] or i[0]==i[3]==i[6] or i[2]==i[5]==i[8] or i[6]==i[7]==i[8] or i[3]==i[4]==i[5] or i[0]==i[4]==i[8] or i[2]==i[4]==i[6]
    else:    
        return 'Keep playing'

def altern(P1,P2,i):
    res = 'Keep playing'
    x=0
    while res=='Keep playing':
        if x%2==0:
            g=go(P1,i,'P1',x)
            board(g[0])
            res=status(g[0])
            P='P1'
            x=g[1]
            x=x+1
        else:
            g=go(P2,i,'P2',x)
            board(g[0])
            res=status(g[0])
            P='P2'
            x=g[1]
            x=x+1
    return (res,P)
        

def replay():
    x=input('Want to play again?: Enter "Yes".\nWant to end the game?: Press enter.\n').upper()
    while x!='YES' and x!='':
        x=input('Please enter "Yes" or press enter to end.\n').upper()
    if x=='YES':
        r=1
        return r
    else:
        r=0
        return r

def tic_tac_toe():
    r=1
    while r==1:
        x=startup()
        board(x[2])
        print('Enter the corresponding number above to place in the grid.')
        i=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
        res=altern(x[0],x[1],i)
        if res[0]=='Draw.':
            print(res[0])
        else:
            print(res[1]+' '+res[0]+'s.')
        r=replay()
    return print('Thanks for playing.')
    
tic_tac_toe()