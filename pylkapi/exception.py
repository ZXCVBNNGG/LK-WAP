class PyLKApiException(Exception):
    def __init__(self, code: int):
        self.code = code
        super(PyLKApiException, self).__init__()

    def __str__(self):
        return f"An exception happened during handling the request! The return code is {self.code}."
