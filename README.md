# splitnjoin
Simple module for splitting files into multiple chunks and viceversa (from chunks to original file).

I made splitnjoin for 3 reasons:
1. Speed-up my uploading sessions (it's better to upload small, multiple files instead of a bigger one; in case of network failure some parts of file are already online)
2. Surpass my ISP _not-nice_ upload limitations about filesizes.
3. End the laziness of a boring sunday

Splitting and joining methods were **tested** with different file formats and sizes (for example, a VDI VirtualBox VM sized 8+ Gb) and everything works flawlessy in a resonable amount of time (1/2 minutes) for both split/join phase.

TO-DO:
- Improve splitting and joining methods to speedup the entire process
- Use multiprocess module to improve performance
- Using the module for write a basic CLI application and...
- ...Cross-compile this CLI application for Linux/macOS/Windows (multiplatform-binary)

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

#Set size of each chunk, for example: 25
p_size = 25

#File to split and subdir where to save chunks
from_file = "myFile.ext"
to_dir = "splitting_dir"

absfrom, absto = map(os.path.abspath, [from_file, to_dir])
print('Splitting', absfrom, 'to', absto, 'by', chunksize)
#Split now
fsplitter._split_file(from_file, _get_chunk_size(p_size), to_dir)
```

**Joining example**
```
import splitnjoin as snj
import os
import sys

fjoiner = snj.FileProcessor()

#Set the size-value for reading chunks
readsize = 1024

#Set chunks dir and dest filename
from_dir = "splitting_dir"
to_file = "joined_myFile.ext"

absfrom, absto = map(os.path.abspath, [from_dir, to_file])
print('Joining', absfrom, 'to', absto, 'by', readsize)
fjoiner._join_file(from_dir, to_file, int(readsize))
```
