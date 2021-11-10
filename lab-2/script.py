class Error(Exception):
    pass


class InputError(Error):
    """Exception raised for errors in the input, unfit quantity.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TypeError(Error):
    """Exception raised for errors in the input, unfit elements type.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


def main():

    i_bits = tuple(map(int, ''.join(input("Write received message: ").strip().split())))

    if len(i_bits) != 7:
        raise InputError(i_bits, f"Were expected 7 bits, got {len(i_bits)}!")


    if not all(i_bits[i] in (0, 1) for i in range(len(i_bits))):
        raise TypeError(i_bits, f"Non bit string: {i_bits}")

    message = dict(zip(( "r1", "r2", "i1", "r3", "i2", "i3", "i4"), i_bits))

    sindrome = {
            "s1" : message["r1"] ^ message["i1"] ^ message["i2"] ^ message["i4"],\
            "s2" : message["r2"] ^ message["i1"] ^ message["i3"] ^ message["i4"],\
            "s3" : message["r3"] ^ message["i2"] ^ message["i3"] ^ message["i4"]
            }

    mistake_bit_numder = int(f"{sindrome['s1']}{sindrome['s2']}{sindrome['s3']}"[::-1], 2)
    
    if mistake_bit_numder:
        print(f"Mistake is in {mistake_bit_numder} bit.")

        print(f"Original message: ", end='')

        for i in range(len(i_bits)):
            if i == mistake_bit_numder - 1:
                print(1 ^ i_bits[i], end="")
                continue
            print(i_bits[i], end="")
        print()

    else:
        print("There is no mistakes in message.")
    
    pass
    

if __name__ == "__main__":
    main()
