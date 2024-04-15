# Create a table with novelWriter metadata.


## Features

This Python script searches a [novelWriter](https://novelwriter.io/) project for
tags, references, comments, and synopses. It creates a table with a row for 
each heading, and a column for each metadata category.

The metadata table is exported as a csv file.

```
         , key 1, key 2, ... key n
heading 1, value, value, ... value
  .
  .
  .
heading m, value, value, ... value   

```

## Requirements

- A Python installation (version 3.6 or newer).


## Download

Save the file [nw_meta.py](https://raw.githubusercontent.com/peter88213/nw_metadata/main/src/nw_meta.py).


## Usage

`nw_meta.py sourceFolder`

Positional arguments:
- sourceFolder -- Path to the *novelWriter* project folder.


You can also drag the *novelWriter* project folder icon and drop it on the *nw_meta.py* icon. 



------------

## License

Published under the [MIT License](https://opensource.org/licenses/mit-license.php)

---

## See also


### mm2nw

Generate a novelWriter project from a FreeMind/Freeplane outline.

[mm2nw](https://github.com/peter88213/mm2nw/)


### odt2nw

Generate a novelWriter project from a work in progress written with e.g. LibreOffice.

[odt2nw](https://github.com/peter88213/odt2nw/)


### md2nw

Generate a novelWriter project from a work in progress written with any text editor or Markdown word processor.

[md2nw](https://github.com/peter88213/md2nw/)


### yw2nw

Converter between yWriter and novelWriter.

[![yw2nw](img/yw2nw.png)](https://peter88213.github.io/yw2nw/)



