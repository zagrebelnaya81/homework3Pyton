"""
high level support for doing this and that.
"""


class Rectangle:
    def __init__(self):
        self.i = 0

    def print_square(self, length):
        """ Function will display a square of the given size on the screen """
        if length == 1:
            print("*")
            return
        if length == 2:
            print("*" * 4)
            return
        if self.i == 0:
            print("* " * length)
        print("* " + "  " * (length - 2) + "*")
        if self.i == length - 3:
            print("* " * length)
        self.i = self.i + 1
        if self.i < length - 2:
            self.print_square(self, length)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    r = Rectangle()
    print(r.print_square(4))
