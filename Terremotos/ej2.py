class RadiusImputError(Exception):
    message = "'{radio}' no es un número."

    def __init__(self, radio):
        self.radio = radio
        super().__init__(self.message.format(radio=radio))


class Circle(object):

    def __init__(self, radio):
        self.radio = self.verifyRadio(radio)

    def verifyRadio(self, radio):

        if type(radio) is int:
            return radio
        else:
            raise RadiusImputError(radio)

    def __str__(self):
        return 'Radio: {}'.format(self.radio)


def main():
    try:
        circle = Circle('hello')
        print(circle)
    except RadiusImputError as e:
        print(e)


if __name__ == "__main__":
    main()
