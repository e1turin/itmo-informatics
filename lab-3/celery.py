def main(arg=None):
    import re

    # text = input().strip()
    if not arg:
        text=''
        temp=input().strip()
        while temp:
            text = text + ' ' + temp
            temp = input().strip()
    else:
        text = arg


    words = re.split(r"(\w+)(\W)", text)

    new_text = []
    new_text.append(words[0])

    for i in range(1, len(words)-1):
        if words[i] in ( '', ' ') or new_text[-1].lower() == words[i].lower():
            continue
        
        else:
            new_text.append(words[i].strip())

    # print(words)
    # print(new_text)

    print(re.sub(r" (?=[.,?';!])", '', ' '.join(new_text)).replace('  ', ' ').strip())


if __name__=="__main__":
    main()
