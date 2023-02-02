import random
import time
start_time = time.time()
elementwhereweareusecounter3rd=[]

ultras=['1','6','9','11','14','18','21','30']
rares=['2','10','15','16','22','25','27']

buster=[]
list7=[]

#1 дисплей карт = 24 бустера, 2 ультры будет на дисплей

#генерирую 6 обычных карт
def openusually6():
    usually=['3','4','5','7','8','12','13','17','19','20','23','24','26','28','29']
    #all=ultras+rares+usually
    #len(all) проверка на корректность = 30 что все карточки из сэта распределены по спискам
    for i in range(6):    
        random_index = random.randint(0, len(usually) - 1)
        c=(usually[random_index])
        usually.remove(usually[random_index])#здесь оставляю remove чтобы в рамках одного бустера не повторялись частые карты, чтобы было красиво
        buster.append(c)

        
        
        
#создаю функцию генерации ультра карт для добавления в массив
def open7ultras():
    random_index = random.randint(0, len(ultras) - 1)
    a=ultras[random_index]
    elementwhereweareusecounter3rd.append(a)
    ultras.remove(ultras[random_index]) #здесь remove можно потому что ультра карт меньше намного чем элементов и ошибки не будет
    list7.append(a)
     

#создаю функцию, которая генерирует пару ультр для дисплея
def generatingultrasforbox():
    for i in range(2):
        open7ultras()
                

#создаю функцию генерации редких карт для добавления в массив 
def open7rares():
    random_index = random.randint(0, len(rares) - 1)
    a=rares[random_index]
    #rares.remove(rares[random_index]) редких карт меньше чем 22 поэтому пусть повторяются
    list7.append(a)

#создаю функцию, которая генерирует 22 оставшиеся редкие карты для дисплея и добавляет их в массив
def generatingraresforbox():
    for i in range(22):
        open7rares()

#функция генерации 7-ой карты для бустера
def open7card():
    random_index = random.randint(0, len(list7) - 1)
    b=list7[random_index]
    list7.remove(list7[random_index]) 
    buster.append(b)
   

#открытие бустера. генерация 6 карт и 7 карты
def openbuster():
    openusually6()
    open7card()
    

#генерация дисплея и отображение списка id карт дисплея
def opendisplay():
    generatingultrasforbox()
    generatingraresforbox()
    for i in range(24):
        openbuster()
        print(buster)
        buster.clear()
        
    
opendisplay()
print("ultras in it ", elementwhereweareusecounter3rd)
#print("--- %s seconds ---" % (time.time() - start_time))
