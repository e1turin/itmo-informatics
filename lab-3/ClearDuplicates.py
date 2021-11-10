import Exeptions


def cleartext(text: str):
    if not text:
        raise Exeptions.InputError(f"Input text: '{text}'", "Write not empty text or use 'main' function in module")
    return main(text)


def main(arg: str | None = None) -> str:
    """
    Функция принимает строку или вызывается без аргументов,
    если аргументы не были переданы, то она предлагает ввести текст и преобразует его к одной строке.

    Возвращает исправленный текс (строка) без повторений слов и множественных пробелов.
    * повторением считается слово отделенного от предыдущего одним или больше пробелов, равное ему без учета регистра.
    """
    import re

    text: str = ""
    # text = input().strip()
    if not arg:
        temp = input().strip()
        while temp:  # считываем данные, если они не даны
            text = text + ' ' + temp
            temp = input().strip()
    else:
        text = arg

    text = re.sub(r"  *", r" ", re.sub(r'(?i)(\b.+\b) +\1', r"\1", arg))

    return text


if __name__=="__main__":
    main()
