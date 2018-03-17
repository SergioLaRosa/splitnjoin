import os
import sys


class FileProcessor:

    def __init__(self):
        self._kilobytes = 1024
        self._megabytes = self._kilobytes * 1000

    def _get_chunk_size(self, data_size):
        return int(int(data_size) * self._megabytes)

    def split_file(self, from_file, chunk_size, to_dir):
        self._part_num = 0

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
                            self._get_chunk_size(chunk_size))
                        if not self._chunk:
                            break
                    except MemoryError as mem_err:
                        print(
                            "[!] Memory Error: try changing chunksize!")
                        print("[*] Details:", mem_err)
                    except IOError as read_err:
                        print("[!] Error: unable to read file chunk(s)!")
                        print("[*] Details:", read_err)

                    self._part_num += 1

                    try:
                        self._filename = os.path.join(
                            to_dir, (str(from_file) + '_part_%04d' %
                                     self._part_num))
                    except OSError as os_err:
                        print("[!] Error: unable to prepare chunk(s) path!")
                        print("[*] Details:", os_err)
                    try:
                        with open(self._filename, 'wb') as self._fileobj:
                            self._fileobj.write(self._chunk)
                    except IOError as write_err:
                        print("[!] Error: unable to write chunk(s)!")
                        print("[*] Details:", write_err)
                        

            return self._part_num

        except FileNotFoundError:
            print("[!] Error: file", from_file, "not found!")
        except KeyboardInterrupt:
            print("[!] Script interrupted (ctrl+C)")
            
    def join_file(self, from_dir, to_file, readsize):
        try:
            with open(to_file, 'wb') as self._output:
                try:
                    self._parts = os.listdir(from_dir)
                    self._parts.sort()
                except OSError as os_err:
                    print("[!] Error: unable to list chunks!")
                    print("[*] Details:", os_err)
                    
                for self._filename in self._parts:
                    try:
                        self._filepath = os.path.join(from_dir, self._filename)
                    except OSError as os_err:
                        print("[!] Error: unable to preapare joined file path!")
                        print("[*] Details:", os_err)    
                    try:
                        with open(self._filepath, 'rb') as self._fileobj:
                            while True:
                                try:
                                    self._filebytes = self._fileobj.read(
                                        self._get_chunk_size(readsize))
                                    if not self._filebytes:
                                        break
                                except MemoryError as mem_err:
                                    print(
                                        "[!] Memory Error: try changing readsize!")
                                    print("[*] Details:", mem_err)
                                except IOError as read_err:
                                    print("[!] Error: unable to read chunk(s)!")
                                    print("[*] Details:", read_err)
                                try:
                                    self._output.write(self._filebytes)
                                except IOError as write_err:
                                    print(
                                        "[!] Error: unable to write joined file!")
                                    print("[*] Details:", write_err)

                            self._fileobj.close()

                    except IOError as read_err:
                        print("[!] Error: unable to find chunk path!")
                        print("[*] Details:", read_err)

        except IOError as write_err:
            print("[!] Error: unable to prepare joined file!")
            print("[*] Details:", write_err)
        except KeyboardInterrupt:
            print("[!] Script interrupted (ctrl+C)")
            
