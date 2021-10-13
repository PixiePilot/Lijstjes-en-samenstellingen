




def pop(list1,list2:int):
    list1
    list2
    listThree = list1.copy()
    listFour = list2.copy()


    print('Add list')
    #for x in range(6):
    times = len(list1)

    while times > 0:
        times = times + 1
        a = listThree.pop(0) #listOne = [1,2,3,4,5,6,7,8,9,10]
        b = listFour.pop(0) #listTwo = [2,4,6,8,10,12,14,16,18,20]
        #pop1 = listOne.pop(0) #listOne = [1,2,3,4,5,6,7,8,9,10]
        #pop2 = listTwo.pop(0)#listTwo = [2,4,6,8,10,12,14,16,18,20]
        #pop1 = pop1 + pop2
        pop1 = a+b
        print(a, '+' , b , '=' , pop1)
    return 
listOne = [1,2,3,4,5,6,7,8,9,10]
listTwo = [2,4,6,8,10,12,14,16,18,20]
try:
    pop(listOne,listTwo)
except:
    print('no u')



def pop2(list1,list2:int):
    list1
    list2
    listThree = list1.copy()
    listFour = list2.copy()


    print('Add list')
    times = len(list1)

    while times > 0:
        times = times + 1
        a = listThree.pop(0) #listOne = [1,2,3,4,5,6,7,8,9,10]
        b = listFour.pop(0) #listTwo = [2,4,6,8,10,12,14,16,18,20]
        pop1 = a-b
        print(a, '-' , b , '=' , pop1)
    return 

listOne = [1,2,3,4,5,6,7,8,9,10]
listTwo = [2,4,6,8,10,12,14,16,18,20]
try:
    pop2(listOne,listTwo)
except:
    print('no u')

def pop3(list1,list2:int):
    list1
    list2
    listThree = list1.copy()
    listFour = list2.copy()


    print('Add list')
    times = len(list1)

    while times > 0:
        times = times + 1
        a = listThree.pop(0) #listOne = [1,2,3,4,5,6,7,8,9,10]
        b = listFour.pop(0) #listTwo = [2,4,6,8,10,12,14,16,18,20]
        pop1 = a*b
        print(a, '*' , b , '=' , pop1)
    return 

listOne = [1,2,3,4,5,6,7,8,9,10]
listTwo = [2,4,6,8,10,12,14,16,18,20]
try:
    pop3(listOne,listTwo)
except:
    print('no u')

def pop4(list1,list2:int):
    list1
    list2
    listThree = list1.copy()
    listFour = list2.copy()


    print('Add list')
    times = len(list1)

    while times > 0:
        times = times + 1
        a = listThree.pop(0) #listOne = [1,2,3,4,5,6,7,8,9,10]
        b = listFour.pop(0) #listTwo = [2,4,6,8,10,12,14,16,18,20]
        pop1 = a/b
        print(a, '/' , b , '=' , pop1)
    return 

listOne = [1,2,3,4,5,6,7,8,9,10]
listTwo = [2,4,6,8,10,12,14,16,18,20]
try:
    pop4(listOne,listTwo)
except:
    print('no u')