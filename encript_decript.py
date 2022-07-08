characterMap = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
    "G": 16,
    "H": 17,
    "I": 18,
    "J": 19,
    "K": 20,
    "L": 21,
    "M": 22,
    "N": 23,
    "O": 24,
    "P": 25,
    "Q": 26,
    "R": 27,
    "S": 28,
    "T": 29,
    "U": 30,
    "V": 31,
    "W": 32,
    "X": 33,
    "Y": 34,
    "Z": 35,
    " ": 36,
    ",": 37,
    ".": 38,
    "_": 39,
    "-": 40,
    "?": 41,
    "(": 42,
    ")": 43,
    "'": 44,
    '"': 45,
    "+": 46,
    "=": 47,
    "-": 48,
    "*": 49,
    "a": 51,
    "b": 52,
    "c": 53,
    "d": 54,
    "e": 55,
    "f": 56,
    "g": 57,
    "h": 58,
    "i": 59,
    "j": 60,
    "k": 61,
    "l": 62,
    "m": 63,
    "n": 64,
    "o": 65,
    "p": 66,
    "q": 67,
    "r": 68,
    "s": 69,
    "t": 70,
    "u": 71,
    "v": 72,
    "w": 73,
    "x": 74,
    "y": 75,
    "z": 76,
    "{": 77,
    "}": 78,
    "[": 79,
    "]": 80,
    "!": 81
}


def encript(key):
    encripted = ""
    for i in range(len(key)):
        try:
            encripted += f"{characterMap[key[i]]}"
        except:
            return f"{key[i]} cant encode"

    return encripted


def decript(key):
    decripted = ""
    n = 0
    while(n < len(key)): 
        number = "" 
        number = str(key[n]) + str(key[n+1]) 
        for item in characterMap:
            if(characterMap[item] == int(number)): 
                decripted += item 
        n += 2
            
        
    return decripted

print(encript("Hello, world!"))
print(decript("17556262653736736568625481"))
