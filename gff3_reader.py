#!/usr/bin/env python3
import sys


def gff3_reader(input_filename, output_filename):
    relevant_lines = []  # used to store relevant lines of yeast.gff3
    bed_string = ''  # used to write to the bed file
    with open(f'{input_filename}.gff3', 'r') as yeast:
        lines = yeast.readlines()

        for line in lines:
            if line[0] != '#':  # doesn't work on comments
                split = line.split('\t')
                if split[2] == 'gene':  # indicates gene feature
                    relevant_lines.append(split)

    for line_list in relevant_lines:
        chrom_start = str(int(line_list[3]) - 1)  # start value is different in 0-indexing, end is the same
        main_stuff = f'{line_list[0]}\t{chrom_start}\t{line_list[4]}'  # chrom, chrom_start, chromEnd

        # the question implied it had to contain score fields
        # and the gff3 file contains strand data
        # so I am assuming it should be a BED6 file
        name = line_list[8].split(';')[1][5:]
        additional = f'{name}\t0\t{line_list[6]}'  # name, score, strand

        bed_string += f"{main_stuff}\t{additional}\n"

    with open(f'{output_filename}.bed', 'w') as bed:
        bed.write(bed_string)


if __name__ == '__main__':
    gff3_reader(sys.argv[1], sys.argv[2])
