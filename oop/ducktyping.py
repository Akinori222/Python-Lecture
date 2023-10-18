class Duck:
    """
    This is a class for Duck.

    Attributes:
        name(str): the name of the duck

    Methods:
        walk: print~
        quack: print~
        fly: print~
    """
    def __init__(self, name):
        """
        The contructor for Duck class
        :param name: the name of duck
        """
        self.name = name

    def walk(self):
        print("walking")

    def quack(self):
        print("quack quack")

    def fly(self):
        print("flying")


class Penguin:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walking")

    def quack(self):
        print("quack quack")

    def swim(self):
        print("swimming")


if __name__ == "__main__":
    print(help(Duck))
    donald = Duck("Donald")
    pingu = Penguin("Pingu")
    donald.walk()
    donald.fly()
    pingu.walk()


