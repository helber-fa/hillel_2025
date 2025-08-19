#global
# local
# non-local
# build-in

dog_name = "Bobik" #global

def dog_actions(name):
    dog_name = name #non local
    def make_sound():

        global dog_name
        dog_name = "Richi"
        dog_sound = "Rrrrrr"
        print(dog_sound) #local
        print(dog_name)

    def walk():
        print("walking") #build-in

    walk()
    make_sound()
    print(dog_name)

dog_actions("Naida")
print(dog_name)