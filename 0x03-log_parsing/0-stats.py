#!/usr/bin/python3
"""
Log parsing
"""

import sys


def parse_line(line):
    try:
        data = line.split()
        status_code = data[-2]
        file_size = data[-1]
        return status_code, int(file_size)
    except BaseException:
        pass


def print_stats(stats, file_size):
    print(f'File size: {file_size}')
    for key in sorted(stats.keys()):
        if stats[key]:
            print(f'{key}: {stats[key]}')


if __name__ == '__main__':
    filesize = 0
    count = 0
    stats = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405':
             0, '500': 0}

    try:
        for line in sys.stdin:
            count += 1
            SCODE, FSIZE = parse_line(line)

            try:
                if SCODE in stats.keys():
                    stats[SCODE] += 1
                filesize += FSIZE
            except BaseException:
                pass

            if count % 10 == 0:
                print_stats(stats, filesize)

        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise
