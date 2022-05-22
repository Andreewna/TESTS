#Привет,это проверка имы внесли первые изменения
#вносим вторые изменения и делаем branch  с этим изменением,потому что я так хочу
ark=[1,2,3,4,5,6,7,8,9]
r=0
def prnt_desk(): 
    for i in range(0,3):
        print (ark[0+i*3],"|",ark[1+i*3],"|",ark[2+i*3])
def win():
    if ark[0]==ark[3]==ark[6]:
        return ark[0]
    elif ark[1]==ark[4]==ark[7]:     
        return ark[1]
    elif ark[2]==ark[5]==ark[8]:
        return ark[2]
    elif ark[0]==ark[1]==ark[2]:
        return ark[0]
    elif ark[3]==ark[4]==ark[5]:
        return ark[3]
    elif ark[6]==ark[7]==ark[8]:
        return ark[6]
    elif ark[0]==ark[4]==ark[8]:
        return ark[0]
    elif ark[2]==ark[4]==ark[6]:
        return ark[2]
def funkO():
    prnt_desk()
    z="o"
    print("Теперь Ваш ход игрок - O")
    v=int(input( "выбери число:"))
    ark[v-1]=z
    if win()=="o":
        print(win())
    else:
        pass
while r<=4:
    prnt_desk() 
    h="x"
    print("Ваш ход игрок - Х")
    p= int(input( "выбери число:"))
    ark[p-1]=h  
    if win()== "x" or win()=="o":
        print(win())
        break
    else:
        funkO() 
    r+=2
    
