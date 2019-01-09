"""
# Design
Since the input file can be really large, I don't want to read entire input file into
memory. Therefor, this file heavily utilizes the iterator protocol:
    - Input file is read into a iterator
    - For each row of the iterator, it's transformed to a correct output format, then
      written into output file
"""

import click, csv, sys, os
from src.writers import StdoutWriter, MarkdownWriter


def extension(fileobject):
    """Get the extension of the file object"""
    _, ext = os.path.splitext(fileobject.name)
    return ext


def get_reader(infile):
    """Return a iterator over every row of the input file
    IMPORTANT: make sure the custom readers read each row into a list of string,
    which is similar to the csv reader"""
    ext = extension(infile)
    if ext == '.csv': 
        return csv.reader(infile) # reader is an iterator
    else:
        raise NotImplementedError('Need to implement reader for {} extension'.format(ext))



def get_writer(fileobject):
    """Return a file writer depends on the output type"""
    ext = extension(fileobject)
    if ext == '.csv':
        return csv.writer(ext)
    elif ext == '.md':
        return MarkdownWriter(fileobject)
    else:
        raise NotImplementedError('Need to implement writer for {} extension'.format(ext))


@click.command()
@click.argument('infile', type=click.File('r'))
@click.argument('outfile', type=click.File('w'))
@click.option('--stdout', help='Also print the output content to std', type=bool, default=False)
def caketable(infile,  outfile, stdout):
    rows = get_reader(infile)
    writer = get_writer(outfile)
    stdwriter = StdoutWriter() if stdout else None

    for row in rows:
        writer.write(row)
        if stdwriter:
            stdwriter.write(row)


if __name__ == '__main__':
    caketable()
