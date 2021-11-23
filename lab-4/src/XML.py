import _io
from src import exceptions


def _print(key: str | None, value: int | str | dict | list | None, output: _io.TextIOWrapper = None,
           makesinglestring: bool = False):
    """
    Вспомогательный метод получает строку содержащую имя нода (key) и его содержимое (value),
    файл в который нужно вывести результат, флаг, отвечающий за возвращение XML в виде одной строки

    если выходной файл не задан, то вывод осуществляется в стандартный поток вывода

    рекурсивно выводит нод с именем key с содержимым value в формате XML внутри тега <key></key>,
    """
    xmlstring: str = ''  # не используется, если не установлен флаг makesinglestring=True

    valtype = type(value).__name__
    if valtype in ("int", "str", "NoneType"):
        if makesinglestring:
            xmlstring = f"<{key}>" + str(value) + f"</{key}>"
            return xmlstring

        print(f"<{key}>", end="", file=output)
        print(value, end="", file=output)
        print(f"</{key}>", file=output)

    elif valtype == "list":
        for i in range(len(value)):
            if makesinglestring:
                xmlstring += f"<{key}>" + _print(None, value[i], output,
                                                 makesinglestring=makesinglestring) + f"</{key}>"
                continue
            print(f"<{key}>", file=output)
            _print(None, value[i], output)
            print(f"</{key}>", file=output)

        if makesinglestring:
            return xmlstring

    elif valtype == "dict":
        for k, v in value.items():
            if makesinglestring:
                xmlstring += f"<{key}>" + _print(k, v, output, makesinglestring=makesinglestring) + f"</{key}>"
                continue
            if key:
                print(f"<{key}>", file=output)
                _print(k, v, output)
                print(f"</{key}>", file=output)
            else:
                _print(k, v, output)

        if makesinglestring:
            return xmlstring


def create(elements: dict, root: str = "", file: _io.TextIOWrapper = None, singlestring: bool = False) -> None | str:
    """
    Метод получает словарь, представляющий древовидную структуру,
    имя корневого элемента, по умолчанию пустая строка (не выводится)
    может возвращать XML файл в одноу строку

    если не указан выходной файл file, то вывод происходит в стандартный поток.
    если не установлен фалг singlestring=True, то метод возвращает None, инача возвращает строку содержащую XML

    по умолчанию ничего не возвращает.
    """

    elementsroot = list(elements.keys())
    if len(elementsroot) > 1:
        raise exceptions.DataFormatError("elements keys: " + str(elements.keys()),
                                        'Wrong assets format, too much root points, should be 1 called "__DATA__"')
    if elementsroot[0] != "__DATA__":
        print(exceptions.Warn("Elements root point: " + str(elementsroot[0]),
                             "Warning! non-standard format ('__DATA__')"))
    tree = {root: elements[elementsroot[0]]}

    print('<?xml version = "1.0" ?>', file=file)
    return _print(None, tree, file, makesinglestring=singlestring)
