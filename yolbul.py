import sys
dosya = open(sys.argv[1], "r")
liste = []
for i in dosya:
    liste += [i.strip('\n')]


# region S'nin ve F'nin kordinatlarını buluyoruz
baslangic = []
bitis = []


def bul(liste, v):
    listex = []
    for i, x in enumerate(liste):
        if v in x:
            listex = [i, x.index(v)]
            return listex


baslangic = bul(liste, 'S')
bitis = bul(liste, 'F')
# endregion


sütun = 0
satir = 0
print()
# region satir sütun hesabi

sütun = len(liste[0])
satir = len(liste)
# endregion


# gezdiğimiz konumu eklediğim liste ↓
gezinti_list = []

konum = []
konum = baslangic
konumx = baslangic[0]
konumy = baslangic[1]




# region üstüm duvar mı yol mu?


def ust(konum):
    if konum[0]-1 >= 0 and liste[konum[0]-1][konum[1]] == 'P':
        return True
    else:
        return False
# endregion

# region altım duvar mı yol mu?


def alt(konum):
    if konum[0]+1 < satir and liste[konum[0]+1][konum[1]] == 'P':
        return True
    else:
        return False
# endregion

# region sağım duvar mı yol mu?


def sag(konum):
    if konum[1]+1 < sütun and liste[konum[0]][konum[1]+1] == 'P':
        return True
    else:
        return False
# endregion

# region solum duvar mı yol mu?


def sol(konum):
    if konum[1]-1 >= 0 and liste[konum[0]][konum[1]-1] == 'P':
        return True
    else:
        return False
# endregion


# region listeyi ayrı bi listeye atarak üstünde oynamalar yapacağız.
son = []
for i in range(0, len(liste)):
    son.append(list(liste[i]))
# endregion

# region matrisi çözen kısım
def matris_coz(x, y):
    global gezinti_list
    global liste
    global son


    if sol([x, y]) is True and [x, y] not in gezinti_list:
        gezinti_list.append([x, y])
        son[x][y] = '1'
        y = y-1
        return matris_coz(x, y)

    if alt([x, y]) is True and [x, y] not in gezinti_list:
        gezinti_list.append([x, y])
        son[x][y] = '1'
        x = x+1
        return matris_coz(x, y)

    if sag([x, y]) is True and [x, y] not in gezinti_list:
        gezinti_list.append([x, y])
        son[x][y] = '1'
        y = y+1
        return matris_coz(x, y)

    if ust([x, y]) is True and [x, y] not in gezinti_list:
        gezinti_list.append([x, y])
        son[x][y] = '1'
        x = x-1
        return matris_coz(x, y)

# endregion


# region labirent çözümünü yeni listeye atıyoruz.
def cozum_yolu():
    global liste
    global son
    global yaz
    for i in range(len(liste)):
        for j in range(len(liste)):
            if son[i][j] == 'W':  # duvarları 0 yapıyoruz
                son[i][j] = '0'
            elif son[i][j] == 'P':  # gittiğimiz yol dışında kalan gidilebilecek yolları 0 yapıyoruz
                son[i][j] = '0'
            # Başlangıç değerim değiştiği için onu tekrardan 'S' yapıyorum
            elif son[baslangic[0]][baslangic[1]] == '1':
                son[baslangic[0]][baslangic[1]] = 'S'
    for x in range(len(liste)):
        print(son[x])
        
# endregion
#region çözüm yolunu dosyaya yazdırıyorum..
def dosyaya_yaz():
    yaz = open(sys.argv[2], "w")
    for x in range(len(liste)):
        for j in range(len(liste)):
            yaz.write((str(son[x][j])).strip("'"))
            if j <(len(liste)-1):
                yaz.write(',')    
        yaz.write('\n')    
    print("Çözüm Yolu Dosyaya Yazıldı")
#endregion


matris_coz(konumx, konumy)
gezinti_list.append(bitis)  # F kordinatinı manuel olarak ekledim..
print('Labirent çözümü', gezinti_list,"\n")

cozum_yolu()
dosyaya_yaz()

