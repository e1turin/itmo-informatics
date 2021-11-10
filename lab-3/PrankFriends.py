import Exeptions


def listprank(group: str, listing: str) -> None:
    if not group:
        raise Exeptions.InputError(f"Input group: {group}", "Write not empty group or use 'main' function in module")
    if not listing:
        raise Exeptions.InputError(f"Input list: {listing}", "Write not empty list or use 'main' function in module")
    main(group, listing)


def main(group: str = "", listing: str = "") -> None:
    """
    Функция принимает название группы (строка) и список человек (строка с разделителями в виде '\n'),

    если название группы не задано, предложит ввести,
    если список не задан, предложит ввести построчно

    Ничего не возвращает, выводит на экран измененный список
    """
    import re


    if not group:
        group = input("Write your group:").strip()

    __group: str = group or "P3110"


    text: list = []
    tabulation: int = 0
    if listing:
        lines = list(listing.split('\n'))
        for line in lines:
            tabulation = len(line) - len(line.lstrip())-1  # используем для выравнивания списка
            line = line.strip()
            if line:
                text.append(line)

    else:
        temp = input("Write list of students: ")
        while temp:
            text.append(tuple(temp.strip()))
            temp = input()

        if not text:
            text = ["Петров П.П. P3110",
                    "Анищенко А.А. P33113",
                    "Примеров Е.В. P3110",
                    "Иванов И.И. P3110"]


    for i in range(len(text)):
        _, surname, name_short, middlename_short, group, _ = re.split(r"(\w+) (\w).(\w). (.+)", text[i])
        # _ - ненужная переменная в которую записывается пустая строка (нюанс поиска регулярного выражения)

        if name_short == middlename_short and group == __group:
            continue
        print(' '*tabulation, text[i])



if __name__ == "__main__":
    main()
