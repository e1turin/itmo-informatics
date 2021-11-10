
def _print_simple(key: str, elem: int | str, count_tabs=0):
    return '\t'*count_tabs + "<{key}>" + str(elem) + f"</{key}>" + '\n'





def _printelem_r(elements: list | dict, key: str='', c: int=0):
    s = ""
    if type(elements).__name__ == "list":
        for el in elements:
            s += '\t'*c + f"<{key}>" + '\n' + \
                    _printelem_r(elements, key, c+1) + '\n' + \
                    '\t'*c + f"/<{key}>" + '\n'


    elif type(elements).__name__ == "dict":
        for k in elements.keys():
            s = '\t'*c + f"<{k}>" + '\n' + \
                _printelem_r(elements[k], k, c+1) + '\n' + \
                '\t'*c + f"</{k}>" + '\n'
    elif type(elements).__name__ in ("str", "int"):
        s += '\t'*c + f"<{key}>" + str(elements) + f"<{key}>" + '\n'

    return s



def create(tree: dict[str: dict | list], inline: bool = False) -> None | str:

    if "__DATA__" in tree.keys():
        _printelem_r(tree["__DATA__"])
    else:
        _printelem_r(tree)


