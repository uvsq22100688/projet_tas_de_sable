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
        obj.append(canvas.create_rectangle((l3[i][0]*tc,0+tc*l3[i][1]),(tc+l3[i][0]*tc,tc+tc*l3[i][1]),fill = color,outline = color ))


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
        obj.append(canvas.create_rectangle((l3[i][0]*tc,0+tc*l3[i][1]),(tc+l3[i][0]*tc,tc+tc*l3[i][1]),fill = color,outline = color))


def clic_config(event):
    global l3,obj
    for i in range(1,cases):
        if tc*l3[i][0] < event.x <tc+tc*l3[i][0] and tc*l3[i][1] < event.y< tc+tc*l3[i][1]:
            print(l3)
            for c in range (len(obj)):
                canvas.delete(obj[c])
            carre()


def stop():
    global cond
    cond = False


def changement_config():
    global l3 , obj , cond
    l4 = copy.deepcopy(l3)
    for i in range(1, cases):
        if l4[i][0] == 0 and l4[i][1]==0 and l4[i][2] >=4:
            l3[i][2] -= 4
            l3[i+1][2] +=1
            l3[i+grille][2] +=1 

        elif l4[i][0] == grille1 and l4[i][1]==0 and l4[i][2] >=4:
            l3[i][2] -= 4
            l3[i-1][2] +=1
            l3[i+grille][2] +=1 

        elif l4[i][0] == 0 and l4[i][1]==grille1 and l4[i][2] >=4:
            l3[i][2] -= 4
            l3[i+1][2] +=1
            l3[i-grille][2] +=1 

        elif l4[i][0] == grille1 and l4[i][1]==grille1 and l4[i][2] >=4:
            l3[i][2] -= 4
            l3[i-1][2] +=1
            l3[i-grille][2] +=1 
        
        elif l4[i][0] == 0 and  l4[i][2] >=4:
            l3[i][2] -= 4
            l3[i-grille][2] +=1
            l3[i+grille][2] +=1 
            l3[i+1][2] +=1

        elif l4[i][0] == grille1 and l4[i][2] >=4:
            l3[i][2] -= 4
            l3[i-grille][2] +=1
            l3[i+grille][2] +=1 
            l3 [i-1][2] +=1

        elif l4[i][1]==0 and l4[i][2] >=4:
            l3[i][2] -= 4
            l3[i+grille][2] +=1
            l3[i-1][2] +=1
            l3[i+1][2] +=1

        elif l4[i][1]==grille1 and l4[i][2] >=4:
            l3[i][2] -= 4
            l3[i-grille][2] +=1
            l3[i+1][2] +=1
            l3[i-1][2] +=1

        elif  l4[i][2] >=4:
            l3[i][2] -= 4
            l3[i-grille][2] +=1
            l3[i+grille][2] +=1
            l3[i+1][2] +=1
            l3[i-1][2] +=1
        for c in range(len(obj)):
            canvas.delete(obj[c])
        obj = []
        carre ()
        if cond == True:
            canvas.after(50, changement_config)  
        elif cond == False:
            cond = True





racine = tk.Tk()
canvas = tk.Canvas(racine , height = HEIGHT , width = WIDTH , bg = "black")
canvas.pack(side='right')
canvas.bind("<Button-1>",clic_config)

bouton1 = tk.Button(racine,text="changemenet de configuration", command = changement_config)
bouton1.pack(side = "top", fill = "x")

bouton2 = tk.Button(racine,text="pile centrée", command = pile_centrée)
bouton2.pack(side = "top", fill = "x")

bouton3 = tk.Button(racine,text="configuration aleatoire", command = config_aleatoire)
bouton3.pack(side = "top", fill = "x")

bouton4 = tk.Button(racine,text="max stable", command = max_stable)
bouton4.pack(side = "top", fill = "x")

bouton5 = tk.Button(racine,text="sauvegarder", command = sauvegarde)
bouton5.pack(side = "top", fill = "x")

bouton6 = tk.Button(racine,text="afficher la sauvegarde", command = affiche_sauvegarde)
bouton6.pack(side = "top", fill = "x")

bouton7 = tk.Button(racine,text="Stop", command = stop)
bouton7.pack(side = "top", fill = "x")

for a in range(grille):
    for v in range(grille):
        l2=[]
        l2.append(v)
        l2.append(a)
        l2.append(0)
        l2.append(l2)
        obj.append(canvas.create_rectangle((v*tc,tc*a),(tc+v*tc,tc+a*tc), fill = color,outline = color))

    racine.mainloop
























        