import sys


class RadialPrint:

    @staticmethod
    def radial(text):
        size = (len(text) * 2) - 1
        return text


if __name__ == "__main__":

    print(RadialPrint.radial(sys.argv[0]))
