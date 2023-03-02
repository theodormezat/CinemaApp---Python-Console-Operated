import random
class Film():

    def __init__(self, titlu, durata, gen):
        self.titlu = titlu
        self.durata = durata
        self.gen = gen

    def getTitlu(self):
        return self.titlu

    def getDurata(self):
        return self.durata

    def getGen(self):
        return self.gen

class Drama(Film):

    def __init__(self, titlu, durata, varsta_minima):
        super().__init__(titlu, durata, "Drama")
        self.varsta_minima = varsta_minima

    def getVarsta_minima(self):
        return self.varsta_minima

    def __str__(self):
        afisare = "Titlu: "+ self.titlu + " (drama)\n"
        afisare += "Durata: " + str(self.durata) + " minute\n"
        afisare += "Varsta minima: " + str(self.varsta_minima) + " ani\n"
        return afisare

class Animatie(Film):

    def __init__(self, titlu, durata, dublaj):
        super().__init__(titlu, durata, "Animatie")
        self.dublaj = dublaj

    def getDublaj(self):
        return self.dublaj

    def __str__(self):
        afisare = "Titlu: "+ self.titlu + " (animatie)\n"
        afisare += "Durata: " + str(self.durata) + " minute\n"
        afisare += "Limba dublaj: " + self.dublaj + "\n"
        return afisare


class Cinematograf():

    def __init__(self):
        self._lista_filme = []

    def adaugare_drama(self, titlu, durata, varsta_minima):

        try:
            durata_film = int(durata)
        except:
            raise ValueError("Valoarea pentru durata filmului nu este valida.")

        try:
            varsta = int(varsta_minima)
        except:
            raise ValueError("Valoarea pentru varsta nu este valida.")

        if durata_film > 180:
            raise ValueError("Durata filmelor trebuie sa fie de cel mult 180 de minute.")

        drama = Drama(titlu, durata_film, varsta)
        self._lista_filme.append(drama)

    def adaugare_animatie(self, titlu, durata, dublaj):

        try:
            durata_film = int(durata)
        except:
            raise ValueError("Valoarea pentru durata filmului nu este valida.")

        if durata_film > 180:
            raise ValueError("Durata filmelor trebuie sa fie de cel mult 180 de minute.")

        animatie = Animatie(titlu, durata_film, dublaj)
        self._lista_filme.append(animatie)

    def afisare_filme(self):

        for film in self._lista_filme:
            print(film)

    def afisare_animatii(self):

        for film in self._lista_filme:
            if film.getGen() == "Animatie":
                print(film)

    def alegere_film(self):
        if len(self._lista_filme) > 0:
            print(self._lista_filme[random.randint(0,len(self._lista_filme)-1)])
        else:
            print("Nu exista niciun film.")

    def salveaza_filme(self, filename):
        f = open("lista_filme.txt", mode='at', encoding='utf-8')
        for film in self._lista_filme:
            f.write(str(film) + "\n")
        f.close()

if __name__ == "__main__":
    cinema=Cinematograf()

    while True:
        cmd=input(">>What do you want to do? Type in one of these commands:" '\n'
                  "1. Add drama" '\n'
                  "2. Add animation" '\n'
                  "3. Display list of dramas" '\n'
                  "4. Display list of animations" '\n'
                  "5. Choose film" '\n'
                  "6. Save film" '\n'
                  ">>")
        args = cmd.split(",")
        try:
            if args[0] == "Add drama":
                if len(args) >= 4:
                    cinema.adaugare_drama(' '.join(args[1:len(args)-2]), args[len(args)-2], args[len(args)-1])
                else:
                    raise ValueError("Incomplete number of parameters.")
            elif args[0] == "Add animation":
                if len(args) >= 4:
                    cinema.adaugare_animatie(' '.join(args[1:len(args)-2]), args[len(args)-2], args[len(args)-1])
                else:
                    raise ValueError("Incomplete number of parameters.")
            elif args[0] == "Display list of dramas":
                cinema.afisare_filme()
            elif args[0] == "Display_list_of_animations":
                cinema.afisare_animatii()
            elif args[0] == "Choosefilm":
                cinema.alegere_film()
            elif args[0:1] == "Save,film":
                if len(args) == 3:
                    cinema.salveaza_filme(args[3])
                else:
                    raise ValueError("Wrong number of parameters.")
            elif args[0] == "exit":
                break
            else:
                print("Command does not exist. Please try again.")
        except ValueError as e:
            print(e)