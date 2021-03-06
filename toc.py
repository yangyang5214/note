# -*- coding: utf-8 -*-
import os


def main():
    data = {}
    for f in os.listdir('.'):
        if f.startswith('.') or f in ignore_file:
            continue
        data[f] = {}
        for sub_f in os.listdir(f):
            if sub_f.startswith('.'):
                continue
            if not sub_f.endswith('.md'):
                continue
            title = get_title(os.path.join(f, sub_f))
            data[f][sub_f] = title

    if not data:
        return

    with open('README.md', 'w') as f:
        f.write("\n")
        for key, val in data.items():
            f.write('## {}'.format(key))
            f.write("\n")
            for k, v in val.items():
                f.write(' - [{}](./{}/{})'.format(v, key, k))
                f.write("\n")
            f.write("\n")


def get_title(file):
    with open(file, 'r') as f:
        for line in f.readlines():
            if line.startswith('##'):
                return line.strip().replace('## ', '').strip()


ignore_file = {
    'README.md',
    'toc.py'
}

if __name__ == '__main__':
    main()
