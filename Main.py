import urllib.request as request
from PIL import Image

filename = "test.png"
#response = request.urlretrieve("https://game.algosup.com/users/8Y2cB07WSTPLKz4F6kLX/bitmap", filename)
#print("debug")


img  = Image.open(filename)

def getDirection(x, y):
    if img.getpixel((x + 25, y + 40))[0] == 0 and img.getpixel((x + 25, y + 10))[0] > 0:
        #up
       return 0
    elif img.getpixel((x + 25, y + 10))[0] == 0 and img.getpixel((x + 25, y + 40))[0] > 0:
        #down
        return 1
    elif img.getpixel((x + 10, y + 25))[0] == 0 and img.getpixel((x + 40, y + 25))[0] > 0:
        #right
        return 2
    elif img.getpixel((x + 40, y + 25))[0] == 0 and img.getpixel((x + 10, y + 25))[0] > 0:
        #left
        return 3
    return 4


def buildResArr():
    res = []
    for x in range(10):
        colum = []
        for y in range(10):
            colum.append(getDirection(x*50, y*50))
        res.append(colum)
    return res

def checkGrid(table):
    for i in table:
        for j in i:
            if not j == 4:
                return False
    return True

def nextMove(pos, table):
    dir = table[pos[0]][pos[1]]
    table[pos[0]][pos[1]] = 4

    if checkGrid(table):
        return True

    if dir == 0:
        for i in reversed(range(pos[1])):
            if not table[pos[0]][i] == 4:
                nextMove((pos[0], i), table)
        return False
    elif dir == 1:
        for i in range((pos[1] + 1), 10 - pos[1]):
            if not table[pos[0]][i] == 4:
                nextMove((pos[0], i), table)
        return False
    elif dir == 2:
        for i in range((pos[0] + 1), 10 - pos[0]):
            if not table[i][pos[1]] == 4:
                nextMove((i, pos[1]), table)
        return False
    elif dir == 3:
        for i in reversed(range(pos[0])):
            print(i)
            if not table[i][pos[1]] == 4:
                nextMove((i, pos[1]), table)
        return False
    else:
        return "rip Bozo"

a = buildResArr()
res = nextMove((4,6) ,a)
print("------")
print(res)

