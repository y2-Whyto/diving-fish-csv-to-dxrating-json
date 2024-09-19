from typing import List, Tuple
import sys, getopt
import codecs
import csv, json


def print_help(code: int = 0, end: str = '\n') -> None:
    help_str = '''\
Usage:
    python {0} <input_switch> <input_file> <output_switch> <output_file>
    python {0} <help_switch>
Options:
    input_switch:   --input, -i
    output_switch:  --output, -o
    help_switch:    --help, -h\
'''.format(sys.argv[0])
    print(help_str, end=end)
    sys.exit(code)


def parse_args(options: List[Tuple[str, str]]) -> Tuple[str, str]:
    input_file: str = None
    output_file: str = None
    for (opt, arg) in options:
        if opt in ('--help', '-h'):
            print_help(0)
        elif opt in ('--input', '-i'):
            input_file = arg
        elif opt in ('--output', '-o'):
            output_file = arg
    if input_file == None or output_file == None:
        print_help(1)
    return (input_file, output_file)


def convert_data(input: str, output: str) -> None:
    with codecs.open(input, 'r') as i, \
            codecs.open(output, 'w', encoding='utf-8') as o:
        w_list = []
        d = {
            'DX': 'dx', 'SD': 'std',
            'Re:MASTER': 'remaster',
            'Master': 'master',
            'Expert': 'expert',
            'Advanced': 'advanced',
            'Basic': 'basic'
        }
        for r_line in csv.DictReader(i):
            item = {
                'sheetId': r_line['曲名'] + '__dxrt__' + d[r_line['类别']] + '__dxrt__' + d[r_line['难度']],
                'achievementRate': float(r_line['达成率'])
            }
            w_list.append(item)
        json.dump(w_list, o, ensure_ascii=False)


if __name__ == '__main__':
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], "hi:o:", ["help", "input=", "output="])
    except getopt.GetoptError:
        print_help()
        sys.exit(1)
    input_file, output_file = parse_args(opts)

    convert_data(input_file, output_file)
