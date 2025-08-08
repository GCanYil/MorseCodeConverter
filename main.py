from tkinter import *

letterToMorse = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".","f":"..-.", "g":"--.", "h":"....", "ı":"..", "j":".---",
                 "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-",
                 "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--..", 
                 "0":"-----", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", 
                 "6":"-....", "7":"--...", "8":"---..", "9":"----.",
                 " ":"/", "&":".-...", "'":".----.", "@":".--.-.", ")":"-.--.-", "(":"-.--.", ":":"---...", ",":"--..--",
                 "=":"-...-", "!":"-.-.--", ".":".-.-.-", "-":"-....-", "%":"⸻   ..- -   ⸻", "+":".-.-.", '"':".-..-.",
                 "?":"..--..", "/":"-..-.", "ç":"-.-..", "ğ":"--.-.", "i":".."}

morseToLetter = {code:letter for letter,code in letterToMorse.items()}

def updateLabel(message):
    final_label.config(text = message)

def transform_LtoM():
    message = message_taken.get()
    translated_version = ""
    try:
        for letter in list(message.lower()):
            translated_version += letterToMorse[letter]
            translated_version += " "
        updateLabel(translated_version)
    except KeyError:
        updateLabel("The message you entered has characters that do not include morse code translation. Please retry.")

def transform_MtoL():
    message = message_taken.get()
    translated_version = ""
    try:
        for letter in message.split():
            translated_version += morseToLetter[letter]
        updateLabel(translated_version)
    except KeyError:
        updateLabel("The message you entered has characters that do not include morse code translation. Please retry.")
    
root = Tk()
root.title("Morse Code Converter")

label = Label(root, text="Welcome to Morse Code Converter!")
label.grid(row=0, column=0, columnspan=2,padx=20, pady=20)

letter_morse_button = Button(root, text="Letter to Morse", command=transform_LtoM)
letter_morse_button.grid(row=2,column=0, padx=20, pady=10)

morse_letter_button = Button(root, text="Morse to Letter", command=transform_MtoL)
morse_letter_button.grid(row=2,column=1, padx=20, pady=10)

message_taken = Entry(root, width=100)
message_taken.grid(row=1, column=0, columnspan=2, padx=20)

final_label = Label(root, text="")
final_label.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

root.mainloop()