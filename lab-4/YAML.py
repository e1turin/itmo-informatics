import _io
import enum
import exeptions


# TODO extends from enum.Enum
class LineType():
    KEY = 1
    VALUE = 2
    LISTELEMENT = 3


def parseline(line: str) -> dict[str:int, str:int, str:list[int], str:int | str | None]:
    # returns tuple with line level, list of types, key, value
    line = line.rstrip()
    level = None
    linetypes = []
    key = ""
    value = ""

    level = len(line) - len(line.lstrip())
    if line.lstrip()[0:2] == "- ":
        linetypes.append(LineType.LISTELEMENT)
        level += 2

    line = line[level:]

    divindex = line.find(':')
    key = line[:divindex]

    if divindex != -1:
        linetypes.append(LineType.KEY)
        """
        None
        for i in range(len(line)):
            # YAML lines always consists ":"
            if line[i] == ":":
                key = line[:i]
                divindex = i
                linetypes.append(LineType.KEY)
                break
        """

        value = line[divindex + 1:].strip()

    if value.isalnum():
        # value processing
        value = int(value)
    else:
        value = value.strip('"') or None

    if value:
        linetypes.append(LineType.VALUE)

    return {"level": level, "types": linetypes, "key": key, "value": value}


def _createNode(elements: list, start: int) -> tuple[dict, int]:
    # функция строит нод (словарь): subtree для элемента в списке с номером start
    subtree: dict = dict()
    stop: int = start  # певый элемент в рассмотрении, позже увеличим, рассматриваем следующий за start
    subtree.update({elements[start]["key"]: elements[start]["value"]})
    # создаем в пустом subtree элемент из-за которого мы вошли в функцию,
    # инициируем его как {key: value | None}

    while stop < len(elements):  # пока не вышли за границы
        stop += 1
        if stop < len(elements) and elements[stop]["key"]:  # если не пустая строка, то продолжаем, иначе скипаем
            if LineType.LISTELEMENT in elements[stop]["types"]:
                # если текущая рассматриваемая строка - массив
                el, stop = _createNode(elements, stop)
                # получили нод - элемент списка и шагнули до следующего элемента списка или понижения уровня
                if not subtree[elements[start]["key"]]:
                    # корневой нод не инициализирован (None | "", но пустой строки быть не может)
                    subtree[elements[start]["key"]] = []
                try:
                    print(subtree)
                    subtree[elements[start]["key"]].append(el)  # добавили в массив сформированный нод
                except AttributeError:
                    raise exeptions.YamlFormatError(f"elements: {elements[start]} subtree: {subtree}, el: {el}",
                                                    f"incorrect yaml-file formatting in line: ±{stop}")
                except:
                    print("_____________________subtree[elements[start][key]]?__________")

            else:  # если текущая рассматриваемая строка не массив, а самостоятельный объект
                if elements[stop]["level"] == elements[start]["level"]:
                    # если уровни текущей и строки и той для которой строим нод (корневой) совпадают
                    subtree.update({elements[stop]["key"]: elements[stop]["value"]})
                    # добавляем рассматриваемый элемент в корневой нод
                elif elements[stop]["level"] > elements[start]["level"]:
                    # если рассматриваемы нод - потомок предыдущего
                    el, stop = _createNode(elements, stop)
                    # создаем новый нод и шагаем до следующего элемента в текущем объекте или в до братского нода

                    rootelkey = tuple(subtree.keys())[-1]  # последний добавленный в subtree елемент - предок найденного
                    subtree.update({rootelkey: el})  # добавляем потомка нашему текущему элементу в корневом ноде

                elif elements[stop]["level"] < elements[start]["level"] or LineType.LISTELEMENT in elements[stop]["types"]:
                    # если (уровень седующего меньше - встретили прародственника) или (встретили другой список)
                    # ! рассматриваем всегда непустой элемент
                    return subtree, stop


    return subtree, stop


def createDict(elements: list) -> dict:
    tree = dict()
    tree.update({'__DATA__': None})

    for i in range(len(elements)):
        if not elements[i]["key"]:
            continue
        else:
            # строим дерево для первого ненулевого элементра
            tree['__DATA__'] = _createNode(elements, i)[0]
            break

    return tree


def parse(file: str | _io.TextIOWrapper) -> dict | None:
    elementTree = dict()
    elements = []

    if type(file).__name__ == "TextIOWrapper":
        for line in file.readlines():
            elements.append(parseline(line))


    elif type(file).__name__ == "str":
        pass
    else:
        return None

    elementTree = createDict(elements)
    for i in elements:
        print(i)
    print(elementTree)
