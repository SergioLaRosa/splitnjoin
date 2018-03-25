# Written by Sergio La Rosa (sergio.larosa89@gmail.com)
# Part of "splitnjoin" package
# https://github.com/SergioLaRosa/splitnjoin

import splitnjoin as snj
import os
import sys
import shutil
import pkg_resources
from timeit import default_timer as timer


fsplitter = snj.FileProcessor()
fjoiner = snj.FileProcessor()
digests = list()
blocksize = 250
p_size = 250
from_file = "fake_data.bin"
to_dir = "test"
read_size = 250
from_dir = "test"
to_file = "joined_fake_data.bin"
snj_ver = pkg_resources.get_distribution("splitnjoin").version
print("[!]'splitnjoin' ver.", snj_ver, "Benchmark&Test tool\n")
print('[+] Generating fake binary file of 1 GB...')
print('[+] Please, wait...')
start = timer()
try:
    with open(os.path.abspath(from_file), 'wb') as fout:
        fout.write(os.urandom(1073741824))
    end = timer()
    print("[+]", from_file, "written.")
    print('[+] Writing time: ', end - start)
    print("")
    absfrom, absto = map(os.path.abspath, [from_file, to_dir])
    print('[+] Splitting', absfrom, 'to', absto, 'by', p_size, 'mb...')
    print('[+] Please, wait...')
    start = timer()
    fsplitter.split_file_by_size(from_file, p_size, to_dir)
    end = timer()
    print('[+] Splitting time: ', end - start)
    print("")
    absfrom, absto = map(os.path.abspath, [from_dir, to_file])
    print('[+] Joining', absfrom, 'to', absto, 'by', read_size, 'mb...')
    print("[+] Please, wait...")
    start = timer()
    fjoiner.join_file(from_dir, read_size, to_file)
    end = timer()
    print("[+] Joining time: ", end - start)
    print("")
    print("[+] Calculating md5 hash for both files...")
    print("[+] Please wait...")
    start = timer()
    digests.append(fsplitter.gen_md5(from_file, blocksize))
    digests.append(fsplitter.gen_md5(to_file, blocksize))
    print("[+] md5:", digests[0], "for", from_file)
    print("[+] md5:", digests[1], "for", to_file)
    end = timer()
    print("[+] Hashing time: ", end - start)
    if digests[0] == digests[1]:
        print("\n[+] Integrity Check OK: files are identical.")
    else:
        print(
            "\n[!] Error: Check FAILED: files are different! (prob. corruption/losses)")
except KeyboardInterrupt:
    print("[!] Script stopped (Ctrl+C).")
    os.remove(from_file)
    shutil.rmtree(from_dir, ignore_errors=True)
    sys.exit()
print("")
print("[+] Removing test files...")
for filename in [from_file, to_file]:
    os.remove(filename)
    print("[+]", filename, " removed.")
print("[+] Removing test dir...")
shutil.rmtree(from_dir, ignore_errors=True)
print("[+] Test directory removed.")
