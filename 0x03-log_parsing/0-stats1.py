#!/usr/bin/python3
"""
Log Parsing
"""

import sys


if __name__ == '__main__':
    FSIZE = 0
    count = 0
    STATS = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405':
             0, '500': 0 }

    def print_stats(code_stats, file_size):
        print('File size: {:d}'.format(file_size))

        for key, value in sorted(code_stats.items()):
            if value:
                print(f'{key}: {value}')

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()

            try:
                status_code = data[-2]
                if status_code in STATS:
                    STATS[status_code] += 1
                FSIZE += int(data[-1])
            except BaseException:
                pass

            if count % 10 == 0:
                print_stats(STATS, FSIZE)

        print_stats(STATS, FSIZE)
    except KeyboardInterrupt:
        print_stats(STATS, FSIZE)
        raise
