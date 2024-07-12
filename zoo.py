class Animal:
    def __init__(self, name, poids, taille):
        self.name = name
        self.poids_animal = poids
        self.taille_animal = taille

       

    def se_deplacer (self):
        pass

    def get_taille(self):
        return self.__taille

    def set_new_taille (self,new_taille):
        try:
            if new_taille >0:
                self.__taille = new_taille

            else: 
                raise ValueError
        except ValueError:

            self.set_taille(abs(new_taille))


        self.__taille = new_taille

class Serpent(Animal):
    def se_deplacer (Serpent):
        print (' je rampe')
    

class Oiseau(Animal):
    def __init__(self, name, poids, taille, altitude_max):
        super().__init__(name,poids,taille)
        self.altitude_max = altitude_max

    def se_deplacer (Oiseau):
        print ('je vole')
    
    
    

class Zoo:

    def __init__(self, liste):
        self.liste_Zoo = []
        
        for animal in self.liste_Zoo:

            self.add_newobject(animal)

    
    def add_newobject(self, animal: Animal):
        if isinstance(animal, Animal):
            self.liste_Zoo.append(animal)
        else:
            raise TypeError('animal must be an Animal')
    
       
           

    def __str__(self):
        msg = ""
        for animal in self.liste_Zoo:
            msg += animal.name + ', '
        return msg





poule = Animal(name = 'poule', poids = 2, taille = 50)
print (poule.name)


print (poule.poids_animal)
print (Zoo)




serpent = Serpent (name = 'serpent', poids = 1, taille = 200)
oiseau = Oiseau (name = 'oiseau', poids = 1, taille = 10, altitude_max = 500)
zoo = Zoo([serpent,oiseau]) 


liste = [serpent, oiseau]



renard = Animal(name = 'renard',poids = 5, taille = 85)
couleuvre = Serpent (name = 'couleuvre',poids = 1, taille = 1)

newlist = (renard, couleuvre)

aigle = Oiseau(name = 'aigle', poids  = 3, taille  = 0.9, altitude_max=6000)
chat = Animal(name = 'chat', poids = 5, taille = 0.3)

listezoo2 = liste= [renard, chat]
listezoo5 = liste= [couleuvre]
listezoo7 = listezoo2.__add__(listezoo5)

for animal in listezoo7:
    print (animal)

