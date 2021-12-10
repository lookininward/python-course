my_name = input('What is your name? ')
my_age = input('What is your age? ')


def print_user_data(name, age):
    """ Prints string with user's name and age. """
    print("User is " + name + ", aged " + age + ".")


def print_decades_lived(age):
    """ Prints string with user's decades lived. """
    decades_lived = str(int(int(age) / 10))
    print("You have lived for " + decades_lived + " decades.")


print_user_data(my_name, my_age)
print_decades_lived(my_age)
