# Dimerization & ZL
### average raw data to meta data

import os
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

BC = 'PBC'
Ls = [64]
Jdis = ['Jdis050','Jdis100','Jdis150','Jdis200','Jdis250']
#Jdis = ['Jdis250']
init_D = 80 #real value is devide by 100
final_D = 90 #1.0
space = 10
file_num = int ((final_D - init_D)/space+1)
Dimer = []
for i in range(file_num):
    D = init_D + space*i
    if (D < 10):
        d = '00' + str(D)[0]
        Dimer.append('Dim' + d)
    elif (D >= 10 and D < 100):
        d = '0' + str(D)[0] + str(D)[1]
        Dimer.append('Dim' + d)
    elif (D >= 100):
        d = str(D)[0] + str(D)[1] + str(D)[2]
        Dimer.append('Dim' + d)
    #print(d)

P = 10
chis = [40]
N = 500
init_seed = 1

arr = []
for j in range(N):
    n = str(init_seed+j)
    arr.append(n)

for i in range(len(Ls)):
    L = Ls[i]
    dfstr = pd.DataFrame(columns = ['Dimerization', 'ZL', 'error'])

    for m in range(len(chis)):
        M = chis[m]

        for j in range(len(Jdis)):
            jdis = Jdis[j]
            J = float(Jdis[j][4] + '.' + Jdis[j][5] + Jdis[j][6])

            for d in range(len(Dimer)):
                dimer = Dimer[d]
                D = float(Dimer[d][3] + '.' + Dimer[d][4] + Dimer[d][5])
                x = 0
                print(str(L)+'_'+str(M)+'_'+jdis+'_'+dimer)

                for k in range(len(arr)):
                    num = arr[k]
                    if(num == "96"):
                        myfile = '/home/liusf/tSDRG/2_MainDimZL/data2/'+ BC +'/'+ jdis +'/'+ dimer +'/L'+ str(L) +'_P'+ str(P) +'_m'+ str(M)+'_'+ str(int(num)+1) +'/ZL.csv'
                    if(num != "96"):
                        myfile = '/home/liusf/tSDRG/2_MainDimZL/data2/'+ BC +'/'+ jdis +'/'+ dimer +'/L'+ str(L) +'_P'+ str(P) + '_m' + str(M) + '_' + num +'/ZL.csv'
                    df = pd.read_csv(myfile)
                    if(k == 0):
                        dftc = df['ZL']
                    dfc = df['ZL']

                    if(k != 0):
                        dftc += dfc
                dfavc = dftc/N 

                for a in range(len(arr)):
                    num = arr[a]
                    if(num == "96"):
                        myfile = '/home/liusf/tSDRG/2_MainDimZL/data2/'+ BC +'/'+ jdis +'/'+ dimer +'/L'+ str(L) +'_P'+ str(P) +'_m'+ str(M)+'_'+ str(int(num)+1) +'/ZL.csv'
                    if(num != "96"):
                        myfile = '/home/liusf/tSDRG/2_MainDimZL/data2/'+ BC +'/'+ jdis + '/'+ dimer + '/L'+ str(L) +'_P'+ str(P) +'_m'+ str(M) +'_'+ num + '/ZL.csv'
                    df = pd.read_csv(myfile)
                    x += np.square(df['ZL'][0]-dfavc.mean())
                
                std = np.sqrt(x/(N-1))
                error = std/np.sqrt(N)
                mean = {'Dimerization':D ,'ZL':dfavc.mean(),'error':error}  ## second average(1 times)
                ## total average times = N
                dfstr.loc[d] = mean

            direc = '/home/liusf/tSDRG/Sorting_data/Spin2/metadata/ZL/'+ jdis
            if (os.path.exists(direc) == False):
                os.mkdir(direc)
            direc2 = direc + '/Dimer-ZL'
            if (os.path.exists(direc2) == False):
                os.mkdir(direc2)
            path = direc2 +'/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m' + str(M) + '_dim-zl_AV'+ str(N) +'.csv'
            dfstr.to_csv(path,index=0)

print('done')
