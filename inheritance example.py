class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        user_sound = input("Enter a cat sound: ")

        if user_sound.lower() == "meow":
            print("Cat meows")

        elif user_sound.lower() == "purr":
            print("Cat purrs")

        else:
            print("This is not a valid sound for a cat")


class Lion(Animal):
            def sound(self):
                user_sound = input("Enter a lion sound: ")
                if user_sound.lower() == "roar":
                    print("Lion roars")
                else:
                    print("This is not a valid sound for a lion")


d = Dog()
d.sound()
d.bark()

c = Cat()
c.sound()


l = Lion()
l.sound()
