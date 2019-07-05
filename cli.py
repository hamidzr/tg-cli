import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='Optional app description')

# Required positional argument
parser.add_argument('username', type=str,
                    help='target username')

# Optional argument
parser.add_argument('--text', type=str,
                    help='text')

# Optional argument
parser.add_argument('--file', type=str,
                    help='file')

# Optional argument
parser.add_argument('--caption', type=str,
                    help='caption')

args = parser.parse_args()
