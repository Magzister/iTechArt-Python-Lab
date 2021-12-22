class FileWorker():
    """FileWorker is a wrapper over functions for working with files."""

    def __init__(self, filename=None, mode='rt'):
        self._file_object = None
        if filename:
            self.open(filename, mode)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()
        return False

    def open(self, filename, mode='rt'):
        """Open function provides the ability to open the file.

        Arguments:
            filename -- Name of the file.
        Keyword arguments:
            mode -- File open mode.
        """

        if self._file_object:
            self._file_object.close()
        try:
            self._file_object = open(filename, mode)
        except FileNotFoundError as e:
            print(e)

    def write(self, text):
        """Write fuction provides the ability to write data to file.

        Arguments:
            text -- Data to be written to the file.
        """

        if self._file_object:
            try:
                self._file_object.write(text)
            except Exception as e:
                print(e)
        else:
            print("Open file first!")

    def read(self, size=-1):
        """Read function provides the ability to read data from file.

        Arguments:
            size -- Amount os bytes in binary mode and
                    amount of letters in normal mode.
        """

        if self._file_object:
            try:
                text = self._file_object.read(size)
                return text
            except Exception as e:
                print(e)
        else:
            print("Open file first!")

    def seek(self, n):
        """Seek function moves the pointer to the specific position.

        Arguments:
            n - The position in the file.
        """

        if self._file_object:
            return self._file_object.seek(n)
        else:
            print("Open file first!")

    def tell(self):
        """Tell function returns current pointer position in file."""

        if self._file_object:
            return self._file_object.tell()
        else:
            print("Open file firest!")

    def close(self):
        """Close function closes the file if it is open."""
        if self._file_object:
            self._file_object.close()
            self._file_object = None

    def __del__(self):
        self.close()


if __name__ == '__main__':
    worker = FileWorker()
    worker.open('./1', mode='w')
    worker.write('123')
    worker.close()
    worker.open('./1', mode='r')
    data = worker.read()
    print(data)

    print("-" * 32)

    worker.open('./2', mode='a+')
    worker.open('./2', mode='a+')
    worker.write('123')
    worker.seek(0)
    data = worker.read()
    print(data)

    print("-" * 32)

    with FileWorker('./2', mode='a+') as worker:
        worker.write('123')
        worker.seek(0)
        data = worker.read(2)
        print(data)
