class Error(Exception):
    pass


class YamlFormatError(Error):
    """Exception raised for errors in the input file format.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
