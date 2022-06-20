# regex-rename
`rrename` for short

## Why?

Tried batch renaming a bunch of files on a Steam Deck using regex and wasted an hour. Then wasted another hour making this.

Note that in verbose mode (`-v`), this script shaves files' directories off for display. By design, it doesn't move files to other directories, so this shouldn't matter.

## Usage

```
$ rrename -h
usage: rrename [-h] [-v] [-n] [-s] expression replacement file [file ...]

rename files with regular expressions

positional arguments:
  expression            regex search expression
  replacement           regex replacement expression
  file                  the files to operate on

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         explain actions before doing them
  -n, --dry-run         don't modify any files
  -s, --case-sensitive  disable case-insensitive mode
```

### Example:

```
$ rrename -vn '(.*?)\s\(.*\.(.*)' '\1.\2' ./*.gba
'Mega Man Zero (USA, Europe).gba' → 'Mega Man Zero.gba'
'Mega Man Zero 2 (Europe).gba' → 'Mega Man Zero 2.gba'
'Mega Man Zero 3 (Europe).gba' → 'Mega Man Zero 3.gba'
'Mega Man Zero 4 (Europe).gba' → 'Mega Man Zero 4.gba'
'Wario Land 4 (USA, Europe).gba' → 'Wario Land 4.gba'
--- 0 files renamed.
```