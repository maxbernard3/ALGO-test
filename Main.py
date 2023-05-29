from PIL import Image
import requests


img_data = requests.get("https://game.algosup.com/users/33CP9ghQ6SW7kcYJI65z/bitmap").content
with open('game_image.png', 'wb') as handler:
    handler.write(img_data)
filename = "game_image.png"

img = Image.open(filename)


def visualize(table):
    table = zip(*table)

    for row in table:
        tostr = ''.join(str(x) for x in row)
        tostr = tostr.replace(",[]", "")
        tostr = tostr.replace("4", ". ")
        tostr = tostr.replace("0", "↑ ")
        tostr = tostr.replace("1", "↓ ")
        tostr = tostr.replace("2", "→ ")
        tostr = tostr.replace("3", "← ")
        print(tostr)


def get_direction(x, y):
    if img.getpixel((x + 25, y + 40))[0] == 0 and img.getpixel((x + 25, y + 10))[0] > 0:
        # up
       return 0
    elif img.getpixel((x + 25, y + 10))[0] == 0 and img.getpixel((x + 25, y + 40))[0] > 0:
        # down
        return 1
    elif img.getpixel((x + 10, y + 25))[0] == 0 and img.getpixel((x + 40, y + 25))[0] > 0:
        # right
        return 2
    elif img.getpixel((x + 40, y + 25))[0] == 0 and img.getpixel((x + 10, y + 25))[0] > 0:
        # left
        return 3
    return 4


def build_res_arr():
    res = []
    for x in range(10):
        colum = []
        for y in range(10):
            colum.append(get_direction(x * 50, y * 50))
        res.append(colum)
    return res


def check_grid(table):
    for i in table:
        for j in i:
            if not j == 4:
                return False
    return True


def next_move(pos, table):
    direction = table[pos[0]][pos[1]]
    table[pos[0]][pos[1]] = 4
    result = False

    if check_grid(table):
        result = True
        return result

    if direction == 0:
        for i in reversed(range(pos[1])):
            if not table[pos[0]][i] == 4:
                result = next_move((pos[0], i), table)
        return result
    elif direction == 1:
        for i in range(pos[1], 10):
            if not table[pos[0]][i] == 4:
                result = next_move((pos[0], i), table)
        return result
    elif direction == 2:
        for i in range(pos[0], 10):
            if not table[i][pos[1]] == 4:
                result = next_move((i, pos[1]), table)
        return result
    elif direction == 3:
        for i in reversed(range(pos[0])):
            if not table[i][pos[1]] == 4:
                result = next_move((i, pos[1]), table)
        return result
    else:
        print("not a good starting square")


def bruteforce(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if not table[i][j] == 4:
                res = next_move((i, j), table)
                if res:
                    return i, j


a = build_res_arr()
visualize(a)
print("------")
res1, res2 = bruteforce(a)

print(f"result = ({res1}, {res2})")

