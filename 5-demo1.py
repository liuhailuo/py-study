import argparse

parser =argparse.ArgumentParser(description="这个程序的用途")

parser.add_argument("-number",help="输入一个数字")

args = parser.parse_args()

print(f"您输入的number参数是 {args.number}")