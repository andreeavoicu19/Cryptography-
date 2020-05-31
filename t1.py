from tkinter import *
from tkinter import messagebox
import string

#Am folosit TKinter pentru interfata aplicatiei

# Fisierele
inputFile = "./input.txt"
outputFile = "./output.txt"

# Culori fereastra
colorBg = "#ffffff"
colorTxt = "#000000"
colorAns = "#A9A9A9"

# Initializarea ferestrei de afisare
root = Tk()
root.title("Caesar/Vigenere Cipher")
root.geometry("750x300")
root['background'] = colorBg

# Top frame
Tops = Frame(root, width = 650,height = 50, bg = colorBg)
Tops.pack(side = TOP)

f1 = Frame(root, width = 220, height = 280, relief = SUNKEN,bg = colorBg)
f1.pack(side = LEFT)

f2 = Frame(root, width = 480, height = 280, relief = SUNKEN,bg = colorBg)
f2.pack(side = LEFT)

# Titlu aplicatie
lblTitle = Label(Tops, font = ('times', 20, 'bold'), text = "Aplicatie de dubla cifrare",
                 fg = colorTxt, bd = 10, anchor = 'w',bg = colorBg)
lblTitle.grid(row = 0, column = 0)

lblQ1 = Label(f1, font = ("times",15,"bold"), text = "Alege cifrul :", fg = colorTxt, anchor = "n", bg = colorBg )
lblQ1.pack(side = TOP)

Label(f1,font = ("times",3,"bold"),text = "  ",bg = colorBg).pack()


# Alegerea cifrului
optionCipher = StringVar()

values = {"Cifrul Caesar":"S-a ales Cifrul Caesar","Cifrul Vigenere":"S-a ales Cifrul Vigenere"}
for text, option in values.items():
        Radiobutton(f1, font = ("times",12,"bold"), text = text, variable = optionCipher, value = option, 
                    fg = colorAns,
                    bg = colorBg, anchor = "w",activebackground = colorBg, 
                    activeforeground = colorTxt).pack(side = TOP, ipady = 5)


Label(f1, font = ("times", 6), text = "  ", bg = colorBg).pack()

Label(f2, font = ("times", 15), text = " Cheie cifrul Caesar", anchor = "center",fg = colorTxt,
      bg = colorBg ).grid(row = 0, column = 0)
caesarCipher = Entry(f2,font = ("times", 15, "bold"), bd = 5,bg = colorBg, fg = colorAns, width = 20)
caesarCipher.grid(row = 0, column = 1)

Label(f2, font = ("times", 2), text = " ", anchor = "center", fg = colorTxt, bg = colorBg ).grid(row = 1, column = 0)

Label(f2, font = ("times",15), text = " Cheie cifrul Vigenere", anchor = "center",fg = colorTxt,
      bg = colorBg ).grid(row = 2, column = 0)
vigenereCipher = Entry(f2, font = ("times", 15), bd = 5, bg = colorBg, fg = colorAns, width = 20)
vigenereCipher.grid(row = 2, column = 1)


# Validarea cheii corespunzatoare cifrului

def verificaCheia():

    optiune = optionCipher.get()
    print(optiune)

    if (optiune == "Cifrul Caesar"):
        if (caesarCipher.get().isnumeric() and (int(caesarCipher.get()) >= 0 and int(caesarCipher.get()) <= 25)):
            print("Cheia este valida.")
            messagebox.showinfo("Info", "Cheia este valida.")
        else:
            messagebox.showerror("Eroare", "Cheia nu verifica conditia.")
            caesarCipher.delete(0, END)
    elif (optiune == "Cifrul Vigenere"):
        regex = re.compile('[@_!#$%^&*()<>0123456789?/\\| }{~:]')
        if (regex.search(vigenereCipher.get()) == None):
            print("Cheia este valida")
            messagebox.showinfo("Info", "Cheia este valida.")
        else:
            messagebox.showerror("Eroare", "Cheia introdusa nu este valida.")
            vigenereCipher.delete(0, END)

# Buton de verificare cheie
Label(f2, font = ("times", 1, "bold"), text = " ", anchor = "center", fg = colorTxt, 
      bg = colorBg).grid(row = 3, column = 0)
validBtn = Button(f2, font = ("times", 12, "bold"), text = "Verifica cheia", fg = colorAns, bg = colorTxt, 
                  anchor = "e", bd = 5,
                  padx = 32, activebackground = colorAns, activeforeground = colorBg, 
                  command = verificaCheia).grid(row = 4, column = 2, columnspan = 2, padx = 3, pady = 3)


# Ia in considerare atat majusculele, cat si minusculele
characters = string.ascii_lowercase + string.ascii_uppercase

# Criptare/decriptare Cifrul Caesar

def caesarCipher(text, key, characters, decrypt = False, shift_type = "right"):

    if key < 0:
        print("key cannot be negative")
        return None
    # numarul total de litere
    n = len(characters)
    if decrypt == True:
        key = n - key
    if shift_type == "left":
        # daca se doreste decriptarea, se inverseaza semnul cheia pentru ca shiftarea sa fie spre stanga
        key = -key
    table = str.maketrans(characters, characters[key:] + characters[:key])
    translated_text = text.translate(table) # textul rezultat

    return translated_text

# Cifrul Vigenère

def vigenereCipher(text, keys, decrypt = False):

    n = len(keys)
    translatedText = " "
    i = 0  # retine numarul de litere procesate pana la momentul respectiv

    # itereaza la fiecare litera din text
    for c in text:

        if c.islower() or c.isupper():

            shift = keys[i % n]  # decide ce cheie sa fie folosita

            if decrypt == True:
                # in cazul in care se doreste decriptarea, se face cheia negativa
                shift = -shift

            # realizeaza shiftarea
            shifted_c = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))

            translatedText += shifted_c

            i += 1
        # in cazul spatierii
        else:

            translatedText += c

    return translatedText


def cripteaza():

    with open(inputFile, "r") as f_in:
        if optionCipher.get() == "Caesar":
            with open(outputFile, "w") as f_out:
                for line in f_in:
                    lineNew = caesarCipher(line, 3, characters, decrypt = False, shift_type = "right")
                    f_out.write(lineNew)
        else:
            with open(outputFile, "w") as f_out:
                for line in f_in:
                    lineNew = vigenereCipher(line, [1,2,3],  decrypt = False)
                    f_out.write(lineNew)

def decripteaza():

    with open(inputFile, "r") as f_in:
        if optionCipher.get() == "Caesar":
            with open(outputFile, "w") as f_out:
                for line in f_in:
                    lineNew = caesarCipher(line, 3, characters, decrypt= True, shift_type = "left")
                    f_out.write(lineNew)
        else:
            with open(outputFile, "w") as f_out:
                for line in f_in:
                    lineNew = vigenereCipher(line, [1,2,3], decrypt = True)
                    f_out.write(lineNew)



butonCriptare= Button(f2, font = ("times", 12), text = "Cripteaza", fg = colorAns, bg = colorTxt, anchor = "e", bd = 5,
                    width = 5, padx = 40, activebackground = colorAns, activeforeground = colorBg,
                    command = cripteaza).grid(row = 6, column = 1, padx = 3, pady = 3)

butonDecriptare = Button(f2, font = ("times", 12), text = "Decripteaza", fg = colorAns, bg = colorTxt, anchor = "e", bd = 5,
                    width = 5, padx = 40, activebackground = colorAns, activeforeground = colorBg,
                    command = decripteaza).grid(row = 6, column = 2, padx = 3, pady = 3)

root.mainloop()
