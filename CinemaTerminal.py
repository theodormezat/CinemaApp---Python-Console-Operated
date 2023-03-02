import random


class Film():

    def __init__(self, title, duration, genre):
        self.title = title
        self.duration = duration
        self.gen = genre

    def getTitle(self):
        return self.title

    def getDuration(self):
        return self.duration

    def getGenre(self):
        return self.genre


class Drama(Film):

    def __init__(self, title, duration, minimum_age):
        super().__init__(title, duration, "Drama")
        self.minimum_age = minimum_age

    def getMinimumAge(self):
        return self.minimum_age

    def __str__(self):
        display = "Title: " + self.title + " (Drama)\n"
        display += "Duration: " + str(self.duration) + " minutes\n"
        display += "Minimum viewing age: " + str(self.minimum_age) + " years old\n"
        return display


class Animation(Film):

    def __init__(self, title, duration, dubbing):
        super().__init__(title, duration, "Animation")
        self.dubbing = dubbing

    def getDubbing(self):
        return self.dubbing

    def __str__(self):
        display = "Title: " + self.title + " (Animation)\n"
        display += "Duration: " + str(self.duration) + " minutes\n"
        display += "Dubbing language: " + self.dubbing + "\n"
        return display


class Cinema():

    def __init__(self):
        self._film_list = []

    def add_drama(self, title, duration, minimum_age):

        try:
            film_duration = int(duration)
        except:
            raise ValueError("The value for film duration is not valid.")

        try:
            age = int(minimum_age)
        except:
            raise ValueError("The value for age is not valid.")

        if film_duration > 180:
            raise ValueError("Film duration must be at most 180 minutes.")

        drama = Drama(title, film_duration, age)
        self._film_list.append(drama)

    def add_animation(self, title, duration, dubbing):

        try:
            film_duration = int(duration)
        except:
            raise ValueError("The value for film duration is not valid.")

        if film_duration > 180:
            raise ValueError("Film duration must be at most 180 minutes.")

        animation = Animation(title, film_duration, dubbing)
        self._film_list.append(animation)

    def display_dramas(self):

        for film in self._film_list:
            print(film)

    def display_animations(self):

        for film in self._film_list:
            if film.getGen() == "Animation":
                print(film)

    def get_random_film(self):
        if len(self._film_list) > 0:
            print(self._film_list[random.randint(0, len(self._film_list) - 1)])
        else:
            print("No movie is available yet.")

    def save_movie(self, filename):
        f = open("film_list.txt", mode='at', encoding='utf-8')
        for film in self._film_list:
            f.write(str(film) + "\n")
        f.close()


if __name__ == "__main__":
    cinema = Cinema()

    while True:
        cmd = input(">>What do you want to do? Type in one of these commands:" '\n'
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
                    cinema.add_drama(' '.join(args[1:len(args) - 2]), args[len(args) - 2], args[len(args) - 1])
                else:
                    raise ValueError("Incomplete number of parameters.")
            elif args[0] == "Add animation":
                if len(args) >= 4:
                    cinema.add_animation(' '.join(args[1:len(args) - 2]), args[len(args) - 2], args[len(args) - 1])
                else:
                    raise ValueError("Incomplete number of parameters.")
            elif args[0] == "Display list of dramas":
                cinema.display_dramas()
            elif args[0] == "Display_list_of_animations":
                cinema.display_animations()
            elif args[0] == "Choosefilm":
                cinema.get_random_film()
            elif args[0:1] == "Save,film":
                if len(args) == 3:
                    cinema.save_movie(args[3])
                else:
                    raise ValueError("Wrong number of parameters.")
            elif args[0] == "exit":
                break
            else:
                print("Command does not exist. Please try again.")
        except ValueError as e:
            print(e)
