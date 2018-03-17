class FileSplit:

    def __init__(self, size, nomeFile):
        self._nomeFile = nomeFile
        self._fileSize = size*1024*1024     #100Mb per file
        self._buffer = 2*1024*1024*1024     #2Gb buffer
        self._ext = 0                       #.000 file
        self._file = ''
        self._buffCheck = ''
        self._wrote = 0
        self._fileTemp = ''
        self._combinefile = ''

    def splitFile(self):
        with open(self._nomeFile, 'rb') as self._file:
            while True:
                self._fileTemp = open(self._nomeFile + '.%03d' % self._ext, 'wb')
                self._wrote = 0
                while self._wrote < self._fileSize:
                    if len(self._buffCheck) > 0:
                        self._fileTemp.write(self._buffCheck)
                    self._fileTemp.write(self._file.read(min(self._buffer, self._fileSize - self._wrote)))
                    self._wrote += min(self._buffer, self._fileSize - self._wrote)
                    self._buffCheck = self._file.read(1)
                    if len(self._buffCheck) == 0:
                        break
                self._fileTemp.close()
                if len(self._buffCheck) == 0:
                    break
                self._ext += 1


    def combineFile(self, nuovoFile):
        open(nuovoFile, 'wb')
        with open(nuovoFile, 'ab') as self._file:
            while True:
                try:
                    self._fileTemp = open(self._nomeFile + '.%03d' % self._ext, 'rb')
                except IOError:
                    break
                else:
                    self._file.write(self._fileTemp.read(self._buffer))
                    self._fileTemp.close()
                    self._ext += 1
