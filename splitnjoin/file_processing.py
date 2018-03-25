# Written by Sergio La Rosa (sergio.larosa89@gmail.com)
# Part of "splitnjoin" package
# https://github.com/SergioLaRosa/splitnjoin

import os
import sys
import logging
import hashlib
import math


class FileProcessor:

    def __init__(self):
        self._kilobytes = 1000
        self._megabytes = self._kilobytes * 1000

    def _get_chunk_size(self, data_size):
        return int(int(data_size) * self._megabytes)

    def _get_part_size(self, tot_size, tot_parts):
        return (math.ceil(tot_size / tot_parts))

    def gen_md5(self, filename, blocksize):
        self._blocksize = self._get_chunk_size(blocksize)
        self._m = hashlib.md5()
        with open(filename, "rb") as self._f:
            while True:
                self._buf = self._f.read(self._blocksize)
                if not self._buf:
                    break
                self._m.update(self._buf)
        return self._m.hexdigest()    

    def split_file_by_parts(self, from_file, tot_parts, to_dir):
        try:
            self._fstat = os.stat(from_file)
        except PermissionError as perm_err:
            logging.error(str(perm_err))
        except OSError as os_err:
            logging.error(str(os_err))
        self._part_size = self._get_part_size(self._fstat.st_size, tot_parts)
        self._split_file(from_file, self._part_size, to_dir)

    def split_file_by_size(self, from_file, chunk_size, to_dir):
        self._real_size = self._get_chunk_size(chunk_size)
        self._split_file(from_file, self._real_size, to_dir)

    def _split_file(self, from_file, chunk_size, to_dir):
        self._part_num = 0
        self._real_size = chunk_size
        if not os.path.exists(to_dir):
            try:
                os.mkdir(to_dir)
            except PermissionError as perm_err:
                logging.error(str(perm_err))
            except OSError as os_err:
                logging.error(str(os_err))
        else:
            for fname in os.listdir(to_dir):
                try:
                    os.remove(os.path.join(to_dir, fname))
                except PermissionError as perm_err:
                    logging.error(str(perm_err))
                except OSError as os_err:
                    logging.error(str(os_err))
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
                        break
                    except IOError as read_err:
                        logging.error(str(read_err))
                        break
                    except OSError as os_err:
                        logging.error(str(os_err))
                        break
                    self._part_num += 1
                    self._filename = os.path.join(
                        to_dir, (str(from_file) + '_part_%04d' %
                                 self._part_num))
                    try:
                        with open(self._filename, 'wb') as self._fileobj:
                            self._fileobj.write(self._chunk)
                    except PermissionError as perm_err:
                        logging.error(str(perm_err))
                        break
                    except IOError as write_err:
                        logging.error(str(write_err))
                        break
                    except OSError as os_err:
                        logging.error(str(os_err))
                        break
            return self._part_num
        except PermissionError as perm_err:
            logging.error(str(perm_err))
        except OSError as os_err:
            logging.error(str(os_err))
        except FileNotFoundError as notfnd_err:
            logging.error(str(notfnd_err))

    def join_file(self, from_dir, chunk_size, to_file):
        self._real_size = self._get_chunk_size(chunk_size)
        self._parts = list()
        try:
            with open(to_file, 'wb') as self._output:
                try:
                    self._parts = os.listdir(from_dir)
                    self._parts.sort()
                except OSError as os_err:
                    logging.error(str(os_err))
                if self._parts:
                    for self._filename in self._parts:
                        self._filepath = os.path.join(from_dir, self._filename)
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
                                        break
                                    except IOError as read_err:
                                        logging.error(str(read_err))
                                        break
                                    except OSError as os_err:
                                        logging.error(str(os_err))
                                        break
                                    try:
                                        self._output.write(self._filebytes)
                                    except IOError as write_err:
                                        logging.error(str(write_err))
                                        break
                                    except OSError as os_err:
                                        logging.error(str(os_err))
                                        break
                                self._fileobj.close()
                        except PermissionError as perm_err:
                            logging.error(str(perm_err))
                            break
                        except IOError as read_err:
                            logging.error(str(read_err))
                            break
                        except OSError as os_err:
                            logging.error(str(os_err))
                            break
        except PermissionError as perm_err:
            logging.error(str(perm_err))
        except IOError as write_err:
            logging.error(str(write_err))
        except Exception as generic_err:
            logging.error(str(generic_err))
