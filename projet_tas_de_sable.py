########################################
# groupe MI TD04 
# Habib MABROUK
# Aissam BERRAHMANE
# Furkan YILMAZ
# Sylia OUAKLI
# https://github.com/uvsq22100688/projet_tas_de_sable
#######################################

import tkinter as tk
import random
import copy

HEIGHT = 700
WIDTH = 700
grille = 20
grille1 = grille -1
tc = HEIGHT //grille
obj = []
cases = grille*grille+1
liste_couleurs = ["midnightblue","mediumblue","royalblue","cornflowerblue","skyblue"]
cond = True
color = "powderblue"
l3 = [[0,0,0]]

def carre():
    for i in range(1,cases):
        if l3[i][2] >=5:
            color = "midnightblue"
        if l3[i][2] == 4:
            color = "mediumblue"
        if l3[i][2] == 3:
            color = "royalblue"
        if l3[i][2] == 2:
            color = "cornflowerblue"
        if l3[i][2] == 1:
            color = "skyblue"
        if l3[i][2] == 0 :
            color = "powderblue"
        obj.append(tk.Canvas.create_rectangle((l3[i][0]*tc,0+tc*l3[i][1]),(tc+l3[i][0]*tc,tc+tc*l3[i][1]),fill = ))


def sauvegarde():
    global l3
    fic = open("f_texte","w")
    for v in range(len(l3)):
        fic.write(str(l3[v][2])+"\n")
    fic.close


def affiche_sauvegarde():
    fic = open("f_texte","r")
    c = 0
    for l in fic:
        l3[c][2] = int(l)
        c += 1
    carre()


def config_aleatoire():
    global l3
    for i in range (1,cases):
        l3[i][2] = random.randint(1,4)
    carre()

def pile_centrée():
    global l3,obj
    case = (grille*grille)//2 - grille//2
    for i in range(1, cases):
        l3[i][2]= 0
    l3[case][2] = 700
    carre()



def max_stable():
    global l3, obj
    for i in range(1,cases):
        l3[i][2] = 6
    for i in range(1,cases):
        color = "royalblue"
        obj.append(tk.Canvas.create_rectangle((l3[i][0]*tc,0+tc*l3[i][1]),(tc+l3[i][0]*tc,tc+tc*l3[i][1]),fill = ))


def clic_config(event):
    global l3,obj
    for i in range(1,cases):
        if tc*l3[i][0] < event.x <tc+tc*l3[i][0] and tc*l3[i][1] < event.y< tc+tc*l3[i][1]:
            print(l3)
            for c in range (len(obj)):
                tk.Canvas.delete(obj[c])
            carre()


def stop():


#def changement_config():





























        