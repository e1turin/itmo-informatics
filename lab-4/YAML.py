import _io
# import enum
import exeptions


# TODO extends from enum.Enum
class LineType:
    KEY = 1
    VALUE = 2
    LISTELEMENT = 3


def parseline(line: str) \
        -> dict[str:int, str:int, str:list[int], str:int | str | None]:
    """
    Метод получает строку из YAML файла, преобразует ее в картежу в формате:
    (уровень строки, список типов строки, ключ, значение)

    Уровень строки - размер отступа от начала строки (количество побелов)
    Список типов - свойства, которыми обладает строка (имеет ключ, имееет значение, является первым элементом списка)
    Ключ - ключ элемента в YAML файле в текущей строке
    Значение - значение элемента в YAML файле (None, если в строке посде ":" ничего смыслового не следует)

    возвращает словарь содержащий соответственно ключам "level", "types", "key", "value"
    - уровень строки, список типов, ключ, значение
    """

    # Инициализация
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

    if divindex != -1:
        key = line[:divindex]
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

        # TODO вставка '"' в знаение ключа (удалять только один сивмол кавычек в начале и конце)
        value = line[divindex + 1:].strip()

    if value.isdecimal():  # обработка значения (парсинг числа, строки, пустого значения (None))
        # TODO парсинг числа с "-", "0x..." нотация
        value = int(value)
    else:
        # TODO пустая строка в значении - не None
        value = value.strip('"') or None

    if value:  # добавление типа строки (имеет значение ключа)
        linetypes.append(LineType.VALUE)

    return {"level": level, "types": linetypes, "key": key, "value": value}


def _createNode(elements: list[dict[str: int, str: list[int], str: str, str: str]], start: int) \
        -> tuple[dict[dict | list | str], int]:
    """
    Вспомогательный метод строит нод subtree (словарь словарей и массивов) для элемента в списке с номером start
    [0 <= start < len(elements)]

    находит stop (int) - номер строки, в которой закончена обработка [start < stop <= len(elements)]
    TODO: must: stop < len(elements)

    возвращает tuple(subtree, stop)
    """

    subtree: dict = dict()  # новый нод (словарь)
    stop: int = start  # номер элемент в рассмотрении, всегда больше start, увеличивается в цикле
    subtree.update({elements[start]["key"]: elements[start]["value"]})
    # создаем в пустом subtree элемент из-за которого мы вошли в функцию,
    # инициируем его как {key: value | None}
    rootelkey: str = elements[start]["key"]
    # последний добавленный в subtree елемент (предок нового найденного элемента в искомых случаях необходимости)

    while stop < len(elements):  # пока не вышли за границы
        stop += 1  # делаем шаг к следующей строке
        currstop = stop  # переменная для отладки

        # TODO delete stop < len(elements)
        if stop < len(elements) and elements[stop]["key"]:  # проверка на пустую строку (отсутсвует ключ перед ":")

            if LineType.LISTELEMENT in elements[stop]["types"]:  # проверка типа строки (является элементом списка)
                if LineType.LISTELEMENT in elements[start]["types"] and \
                        elements[start]["level"] == elements[stop]["level"]:
                    # проверка для прекращения создания нода,
                    # срабатывает, когда в ноде списка доходит до начала следующего нода
                    return subtree, stop

                if not subtree[rootelkey]:
                    # корневой нод не инициализирован (None) тогда инициализируем массивом
                    subtree[rootelkey] = []

                # TODO обработка вложенных списков:
                """ 
                    | file.yaml:                |
                    |---------------------------|
                    |el0:                       |
                    |  - el1:                   |
                    |    - el12:                |
                    |      el13:                | 
                    |        - el134: "val134"  |
                    |          el135: "val135"  |
                    |___________________________|     
                    
                    _createNode(...file.yaml...) --(неверное поведение)-> {el0: [{el1: None}, {el2: None, el13: None}, {el134: "val134", el135: "val135"}]}
                """
                while stop < len(elements) and LineType.LISTELEMENT in elements[stop]["types"]:
                    # дополняем массив новыми нодами, пока каждая обработка нода заканчивается на новом элементе списка
                    el, stop = _createNode(elements, stop)
                    # получили нод - элемент списка и шагнули до следующего элемента списка или понижения уровня

                    # Обработка неверного формата yaml-файла - TODO
                    try:
                        subtree[rootelkey].append(el)  # добавили в массив сформированный нод
                    except AttributeError:
                        raise exeptions.YamlFormatError(
                            f" по ключу 'rootelkey': {rootelkey}, пытаюсь .append(el) в subtree[rootelkey]: {subtree[rootelkey]} | cтрою нод для строки start: {start}+1, elements[start]: {elements[start]} | получаю нод subtree: {subtree} | el: {el}",
                            f"incorrect yaml-file formatting in line: ±{currstop}, may be in line: ±{start},may be other place, idk")

                    except:
                        print("___________ FINDME ___________")

            else:  # если текущая рассматриваемая строка не начало списка, а самостоятельный объект
                if elements[stop]["level"] == elements[start]["level"]:
                    # если уровни текущей и строки и той для которой строим нод (корневой) совпадают
                    subtree.update({elements[stop]["key"]: elements[stop]["value"]})
                    # добавляем рассматриваемый элемент в корневой нод
                    rootelkey = elements[stop]["key"]  # обновили ключ последнего элемента в списке

                # TODO: обработка вложенных листов
                elif elements[stop]["level"] > elements[start]["level"]:
                    # если рассматриваемы нод - потомок предыдущего
                    el, stop = _createNode(elements, stop)
                    # создаем новый нод и шагаем до следующего элемента в текущем объекте или в до братского нода

                    subtree.update({rootelkey: el})  # добавляем потомка нашему текущему элементу в корневом ноде

                # TODO this for example vvv
                elif elements[stop]["level"] < elements[start]["level"]:
                    # встретили прародственника - обрабатываемый нод закончился
                    return subtree, stop
                # TODO examaple:
                """ 
                    | file.yaml:                |
                    |---------------------------|
                    |el0:                       |
                    |  - el01: "val01"          |
                    |el1:                       |
                    |  - el12: "val12"          | 
                    |    el13: "val13"          |
                    |    el14: "val14"          |
                    |___________________________|     

                    _createNode(...file.yaml...) --(неверное поведение)-> {el0: [{el1: "val01"}, {el12: "val12", el13: "val13", el14: "val14"}]}
                """

    return subtree, stop


def _createDict(elements: list[dict[str: int, str: list[int], str: str, str: str]]) -> dict[dict | list]:
    """
    Вспомогательный метод получает список подготовленных строк формата: dict({"level": int, "types": list[int], "key": str, "value": str})

    Возвращает дерево построенное по заданным строкам
    """
    tree: dict = dict()  # инициализируем дерево
    tree.update({'__DATA__': None})  # создаем корневой элемент (необходимо для поддержки неименованных списков)

    for i in range(len(elements)):  # пропускаем все пустые строки (не имеющие ключа)
        if not elements[i]["key"]:
            continue
        else:
            # строим дерево для первого ненулевого элементра
            tree['__DATA__'], _ = _createNode(elements, i)  # запускаем рекурсивное создание нодов
            break

    return tree


def parse(file: _io.TextIOWrapper | str) -> dict[dict | list] | None:
    """
    Метод для парсинга структуры данных из фацла YAML
    получает на вход объект файла или строку
    TODO: работа со входной строкой

    возвращает словарь словарей и массивов, где в единственном элементе с ключом '__DATA__'
    находится обработанная структура
    """

    elementTree: dict = dict()
    elements: list = []

    if type(file).__name__ == "TextIOWrapper":  # Определение типа входных данных
        for line in file.readlines():
            elements.append(parseline(line))

    # TODO:
    elif type(file).__name__ == "str":
        print("TODO")
        return None

    else:
        print("Wrong input type")
        return None

    elementTree = _createDict(elements)
    # запуск вспомогательного метода для создания словаря по обработанным строкам

    return elementTree
