import os
import sys
import logging

class FileProcessor:

    def __init__(self):
        self._kilobytes = 1000
        self._megabytes = self._kilobytes * 1000

    def _get_chunk_size(self, data_size):
        return int(int(data_size) * self._megabytes)

    def split_file(self, from_file, chunk_size, to_dir):
        self._part_num = 0
        self._real_size = self._get_chunk_size(chunk_size)
        if not os.path.exists(to_dir):
            os.mkdir(to_dir)
        else:
            for fname in os.listdir(to_dir):
                os.remove(os.path.join(to_dir, fname))
        try:
            with open(from_file, 'rb') as self._curr_file:
                while True:
                    try:
                        self._chunk = self._curr_file.read(
                            self._real_size)
                        if not self._chunk:
                            break
                    except MemoryError as mem_err:
                        logging.error(str(mem_err))
                    except IOError as read_err:
                        logging.error(str(read_err))
                    self._part_num += 1
                    try:
                        self._filename = os.path.join(
                            to_dir, (str(from_file) + '_part_%04d' %
                                     self._part_num))
                    except OSError as os_err:
                        logging.error(str(os_err))
                    try:
                        with open(self._filename, 'wb') as self._fileobj:
                            self._fileobj.write(self._chunk)
                    except IOError as write_err:
                        logging.error(str(write_err))
            return self._part_num
        except FileNotFoundError as notfnd_err:
            logging.error(str(notfnd_err))
        except Exception as generic_err:
            logging.error(str(generic_err))
            
    def join_file(self, from_dir, chunk_size, to_file):
        self._real_size = self._get_chunk_size(chunk_size)
        try:
            with open(to_file, 'wb') as self._output:
                try:
                    self._parts = os.listdir(from_dir)
                    self._parts.sort()
                except OSError as os_err:
                    logging.error(str(os_err))
                for self._filename in self._parts:
                    try:
                        self._filepath = os.path.join(from_dir, self._filename)
                    except OSError as os_err:
                        logging.error(str(os_err))
                    try:
                        with open(self._filepath, 'rb') as self._fileobj:
                            while True:
                                try:
                                    self._filebytes = self._fileobj.read(
                                        self._real_size)
                                    if not self._filebytes:
                                        break
                                except MemoryError as mem_err:
                                    logging.error(str(mem_err))
                                except IOError as read_err:
                                    logging.error(str(read_err))
                                try:
                                    self._output.write(self._filebytes)
                                except IOError as write_err:
                                    logging.error(str(write_err))
                            self._fileobj.close()
                    except FileNotFoundError as notfnd_err:
                        logging.error(str(notfnd_err))
                    except IOError as read_err:
                        logging.error(str(read_err))
        except IOError as write_err:
            logging.error(str(write_err))
        except Exception as generic_err:
            logging.error(str(generic_err))
