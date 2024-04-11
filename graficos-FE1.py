import matplotlib.pyplot as plt
import numpy as np

deltax0ida0 = [x/100 for x in [1.4,
2.0,
3.3,
4.3,
6.5,
8.0,
7.2,
11.5,
13.4,
15.3,
17.1,
18.3,
19.7,
20.4]]



deltax0ida1 =[x/100 for x in [0.3,
0.9,
2.8,
4.0,
6.8,
8.3,
9.6,
12.8,
14.6,
16.3,
18.2,
18.8,
20.5,
21.6,
23.6,
24.3,
24.8,
25.6,
26.5]]



deltax1ida0 = [x/100 for x in [0.2,
0.5,
0.8,
0.8,
1.0,
1.1,
1.4,
1.7,
1.8,
2.1,
2.4,
2.6,
3.1,
3.3,
3.5,
4.0,
4.1,
4.5,
5.0]]

pesoi = [784.356,
1204.896,
1474.824,
2018.592,
2305.146,
2600.502,
3096.348,
3383.88,
3880.704,
4389.264,
4774.596,
5280.222,
5554.062,
5826.924,
6306.144,
6581.94,
7138.422,
7562.874,
8141.85]

deltax1ida1 = [x/100 for x in [0.4,
0.5,
0.8,
0.9,
1.2,
1.3,
1.6,
1.9,
2.3,
2.7,
3.0,
3.2,
4.0,
4.0,
4.1,
4.8,
5.0,
5.5,
5.7]]

deltax0volta0 = [x/100 for x in [20.6,
20.1,
19.3,
19.1,
17.9,
17.2,
14.7,
12.4,
10.7,
8.8,
6.9,
4.7,
2.8,
1.3,]]

deltax0volta1 = [x/100 for x in [26.5,
26.1,
25.6,
25.1,
24.8,
24.7,
23.8,
23.2,
22.4,
21.1,
18.8,
15.0,
13.3,
12.0,
10.0,
8.2,
5.3,
4.0,
2.0]]
deltax1volta0 = [x/100 for x in [5.2,
4.9,
4.8,
4.3,
4.0,
4.0,
3.6,
3.4,
2.9,
2.4,
2.3,
1.9,
1.5,
1.3,
1.1,
0.8,
0.6,
0.3,
0.1]]
pesoi0 = [784.356,
1204.896,
1474.824,
2018.592,
2305.146,
2600.502,
3096.348,
3383.88,
3880.704,
4389.264,
4774.596,
5280.222,
5554.062,
5826.924]

pesov0 = [5554.062,
5280.222,
4774.596,
4389.264,
3880.704,
3383.880,
3096.348,
2600.502,
2305.146,
2018.592,
1474.824,
1204.896,
784.356,
299.268,]

pesov = [7562.874,7138.422,6581.94,6306.144,5826.924,5554.062,5280.222,4774.596,4389.264,3880.704,3383.88,3096.348,2600.502,2305.146,2018.592,1474.824,1204.896,784.356,299.268]

pesovolta = [x/1000 for x in pesov]
pesoida = [x/1000 for x in pesoi]
pesovolta0 = [x/1000 for x in pesov0]
pesoida0 = [x/1000 for x in pesoi0]
deltax1volta1 = [x/100 for x in [5.6,5.3,5.1,5.0,4.5,4.1,3.6,3.3,3.1,2.6,2.2,1.9,1.5,1.4,1.1,0.9,0.7,0.4,0.2]] 

incertezax = 0.5/100
incertezay = 0.02041241452

figura, axis = plt.subplots(2, 2)

for i in range(0, 2):
    for j in range(0,2):
        axis[i,j].grid()
        axis[i,j].set_xlabel("Variação de Espaço (m)")
        axis[i,j].set_ylabel("Força Peso (N)")

#Elastico 1 - Ida e Volta 1
        
axis[0,0].set_title("Elástico 1 - Ida e Volta 1")
axis[0,0].scatter(deltax0ida0, pesoida0)
axis[0,0].scatter(deltax0volta0,pesovolta0) 
b, a = np.polyfit(deltax0ida0, pesoida0, deg=1)  
xseq = np.linspace(0, 0.20, num=100)
axis[0,0].plot(xseq, a + b * xseq, color="k", lw=1); 
b, a = np.polyfit(deltax0volta0, pesovolta0, deg=1)
xseq = np.linspace(0, 0.20, num=100)
axis[0,0].plot(xseq, a + b * xseq, color="k", lw=1); 

axis[0,0].errorbar(deltax0ida0, pesoida0, xerr=incertezax, ecolor='grey', elinewidth=1, capsize=5, capthick=1, color='k', linestyle="none",)
axis[0,0].errorbar(deltax0ida0, pesoida0, yerr=incertezay, ecolor='grey', elinewidth=1, capsize=5, capthick=1, color='k', linestyle="none",)

axis[0,0].errorbar(deltax0volta0,pesovolta0, xerr=incertezax, ecolor='grey', elinewidth=1, capsize=5, capthick=1, color='k', linestyle="none",)
axis[0,0].errorbar(deltax0volta0,pesovolta0, yerr=incertezay, ecolor='grey', elinewidth=1, capsize=5, capthick=1, color='k', linestyle="none",)


#Elastico 1 - Ida e Volta 2

axis[1,0].set_title("Elástico 1 - Ida e Volta 2")
axis[1,0].scatter(deltax0ida1, pesoida)
axis[1,0].scatter(deltax0volta1,pesovolta) 
b, a = np.polyfit(deltax0ida1, pesoida, deg=1)  
xseq = np.linspace(0, 0.25, num=100)
axis[1,0].plot(xseq, a + b * xseq, color="k", lw=1); 
b, a = np.polyfit(deltax0volta1, pesovolta, deg=1)
xseq = np.linspace(0, 0.25, num=100)
axis[1,0].plot(xseq, a + b * xseq, color="k", lw=1); 

axis[1,0].errorbar(deltax0ida1, pesoida, xerr=incertezax, ecolor='grey', elinewidth=1, capsize=5, capthick=1, color='k', linestyle="none",)
axis[1,0].errorbar(deltax0ida1, pesoida, yerr=incertezay, ecolor='grey', elinewidth=1, capsize=5, capthick=1, color='k', linestyle="none",)

axis[1,0].errorbar(deltax0volta1,pesovolta, xerr=incertezax, ecolor='grey', elinewidth=1, capsize=5, capthick=1, color='k', linestyle="none",)
axis[1,0].errorbar(deltax0volta1,pesovolta, yerr=incertezay, ecolor='grey', elinewidth=1, capsize=5, capthick=1, color='k', linestyle="none",)

#Elastico 2 - Ida e Volta 1

axis[0,1].set_title("Elástico 2 - Ida e Volta 1")
axis[0,1].scatter(deltax1ida0, pesoida)
axis[0,1].scatter(deltax1volta0,pesovolta)
b, a = np.polyfit(deltax1ida0, pesoida, deg=1)  
xseq = np.linspace(0, 0.06, num=100)
axis[0,1].plot(xseq, a + b * xseq, color="k", lw=1); 
b, a = np.polyfit(deltax1volta0, pesovolta, deg=1)
xseq = np.linspace(0, 0.06, num=100)
axis[0,1].plot(xseq, a + b * xseq, color="k", lw=1); 

axis[0,1].errorbar(deltax1ida0, pesoida, xerr=incertezax, ecolor='grey', elinewidth=1, capsize=5, capthick=1, color='k', linestyle="none",)
axis[0,1].errorbar(deltax1ida0, pesoida, yerr=incertezay, ecolor='grey', elinewidth=1, capsize=5, capthick=1, color='k', linestyle="none",)

axis[0,1].errorbar(deltax1volta0,pesovolta, xerr=incertezax, ecolor='grey', elinewidth=1, capsize=5, capthick=1, color='k', linestyle="none",)
axis[0,1].errorbar(deltax1volta0,pesovolta, yerr=incertezay, ecolor='grey', elinewidth=1, capsize=5, capthick=1, color='k', linestyle="none",)

#Elástico 2 - Ida e Volta 2

axis[1,1].scatter(deltax1ida1, pesoida)
axis[1,1].scatter(deltax1volta1,pesovolta)
b, a = np.polyfit(deltax1ida1, pesoida, deg=1)  
xseq = np.linspace(0, 0.07, num=100)
axis[1,1].plot(xseq, a + b * xseq, color="k", lw=1); 
b, a = np.polyfit(deltax1volta1, pesovolta, deg=1)
xseq = np.linspace(0, 0.07, num=100)
axis[1,1].plot(xseq, a + b * xseq, color="k", lw=1); 

axis[1,1].errorbar(deltax1ida1, pesoida, xerr=incertezax, ecolor='grey', elinewidth=1, capsize=5, capthick=1, color='k', linestyle="none",)
axis[1,1].errorbar(deltax1ida1, pesoida, yerr=incertezay, ecolor='grey', elinewidth=1, capsize=5, capthick=1, color='k', linestyle="none",)

axis[1,1].errorbar(deltax1volta1,pesovolta, xerr=incertezax, ecolor='grey', elinewidth=1, capsize=5, capthick=1, color='k', linestyle="none",)
axis[1,1].errorbar(deltax1volta1,pesovolta, yerr=incertezay, ecolor='grey', elinewidth=1, capsize=5, capthick=1, color='k', linestyle="none",)
axis[1,1].set_title("Elástico 2 - Ida e Volta 2")

plt.show()

