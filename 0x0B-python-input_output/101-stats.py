#!/usr/bin/python3
"""
Prints the metrics based on the provided total size and status codes.
"""


def print_stats(total_size, status_codes):
    """
    Prints the metrics based on the provided total size and status codes.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    import sys

    total_size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(total_size, status_codes)
                count = 1
            else:
                count += 1

            parts = line.split()
            try:
                file_size = int(parts[-1])
                total_size += file_size
            except (IndexError, ValueError):
                pass

            try:
                code = parts[-2]
                if code in valid_codes:
                    status_codes[code] = status_codes.get(code, 0) + 1
            except IndexError:
                pass

        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
