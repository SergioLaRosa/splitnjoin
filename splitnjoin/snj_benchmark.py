import splitnjoin as snj
import os
import sys
import hashlib
import pkg_resources
from timeit import default_timer as timer


fsplitter = snj.FileProcessor()
fjoiner = snj.FileProcessor()
digests = list()

p_size = 250
from_file = "fake_data.bin"
to_dir = "test"

readsize = 250
from_dir = "test"
to_file = "joined_fake_data.bin"

snj_ver = pkg_resources.get_distribution("splitnjoin").version
print("[!]'splitnjoin' ver.", snj_ver, "Benchmark&Test tool\n")
print('[+] Generating fake binary file of 1 GB...')
print('[+] Please, wait...')
start = timer()
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
fsplitter.split_file(from_file, p_size, to_dir)
end = timer()
print('[+] Splitting time: ', end - start)

print("")
absfrom, absto = map(os.path.abspath, [from_dir, to_file])
print('[+] Joining', absfrom, 'to', absto, 'by', readsize, 'mb...')
print("[+] Please, wait...")
start = timer()
fjoiner.join_file(from_dir, to_file, readsize)
end = timer()
print("[+] Joining time: ", end - start)

for filename in [from_file, to_file]:
    hasher = hashlib.md5()
    with open(filename, 'rb') as f:
        buf = f.read(256000)
        hasher.update(buf)
        a = hasher.hexdigest()
        digests.append(a)

print("")
print("[+] md5:", digests[0], "for", from_file)
print("[+] md5:", digests[1], "for", to_file)
if digests[0]==digests[1]:
    print("\n[+] Integrity Check OK, the files are identical.")
else:
	print("\n[!] Error: Check FAILED! Files are diffent (prob. corruption/losses)")
	
