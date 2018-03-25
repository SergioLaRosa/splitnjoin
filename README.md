# splitnjoin
Simple module for splitting files into multiple chunks/parts and viceversa (from chunks/parts to original file).

I made splitnjoin for 3 reasons:
1. Speed-up uploading sessions (it is better to upload small, multiple files instead of a larger one; in case of network failure some parts of file are already online)
2. Surpass ISP _not-nice_ upload limitations about filesizes
3. End the laziness of a boring sunday

Performance of splitting/joining phases can vary greatly **depending on hardware configuration** (especially the HDD speed). 

For instance, let's try to split a Virtual Box virtual machine sized 8.5+ GB (.vdi): 
- A system equipped with AMD Ryzen 7, 16 GB DDR4 and an SSD.MD can split the VM in 34 chunks of 250MB each one, in less than 20 seconds
- An older notebook (i3, 8GB DDR3, and 5400 RPM HDD) requires 4+ minutes to split it with the same parameters

To read benchmark and performance tests, read sections below ("Perfomance tests").

Important: **don't use splitnjoin in production enviroments**, of course.

## Requirements

A default Python3 installation. It works on every Linux distro and every Windows version.

About **hardware requirements**: splitting and joining huge files are **CPU/RAM intensive tasks** and 'splitnjoin' is currently in its early days so don't expect big updates regarding resource optmization soon (I am working on it, that's for sure).

To put it simple: if you have a system with a fairly capable CPU and 4/8 GB RAM you shouldn't have any problem splitting huge files (for example, 8+ GB on hard disk).

## Installation
Install using [pip](https://pip.pypa.io/en/stable/quickstart/)

`pip3 install splitnjoin`

## Examples
**Splitting by chunk size example**

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
print('Splitting', absfrom, 'to', absto, 'by', p_size, 'mb...')
#Split now
fsplitter.split_file(from_file, p_size, to_dir)
```
**Splitting by parts example**

```Python
import splitnjoin as snj
import os
import sys

fsplitter = snj.FileProcessor()

#Set the number of parts you want, for example: 10
p_num = 10

#File to split and subdir where to save parts
from_file = "myFile.ext"
to_dir = "splitting_dir"

absfrom, absto = map(os.path.abspath, [from_file, to_dir])
print('Splitting', absfrom, 'to', absto, 'in', p_num, 'parts...')
#Split now
fsplitter.split_file_by_parts(from_file, p_num, to_dir)
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
#Join now
fjoiner.join_file(from_dir, readsize, to_file)
```

## Performance tests

I made a simple testing and benchmarking tool (splitting a binary file into chunks of 250MB each one). 

Run it like this: `python3 -m splitnjoin.snj_benchmark.py`. 

On my notebook (Intel i3 dual core, 8 GB RAM, 500 GB 5400 RPM disk, Linux Mint 18.3) this is the output:
 
```
[+] Generating fake binary file of 1 GB...
[+] Please, wait...
[+] fake_data.bin written.
[+] Writing time:  13.388530897998862

[+] Splitting /home/sergio/Scrivania/splitnjoin/fake_data.bin to /home/sergio/Scrivania/splitnjoin/test by 250 mb...
[+] Please, wait...
[+] Splitting time:  12.705547745999866

[+] Joining /home/sergio/Scrivania/splitnjoin/test to /home/sergio/Scrivania/splitnjoin/joined_fake_data.bin by 250 mb...
[+] Please, wait...
[+] Joining time:  15.447953824999786

[+] Calculating md5 hash for both files...
[+] Please wait...
[+] md5: 98a1c12f80bc9344846e75dc3b406611 for fake_data.bin
[+] md5: 98a1c12f80bc9344846e75dc3b406611 for joined_fake_data.bin
[+] Hashing time:  7.4639659309996205

[+] Integrity Check OK, the files are identical.

[+] Removing test files...
[+] fake_data.bin  removed.
[+] joined_fake_data.bin  removed.
[+] Removing test dir...
[+] Test directory removed.
```
## TO-DO:
- ~~Improve splitting and joining methods to speedup the entire process~~ (moved to [splitnjoiny project](https://github.com/SNN01/splitnjoiny))
- ~~Use multiprocess module to improve performance (if possibile, *i'm looking at you, I/O interface*)~~ (moved to [splitnjoiny project](https://github.com/SNN01/splitnjoiny))
- Using the module for write a basic CLI application and...
- ...Cross-compile this CLI application for Linux/macOS/Windows (multiplatform-binary)
