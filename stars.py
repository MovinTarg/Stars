x = [4, 6, 1, 3, 5, 7, 25]
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
z = ["Tom", "Michael", "Jimmy Smith"]

def stars(arr):
    for val in arr:
        newStr = ""
        for count in range (0, val):
            newStr += "*"
        print newStr
stars(x)

def stars(arr):
    for val in arr:
        newStr = ""
        for letter in val:
            if letter == val[0]:
                newStr += letter*len(val)
        print newStr
stars(z)

def draw_stars(arr):
    for val in arr:
        newStr = ""
        if isinstance(val, int):
            for count in range (0, val):
                newStr += "*"
            print newStr
        else:
            for letter in val:
                if letter == val[0]:
                    newStr += letter.lower()*len(val)
            print newStr
draw_stars(y)