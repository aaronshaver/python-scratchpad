import sys


class RadialPrint:

    @staticmethod
    def radial(text):
        size = (len(text) * 2) - 1
        if size < 0:
            return ''
        grid = [['.' for x in range(size)] for y in range(size)]

        output = ''
        for line in grid:
            for char in line:
                output += char
            output += '\n'
        output = output[0:-1]
        return output


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(RadialPrint.radial(sys.argv[1]))
    else:
        print('Please supply text to radial print')
