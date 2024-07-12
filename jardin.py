class Jardin:
    
    def __init__(self, listeFleur, listeArbre):
        self.liste_fleur = listeFleur
        self.liste_arbres = listeArbre

    def nombre_rosier(self):
        liste_rosier=[]
        for fleur in self.liste_fleur:
            if fleur.type == 'rosier':
                liste_rosier.append(fleur)
        return len(liste_rosier)

    def nombre_centenaire(self):
        liste_centenaire=[]
        for arbre in self.liste_arbres:
            if arbre.est_centenaire ==True:
                liste_centenaire.append(arbre)
        return len(liste_centenaire)
     
    def __str__(self):
        msg = ""
        for animal in self.liste_Zoo:
            msg += animal.name + ', '
        return msg
    


class Plante:

    def __init__(self, nom, taille, localisation):
        self.nom = nom
        self.taille = taille
        self.localisation= localisation
    


    def __str__(self):
        return f"Cette plante {self.nom}, il a une taille {self.taille} cm et se trouve {self.localisation}"
    

        

class Arbre (Plante):

    def __init__(self, nom, taille, localisation, feuillage, age):
        super().__init__(nom,taille,localisation)
        self.feuillage = feuillage 
        self.age = age 
        self.set_age()

    def set_age (self):
        if self.age >=100:
            self.est_centenaire = True
       

class Fleur (Plante):

    def __init__(self, nom, taille, localisation, couleur, floraison, type):
        super().__init__(nom,taille,localisation)
        self.couleur = couleur
        self.floraison = floraison
        self.type = type







Rose = Fleur ( nom = 'rose', taille = 10, localisation = 'Nord Grenoble',  couleur = 'rose', floraison = 'été', type = 'rosier')

Jonquille = Fleur ( nom = 'jonquille',  taille = 5, localisation = 'Nord Grenoble', couleur = 'jaune', floraison = 'printemps', type = 'non rosier')

Chene = Arbre ( nom = 'chene', taille = 100,feuillage  = 'non persistant', age = 20, localisation = 'Sud Grenoble')

Platane = Arbre ( nom = 'platane', taille = 110,feuillage = 'persistant', age = 50, localisation = 'Nord Grenoble')
Erable = Arbre (nom = 'erable', taille = 80,feuillage  = 'non persistant', age = 101, localisation = 'Sud Grenoble')
Cedre = Arbre (nom = 'cedre', taille = 90,feuillage  = 'non persistant', age = 103, localisation = 'Nord Grenoble')

ListeFleur = (Rose, Jonquille)
ListeArbre = (Chene, Platane, Erable, Cedre)

Listejardin = [ListeFleur, ListeArbre]

print (Listejardin)

jardin = Jardin([Rose, Jonquille], [Chene, Platane, Erable, Cedre])


print("le nombre de rosier est ",jardin.nombre_rosier())
print("les arbres centenairs sont ",jardin.arbres_centenaires())

