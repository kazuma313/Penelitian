import numpy as np
import matplotlib.pyplot as plt

def barH_Tertinggi(data:'DataFrame', banyak:int, x:str, y:str):
    data = data.nlargest(banyak, x)
    
    gejala = list(data[y])
    y_pos = np.arange(len(gejala))
    nilai = list(data[x])
    
    fig, ax = plt.subplots()
    
    hbars = ax.barh(gejala, nilai, align='center')
    ax.set_yticks(y_pos)
    ax.invert_yaxis()
    ax.set_xlabel('nilai')
    ax.set_title('pengaruh Gejala')
    
    ax.bar_label(hbars, fmt='%.2f')
    ax.set_xlim(right = 2)
    
    plt.show()
    
    
def barH_Terendah(data:'DataFrame', banyak:int, x:str, y:str):
    data = data.nsmallest(banyak, x)
    
    gejala = list(data[y])
    y_pos = np.arange(len(gejala))
    nilai = list(data[x])
    
    fig, ax = plt.subplots()
    
    hbars = ax.barh(gejala, nilai, align='center')
    ax.set_yticks(y_pos)
    ax.invert_yaxis()
    ax.set_xlabel('nilai')
    ax.set_title('pengaruh Gejala')
    
    ax.bar_label(hbars, fmt='%.2f')
    ax.set_xlim(left = -2)
    
    plt.show()