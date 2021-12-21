class FileWorker():
    def __init__(self):
        self._file_object = None
        self._mode = ''

    def open(self, filename, create=False, read=True):
        self._mode = 'r'
        if create and not read:
            self._mode = 'w'
        elif not create and not read:
            self._mode = 'a'
        elif create and read:
            self._mode = 'w+'

        try:
            self._file_object = open(filename, self._mode)
        except FileNotFoundError as e:
            print(e)

    def write(self, text):
        if self._file_object:
            if self._mode in 'wa' or self._mode == 'w+':
                self._file_object.write(text)
            else:
                print("It's not allowed to write in file with read openmode!")
        else:
            print("Open file first!")

    def read(self, size=-1):
        if self._file_object:
            if self._mode == 'r' or self._mode == 'w+':
                text = self._file_object.read(size)
                return text
            else:
                print("It's not allowed to read from file with write openmode!")
        else:
            print("Open file first!")

    def seek(self, n):
        if self._file_object:
            return self._file_object.seek(n)
        else:
            print("Open file first!")

    def tell(self):
        if self._file_object:
            return self._file_object.tell()
        else:
            print("Open file firest!")

    def close(self):
        if self._file_object:
            self._file_object.close()
            self._file_object = None

    def __del__(self):
        self.close()

if __name__ == '__main__':
    worker = FileWorker()
    worker.open('./1', create=True, read=False)
    worker.write('123')
    worker.close()
    worker.open('./1', create=False, read=True)
    data = worker.read()
    print(data)

    print("-" * 32)

    worker.open('./2', create=True, read=True)
    worker.write('123')
    worker.seek(0)
    data = worker.read()
    print(data)
