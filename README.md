# splitnjoin
Simple module for splitting files into multiple chunks and viceversa (from chunks to original file).

I made splitnjoin for 3 reasons:
1. Speed-up my uploading sessions (it's better to upload small, multiple files instead of a bigger one; in case of network failure some parts of file are already online)
2. Surpass my ISP _not-nice_ upload limitations about filesizes.
3. End the laziness of a boring sunday

Splitting and joining methods were **tested** with different file formats and sizes and everything works flawlessy in a resonable amount of time (1/2 minutes) for both split/join phases. Just for comparison: splitting a .vdi VM sized 8+Gb on my i3/8G notebook takes 177 seconds circa. 

Important: **don't use splitnjoin in production enviroments**, of course.

To read benchmark and performance tests, see below.

## Requirements

A default Python3 installation. That's all. It works on every Linux distro and every Windows version.

Regarding **hardware reqs**: splitting and joining huge files are **CPU/RAM intensive tasks** and 'splitnjoin' is currently in its early days so don't expect big updates regarding resource optmization soon (I'll working on it, that's for sure).

Put it simple: if you have a system with a fairly capable CPU and 4/8 GB RAM you shouldn't have any problem splitting huge files (for example, 8+GB on hard disk).

## Installation

`pip3 install splitnjoin`

## Examples
**Splitting example**

```Python
import splitnjoin as snj
import os
import sys

fsplitter = snj.FileProcessor()

#Set size of each chunk, for example: 25 mb
p_size = 25

#File to split and subdir where to save chunks
from_file = "myFile.ext"
to_dir = "splitting_dir"

absfrom, absto = map(os.path.abspath, [from_file, to_dir])
print('Splitting', absfrom, 'to', absto, 'by', p_size)
#Split now
fsplitter._split_file(from_file, p_size, to_dir)
```
**Joining example**

```Python
import splitnjoin as snj
import os
import sys

fjoiner = snj.FileProcessor()

#Set the size-value for reading chunks, for example: 25 mb
readsize = 25

#Set chunks dir and dest filename
from_dir = "splitting_dir"
to_file = "joined_myFile.ext"

absfrom, absto = map(os.path.abspath, [from_dir, to_file])
print('Joining', absfrom, 'to', absto, 'by', readsize)
fjoiner._join_file(from_dir, to_file, readsize)
```

## Performance tests

I made a simple test&benchmark tool. Run it like this: `python3 -m splitnjoin.splitnjoin_benchmark.py`. 
 
```
[!]'splitnjoin' ver. 0.42 Benchmark&Test tool

[+] Generating fake binary file of 1 GB...
[+] Please, wait...
[+] fake_data.bin written.
[+] Writing time:  13.059494661999452

[+] Splitting /home/sergio/fake_data.bin to /home/sergio/test by 250 mb...
[+] Please, wait...
[+] Splitting time:  11.533364240999617

[+] Joining /home/sergio/test to /home/sergio/joined_fake_data.bin by 250 mb...
[+] Please, wait...
[+] Joining time:  15.895961958999578

[+] md5: 40fb2889e5d57bc50def0500efe87d14 for fake_data.bin
[+] md5: 40fb2889e5d57bc50def0500efe87d14 for joined_fake_data.bin

[+] Integrity Check OK, the files are identical.
```
TO-DO:
- Improve splitting and joining methods to speedup the entire process
- Use multiprocess module to improve performance (if possibile, *i'm looking at you, I/O interface*)
- Using the module for write a basic CLI application and...
- ...Cross-compile this CLI application for Linux/macOS/Windows (multiplatform-binary)
