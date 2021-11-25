def main() -> None:
    """
    Функция по введенному номеру ИСУ строит смайлик
    предлагает нарисовать его в tkinter
    предлагает подсчитать количество вхождений смайлика в введенную строку
    """
    import re


    eyes: dict[int: str] = {0: ':', 1: ';', 2: 'X', 3: '8', 4: '='}
    noses: dict[int: str] = {0: '-', 1: '<', 2: '-{', 3: '<{'}
    mouthes: dict[int: str] = {0: '(', 1: ')', 2: 'O', 3: '|', 4: '\\', 5: '/', 6: 'P'}

    isu_id: int = int(''.join(input("Write your isu id: ").strip().split()) or "335047")

    smile: str = f"{eyes[isu_id % 5]}{noses[isu_id % 4]}{mouthes[isu_id % 7]}"

    print("Your smile is:", smile)

    if input("Should I drow smile? [y/n]: ").lower() in ('y', 'Y', 'Yes'):
        import tkinter

        window = tkinter.Tk()
        window.title(f"Smile variant №{isu_id}")
        window.geometry("300x250")

        label = tkinter.Label(window, text=smile, font=("Arial Bold", 100))

        label.grid(column=1, row=1)

        window.mainloop()

    print("Write your text, I'll find smiles in it, or I'll use my own:")
    text = input().strip()
    if text:
        matches = re.findall(fr"{smile}", text)
        print("I found", len(matches), "smiles.")

    else:  # using default example
        text = ["dsfjasdjkfk" + smile + "ksdf" + smile + "Skd[}sdjflk}{x!",
                "23jlkds][]sdaf@43042" + smile + ";'23=[}}{}2341X{32=-0",
                smile + smile + "df{X320(!" + smile + "vcxlkasdfnvX{]2",
                "svcsx3p[]234$*(}" + smile + smile + smile + smile + "sxcvm",
                "asf][cX]a-]C]X}sfdasdkf{DFSc]C}ZX}}D#}WE}R}ZXX"]

        for t in text:
            print("I use text: ", t)
            matches = re.findall(fr"{smile}", t)
            print("I found", len(matches), "smiles.")
            print("---------")

        print("[Right answers: 2, 1, 3, 4, 0]")
        print()

    print(f"Good bye, {smile} !")


if __name__ == "__main__":
    main()
