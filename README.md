# splitnjoin
Simple module for splitting files into multiple chunks and viceversa (from chunks to original file).

**Requirements**
A default Python3 installation. That's all. It works on every Linux distro and every Windows version.

**Installation**
`pip3 install splitnjoin
`
**Splitting example**
```
import splitnjoin as snj
import os
import sys

fsplitter = snj.FileProcessor()

#Size of each chunk, for example 25 mb
row_size = int(25)

#Get correct chunksize
chunksize = int(row_size * fsplitter._megabytes)

#File to split and subdir where to save chunks
from_file = "myFile.ext"
to_dir = "splitting_dir"

absfrom, absto = map(os.path.abspath, [from_file, to_dir])
print('Splitting', absfrom, 'to', absto, 'by', chunksize)
fsplitter._split_file(from_file, 4, chunksize, to_dir)
```

**Joining example**
```
import splitnjoin as snj
import os
import sys

fjoiner = snj.FileProcessor()

#Size of each chunk, for example 25 mb
row_size = int(25)

#Get correct chunksize
chunksize = int(row_size * fsplitter._megabytes)

#Set the size-value for reading chunks
readsize = 1024

#Set chunks dir and dest filename
from_dir = "splitting_dir"
to_file = "joined_myFile.ext"

absfrom, absto = map(os.path.abspath, [from_dir, to_file])
print('Joining', absfrom, 'to', absto, 'by', chunksize)
fjoiner = fjoiner._join_file(from_dir, to_file, readsize)
```
