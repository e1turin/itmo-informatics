import re
def main():
    eyes = {0: ':', 1: ';', 2: 'X', 3: '8', 4: '='}
    noses = {0: '-', 1: '<', 2: '-{', 3: '<{'}
    mouthes = {0: '(', 1: ')', 2: 'O', 3: '|', 4: '\\', 5: '/', 6: 'P'}

    isu_id = int(''.join(input("Write your isu id: ").strip().split()) or "335047")

    smile = f"{eyes[isu_id%5]}{noses[isu_id%4]}{mouthes[isu_id%7]}"

    print("Your smile is:", smile)

    if input("Should I drow smile? [y/n]: ").lower() in ('y','Y','Yes'):

        import tkinter

        window = tkinter.Tk()
        window.title(f"Smile variant №{isu_id}")
        window.geometry("300x250")

        label = tkinter.Label(window, text=smile, font=("Arial Bold", 100))

        label.grid(column=2, row=1)

        window.mainloop()

    print("Write your text, I'll find smiles in it:")
    text = input().strip()

    matches = re.findall(fr"{smile}", text)

    print("I found", len(matches), "smiles.")




    print(f"Good bye, {smile}")
    



if __name__ == "__main__":
    main()
