# -- coding: UTF-8 --
import sys, getopt
import optparse

'''
    第一种：通过sys.argv获取命令行参数
'''

print("sys.argv:    ", str(sys.argv))
print('sys.argv[-1]:    ', str(sys.argv[-1]))

#---------------------------------------------------------------------------
import argparse

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--string', type=str, default=None)
parser.add_argument('--int-input', type=int, default=32)
parser.add_argument('--list-input', type=list, default=[1,2,3])
args = parser.parse_args()


if __name__ == '__main__':
    print(args.string)
    print(args.int_input)
    print(args.list_input)

    # 命令行输入这个
    # python cmd_parameter.py --string=python --int-input=10 --list-input=123






