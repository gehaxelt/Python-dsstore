# Python .DS_Store parser

This repository contains a parser for Apple's `.DS_Store` file format. 

A sample file form a CTF is included in the `./samples/` directory and the you can try the parser using `python3 main.py ./samples/.DS_Store.ctf`. 

Here's my blogpost that tries to explain the structure and format in detail:  https://0day.work/parsing-the-ds_store-file-format/

# Usage

```
$ python main.py samples/.DS_Store.ctf 
Count:  6
favicon.ico
flag
static
templates
vulnerable.py
vulnerable.wsgi
```

# Useful ressources

I found the following links to be quite helpful while developing the parser:

- https://wiki.mozilla.org/DS_Store_File_Format
- http://search.cpan.org/~wiml/Mac-Finder-DSStore/DSStoreFormat.pod
- https://digi.ninja/projects/fdb.php

# License

MIT - See License.md
