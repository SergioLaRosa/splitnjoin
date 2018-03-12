import os
import sys


class FileProcessor():

    def __init__(self):
        self._kilobytes = 1024
        self._megabytes = self._kilobytes * 1000

    def _split_file(self, from_file, chunk_num, chunk_size, to_dir):

        if not os.path.exists(to_dir):
            os.mkdir(to_dir)
        else:
            for fname in os.listdir(to_dir):
                os.remove(os.path.join(to_dir, fname))

        self._part_num = 0

        with open(from_file, 'rb') as self._curr_file:
            while True:
                self._chunk = self._curr_file.read(chunk_size)
                if not self._chunk:
                    break
                self._part_num += 1
                self._filename = os.path.join(
                    to_dir, (str(from_file) + '_part_%04d' %
                             self._part_num))

                with open(self._filename, 'wb') as self._fileobj:
                    self._fileobj.write(self._chunk)

        return self._part_num

    def _join_file(self, from_dir, to_file, readsize):

        with open(to_file, 'wb') as self._output:
            self._parts = os.listdir(from_dir)
            self._parts.sort()

            for self._filename in self._parts:
                self._filepath = os.path.join(from_dir, self._filename)
                self._fileobj = open(self._filepath, 'rb')

                while True:
                    self._filebytes = self._fileobj.read(readsize)
                    if not self._filebytes:
                        break
                    self._output.write(self._filebytes)

                self._fileobj.close()
