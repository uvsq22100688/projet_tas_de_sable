########################################
# groupe MI TD04 
# Habib MABROUK
# Aissam BERRAHMANE
# Furkan YILMAZ
# Sylia OUAKLI
# https://github.com/uvsq22100688/projet_tas_de_sable
#######################################



 # salu cava
import tkinter as tk
import random
import copy

HEIGHT = 700
WIDTH = 700
grille = 50
grille1 = grille -1
tc = HEIGHT//grille
obj = []##liste dans laquelle vont être stockés les grains de sable pour pouvoir ensuite les effacer
ncases = grille*grille+1
cond = True
color = "powderblue"
l3=[[0,0,0]]
l4 = []
p = 0


def carre(): ##fonction qui sera utilisée pour afficher les carrés avec leur nouvelle couleur après un changement de configuration
    for v in range(1,ncases):
        if l3[v][2] >= 5:
                color = "midnightblue"
        if l3[v][2] == 4:
                color = "mediumblue"
        if l3[v][2] == 3:
                color = "royalblue"
        if l3[v][2] == 2:
                color = "cornflowerblue"
        if l3[v][2] == 1:
                color = "skyblue"
        if l3[v][2] == 0:
                color = "powderblue"
        obj.append(canvas.create_rectangle((l3[v][0]*tc,0+tc*l3[v][1]),(tc+l3[v][0]*tc,tc+tc*l3[v][1]), fill = color, outline = color))


def sauvegarde(): ##fonction sauvegardant la configuration actuellement affichée
    global l3
    fic = open("f_texte", "w")
    for i in range(len(l3)):
        fic.write(str(l3[i][2])+"\n")
    fic.close

def affiche_sauvegarde(): ##fonction modifiant la liste l3 en la configuration sauvegardée
    fic= open("f_texte", "r")
    c = 0
    for l in fic:
        l3[c][2] = int(l)
        c += 1
    carre()


def config_aléatoire(): ##fonction attribuant un nombre de grains de sable aléatoire à chaque carré
    global l3
    for v in range(1,ncases):
        l3[v][2] = random.randint(1,4)
    carre()

def pile_centrée():
    global l3, obj
    case = (grille*grille)//2 - grille//2
    for v in range(1,ncases):
        l3[v][2] = 0
    l3[case][2] = 700
    carre()


def max_stable(): ##fonction attribuant 3 grains de sable à tous les carrés
    global l3, obj
    for v in range(1,ncases):
        l3[v][2] = 3
    for v in range(1,ncases):
        color = "royalblue"
        obj.append(canvas.create_rectangle((l3[v][0]*tc,0+tc*l3[v][1]),(tc+l3[v][0]*tc,tc+tc*l3[v][1]), fill = color, outline = color))

def clic_config(event):
    global l3, obj
    for v in range(1,ncases):
        if tc*l3[v][0] <event.x< tc+tc*l3[v][0] and tc*l3[v][1] <event.y< tc+tc*l3[v][1]:
            l3[v][2] += 1
            print(l3)
            for c in range(len(obj)):
                canvas.delete(obj[c])
            carre()
cont = 0
def identité():
    global l3, obj, l4, p, cont
    for v in range(1,ncases):
        l3[v][2] = 6
    while p != 1:
        changement_config()
    sauvegarde()
    fic= open("f_texte", "r")
    c = 0
    for l in fic:
        l3[c][2] = 6 - int(l)
        c += 1


def stop():
    global cond
    cond = False

##fonction qui attribue le nouveau nombre de grains de sable de chaque case(nouvelle configuration)
def changement_config():
    global l3, obj, cond, l4, p
    l4 = copy.deepcopy(l3)
    for v in range(1,ncases):
        if l4[v][0] == 0 and l4[v][1]== 0 and l4[v][2] >= 4:
            l3[v][2] -= 4
            l3[v+1][2] += 1
            l3[v+grille][2] += 1
        elif l4[v][0] == grille1 and l4[v][1]== 0 and l4[v][2] >= 4:
            l3[v][2] -= 4
            l3[v-1][2] += 1
            l3[v+grille][2] += 1
        elif l4[v][0] == 0 and l4[v][1]== grille1 and l4[v][2] >= 4:
            l3[v][2] -= 4
            l3[v+1][2] += 1
            l3[v-grille][2] += 1
        elif l4[v][0] == grille1 and l4[v][1]== grille1 and l4[v][2] >= 4:
            l3[v][2] -= 4
            l3[v-1][2] += 1
            l3[v-grille][2] += 1
        elif l4[v][0] == 0 and l4[v][2] >= 4:
            l3[v][2] -= 4
            l3[v-grille][2] += 1
            l3[v+grille][2] += 1
            l3[v+1][2] += 1
        elif l4[v][0] == grille1 and l4[v][2] >= 4:
            l3[v][2] -= 4
            l3[v-grille][2] += 1
            l3[v+grille][2] += 1
            l3[v-1][2] += 1
        elif l4[v][1] == 0 and l4[v][2] >= 4:
            l3[v][2] -= 4
            l3[v+grille][2] += 1
            l3[v-1][2] += 1
            l3[v+1][2] += 1
        elif l4[v][1] == grille1 and l4[v][2] >= 4:
            l3[v][2] -= 4
            l3[v-grille][2] += 1
            l3[v+1][2] += 1
            l3[v-1][2] += 1
        elif l4[v][2] >= 4:
            l3[v][2] -= 4
            l3[v+grille][2] += 1
            l3[v-grille][2] += 1
            l3[v+1][2] += 1
            l3[v-1][2] += 1
    if l4 == l3:
        p = 1
        return 1
    for c in range(len(obj)):
        canvas.delete(obj[c])
    obj = []
    carre()
    if cond == True:
        canvas.after(50, changement_config)
    elif cond == False:
        cond == True
 

##création de la fenêtre tkinter et du canvas
racine = tk.Tk()
canvas = tk.Canvas(racine, height = HEIGHT, width=WIDTH, bg = "black")
canvas.pack(side="right")
canvas.bind("<Button-1>",clic_config) ##ajout du clic souris dans le canevas

##création et placement des boutons éxecutant des fonctions
bouton1 = tk.Button(racine, text="change config", command = changement_config)
bouton2 = tk.Button(racine, text = "pile centrée", command=identité)
bouton3 = tk.Button(racine, text = "config aléatoire", command=config_aléatoire)
bouton4 = tk.Button(racine, text = "max stable", command=max_stable)
bouton5 = tk.Button(racine, text = "enregistrer", command=sauvegarde)
bouton6 = tk.Button(racine, text = "afficher sauvagarde", command=affiche_sauvegarde)
bouton7 = tk.Button(racine, text = "stop", command = stop)
bouton8 = tk.Button(racine,text = "identité", command = identité )
bouton1.pack(side="top", fill = "x")
bouton2.pack(side="top", fill = "x")
bouton3.pack(side="top", fill = "x")
bouton4.pack(side="top", fill = "x")
bouton5.pack(side="top", fill = "x")
bouton6.pack(side="top", fill = "x")
bouton7.pack(side="top", fill = "x")
bouton8.pack(side="top", fill = "x")



for j in range(grille): ##fonction créant des carrés contenant 0 grains de sable
        for i in range(grille):
            l2=[]
            l2.append(i)
            l2.append(j)
            l2.append(0)
            l3.append(l2)
            obj.append(canvas.create_rectangle((i*tc,tc*j),(tc+i*tc,tc+j*tc), fill = color, outline = color))

racine.mainloop()























        