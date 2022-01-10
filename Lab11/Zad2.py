import numpy as np
import matplotlib.pylab as plt

def obliczT(r1,r2):
    tmax = 2*np.pi*np.lcm(r1,r2)/r2
    t = np.linspace(0,tmax,300)
    return t

def obliczX(r1,r2,d,t):
    lista = []
    for i in range(len(t)):
        x = (r2-r1)*np.cos(t[i])+d*np.cos((r2-r1)*t[i]/r1)
        lista.append(x)
    return lista

def obliczY(r1,r2,d,t):
    lista = []
    for i in range(len(t)):
        y = (r2-r1)*np.sin(t[i])-d*np.sin((r2-r1)*t[i]/r1)
        lista.append(y)
    return lista

def main(r1,r2,d):
    t = obliczT(r1,r2)
    x = obliczX(r1,r2,d,t)
    y = obliczY(r1,r2,d,t)
    plt.plot(x,y)
    plt.show()



if __name__ == '__main__':
    main(5,7,4)
    #main(1,2,3)
    #main(8,10,4)
    #main(7,2,10)
