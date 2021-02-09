#3,4,5,7 max 2723
import math

def sapma_ort(dizi1,dizi2,dizi3,dizi4):
    ort = (dizi1[0]+dizi1[1]+dizi1[2]+dizi2[0]+dizi2[1]+dizi2[2]+dizi3[0]+dizi3[1]+dizi3[2]+dizi4[0]+dizi4[1])/11
    sapma_deger = math.sqrt(((dizi1[0]-ort)**2+(dizi1[1]-ort)**2+(dizi1[2]-ort)**2+(dizi2[0]-ort)**2+(dizi2[1]-ort)**2+(dizi2[2]-ort)**2+(dizi3[0]-ort)**2+(dizi3[1]-ort)**2+(dizi3[2]-ort)**2+(dizi4[0]-ort)**2+(dizi4[1]-ort)**2)/11)
    return sapma_deger,ort

def ahmet(dizi1,dizi2,dizi3,dizi4):
    kiyas = (dizi1[0]+dizi1[1]+dizi1[2])*uc_w/3+(dizi2[0]+dizi2[1]+dizi2[2])*dort_w/3+(dizi3[0]+dizi3[1]+dizi3[2])*bes_w/3+(dizi4[0]+dizi4[1])*yedi_w/2
    return kiyas

def umut_yuzde(max, deger):
    return 100*deger/max

uc_deger = [0]   #3
dort_deger = [0] #3
bes_deger = [0]  #3
yedi_deger = [0] #2

uc_w = 4*5*7
dort_w = 3*5*7
bes_w = 4*3*7
yedi_w = 4*5*3

uc_deger.pop(0)
dort_deger.pop(0)
bes_deger.pop(0)
yedi_deger.pop(0)

for i in range(3):
    deger=int(input('Uc dklik deneme netlerini giriniz: '))
    uc_deger.append(deger)
    print(uc_deger[i])
print(uc_deger)

for i in range(3):
    deger=int(input('Dort dklik deneme netlerini giriniz: '))
    dort_deger.append(deger)
    print(dort_deger[i])
print(dort_deger)

for i in range(3):
    deger=int(input('Bes dklik deneme netlerini giriniz: '))
    bes_deger.append(deger)
    print(bes_deger[i])
print(bes_deger)

for i in range(2):
    deger=int(input('Yedi dklik deneme netlerini giriniz: '))
    yedi_deger.append(deger)
    print(yedi_deger[i])
print(yedi_deger)

sapma,ort = sapma_ort(uc_deger,dort_deger,bes_deger,yedi_deger)
son = ahmet(uc_deger,dort_deger,bes_deger,yedi_deger)
yuzde = umut_yuzde(2723,son)

print('\n\n\n')
print('Katsayili degerin: {0:.2f}'.format(son))
print('Yuzdelik basarin: {0:.2f}'.format(yuzde))
print('Ortalaman: {0:.2f}'.format(ort))
print('Standart sapman: {0:.2f}'.format(sapma))
