import argparse
from src.api_fuzzer import ApiFuzzer


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fuzz api list')
    parser.add_argument('-t', '--target', required=True,
                        help='File path of target.json')
    parser.add_argument('-w', '--wordlist', required=True,
                        help='Fuzzing wordlist file')
    args = parser.parse_args()

    ApiFuzzer(target_path=args.target, wordlist_path=args.wordlist)
