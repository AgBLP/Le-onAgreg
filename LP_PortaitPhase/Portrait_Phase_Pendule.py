# coding: utf-8


import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate


#Ce script trace l'évolution temporelle, le portrait de phase
#et la FFT d'un oscillateur 1D.

#Auteurs: Aurélien Pascal, Alexandre Morlet, Brendan Le Pennec


#Discrétisation du temps------------------------

nombre_pas = 20000
t_final = 500
t = np.linspace(0,t_final,num=nombre_pas)

#Système d'équations à résoudre-----------------

def sys(y,t):
    """
    La fonction sys renvoie une liste contenant
    la dérivée de x et celle de x'
    Pour l'oscillateur harmonique le retour est donc [x',-x]
    """
    x, xprime = y

    #changer la ligne suivante pour un oscillateur different

    #return [xprime, -x] #oscillateur harmonique
    #return [xprime, -x-0.05*xprime] #oscillateur harmonique amorti
    #return [xprime, -np.sin(x)] #pendule simple non amorti
    #return [xprime, -np.sin(x)-0.1*xprime] #pendule simple amorti
    return [xprime, (2-x**2)*xprime -x] #oscillateur de Van der Pol

    omega = 2*np.pi #pulsation d'excitation
    omega0 = 1.5*omega #pulsation propre
    beta = omega0/4 #coefficient d'amortissement
    excitation = 1.09
    #return [xprime, -2*(beta)*xprime -(omega0**2)*np.sin(x) + excitation*(omega0**2)*np.cos(omega*t)] #Pendule amorti et forcé



#Liste de conditions initiales-------------------

"""
Les conditions initiales sont sous la forme [x(0),x'(0)]
y0 est un tableau contenant autant de conditions
initiales qu'il y a de portraits de phase à tracer.
Exemple : pour 3 courbes, y0 = [[10,0],[10,2],[8,5]]
"""

# Cas 'normal'
#y0 = [[-np.pi/4,2.0],[-np.pi/2,0.0],[-np.pi,0.0]]
#y0 = [[-np.pi/2,0.0]]

# Van der Pol
y0 = [[0.001,0], [5, 0]]

#Integration par le solveur odeint---------------------------------

#solution contient une liste de matrices, une pour chaque condition initiale y0
#chaque matrice contient (x,x'); le tableau t contient le temps

solution = []
legende = []
for ci in y0:
    solution.append(scipy.integrate.odeint(sys,ci,t))
    legende.append(r"y$_{0}$ = " + str(ci[0]*180/np.pi) + "° ," + r"$\frac{dy}{dt}_0$ = " + str(ci[1]) + " m/s" )

#Affichage---------------------------------------------
f, ax = plt.subplots(1,2) # ax[n] est la figure n

k=0    #compteur pour la légende
## Tracé de la solution en temps
for sol in solution:
    ax[0].plot(t[0000:nombre_pas],sol[0000:nombre_pas,0],label = str(legende[k]))
    ax[0].set_xlabel("Temps")
    ax[0].set_ylim(-4, 10)
    ax[0].grid()
    ax[0].set_ylabel("Position")
    ax[0].set_title('Evolution temporelle du systeme')
    ax[0].legend()
    k+=1

k=0
## Tracé du portrait de phase
for sol in solution: # tracé du portrait de phase
    ax[1].plot(sol[:,0],sol[:,1],label = str(legende[k]))
    #ax[1].set_xlim(-4, 4)
    #ax[1].set_ylim(-2, 2)
    ax[1].set_xlabel("Position")
    ax[1].set_ylabel("Vitesse")
    ax[1].grid()
    ax[1].set_title("Portrait de phase")
    ax[1].legend()
    k+=1

plt.show()
