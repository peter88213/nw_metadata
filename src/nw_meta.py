#!/usr/bin/python3
"""Create a table with novelWriter metadata.

usage: 
nw_meta.py sourceFolder

Positional arguments:
    sourceFolder -- Path to the novelWriter project folder.

Copyright (c) 2024 Peter Triesberger
For further information see https://github.com/peter88213/nw_metadata
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import csv
import glob
import os
import sys


def read_nw(sourceFolder: str) -> list[list[str]]:
    """Return a metadata table.
    
    Table structure: 
    [
        [''       , key 1, key 2, ... key n],
        [heading 1, value, value, ... value],  
        .
        .
        .
        [heading m, value, value, ... value],    
    ]
    """

    # Parse the nwd files in the source folder.
    # Store headings and metadata in a nested dictionary.
    # Create a list of metadata keys.
    headings: dict[str, dict[str, str]] = {}
    metaKeys: list[str] = []

    nwdFiles = []
    try:
        with open(f'{sourceFolder}/ToC.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        print('Reading table of contents ...')
        for line in lines:
            if line.startswith('content/'):
                nwdFiles.append(os.path.join(sourceFolder, line.split(' ')[0]))
    except:
        print('Could not read table of contents. Using file system order.')
        nwdFiles = glob.glob(f'{sourceFolder}/content/*.nwd')

    print('Reading nwd files ...')
    for nwdFile in nwdFiles:
        with open(nwdFile.replace('\\', '/'), 'r', encoding='utf-8') as f:
            lines = f.read().split('\n')
        heading = None
        for line in lines:
            if line.startswith('#'):
                i = 0
                heading = line
                while heading in headings:
                    i += 1
                    heading = f'{line} ({i})'
                headings[heading] = {}
            elif heading is None:
                continue

            elif line.startswith('@') or line.startswith('%'):
                metadata = line.split(':', maxsplit=1)
                metaKey = metadata[0].strip()
                if not metaKey in metaKeys:
                    metaKeys.append(metaKey)
                headings[heading][metaKey] = metadata[1].strip()

    # Create a table: List of rows; each row is a list of cells.
    rows = [[''] + metaKeys]
    for heading in headings:
        row = [heading]
        for metaKey in metaKeys:
            row.append(headings[heading].get(metaKey, ''))
        rows.append(row)
    return rows


def write_csv(csvFile: str, rows: list[list[str]]):
    """ Write the table to a csv file."""
    with open(csvFile, 'w', encoding='utf-8', newline='') as f:
        csvWriter = csv.writer(f, dialect='excel')
        for row in rows:
            csvWriter.writerow(row)


def main(sourceFolder: str):
    rows = read_nw(sourceFolder)
    csvFile = f'{sourceFolder}_metadata.csv'
    write_csv(csvFile, rows)
    print(f'"{os.path.normpath(csvFile)}" written.')


if __name__ == '__main__':
    main(sys.argv[1])
