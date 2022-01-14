import matplotlib.pyplot as plt
import requests
import urllib.request

def getimage(par):
    s = findpar(par, 's')
    d = findpar(par,'d')
    c = findpar(par, 'c')
    t = findpar(par, 't')
    a = findpar(par, 'a')

    with urllib.request.urlopen(f'https://stooq.pl/c/?{s}&{d}&{c}&{t}&{a}') as response:
        imgname = f'{s[2::]}_{d[2::]}_{c[2::]}_{t[2::]}_{a[2::]}.png'
        content = response.read()
        with open(imgname,'wb') as file:
            file.write(content)

    img = plt.imread(imgname)
    plt.imshow(img)
    plt.axis('off')
    plt.show()


def findpar(string,par):
    start = string.find(f'-{par}=')
    end = string.find(' ',start)
    if start == -1:
        return defaultpar(par)
    if end == -1:
        end = len(string)
    string = string[start+1:end]
    return string

def defaultpar(par):
    if par == 's':
        return 's=eurpln'
    elif par == 'd':
        return 'd=20220112'
    elif par == 'c':
        return 'c=1d'
    elif par == 't':
        return 't=l'
    elif par == 'a':
        return 'a=ln'


if __name__ == '__main__':
    #getimage('-s=eurpln -d=20220112 -c=1d')
    getimage(input('podaj parametry'))