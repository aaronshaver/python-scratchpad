import sys


def stringify(grid):
    output = ''
    for line in grid:
        for char in line:
            output += char
        output += '\n'
    return output[:-1]  # remove extra line break


def join_text(text):
    char = ''
    if len(text) > 1:
        char = ' '
    output = ''
    for word in text:
        if len(word) > 1:
            word = ''.join(word)
        else:
            word = word[0]
        output += word + char
    output = output.rstrip()  # strip last space
    return output


def radial_print(*text):

    # return null if we receive null, empty string if empty string
    if not text:
        return None
    elif text[0] == '':
        return ''

    if isinstance(text[0], basestring):  # to support passing in a string
        text = list(text)
    elif isinstance(text, tuple):  # support multi-word input
        text = text[0]

    text = join_text(text)
    text_length = len(text)

    grid_side_length = (text_length * 2) - 1

    # initialize grid
    grid = [[' ' for x in range(grid_side_length)]
            for y in range(grid_side_length)]

    origin_coord = text_length - 1
    x, y = origin_coord, origin_coord

    j = 0
    for i in range(text_length):
        if i == 0:
            grid[y][x] = text[0]
        else:
            grid[y][x-i] = text[j]  # left
            grid[y][x+i] = text[j]  # right
            grid[y+i][x] = text[j]  # down
            grid[y-i][x] = text[j]  # up
            grid[y-i][x-i] = text[j]  # up+left
            grid[y-i][x+i] = text[j]  # up+right
            grid[y+i][x+i] = text[j]  # down+right
            grid[y+i][x-i] = text[j]  # down+left
        j += 1
    return stringify(grid)


if __name__ == "__main__":
    if len(sys.argv) < 2:  # no input
        print('Please supply text to radial print')
    else:
        print(radial_print(sys.argv[1:]))
