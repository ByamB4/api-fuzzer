from requests import get, post
import json
import argparse
from colors import bcolors


class ApiFuzzer:
    TARGET = ''

    def __init__(self, target_path: str) -> None:
        self.read_target(target_path)
        self.meta_information()
        # for api in target['APIs']:
        #     print(
        #         f"{bcolors.BOLD}[*] Target: {target['BASE_URL']}{bcolors.ENDC}")
        #     print(
        #         f"\t{bcolors.WARNING}[*] Endpoint: {api['endpoint']}{bcolors.ENDC}")
        # for method in api['methods']:

    def meta_information()

    def read_target(self, target_path: str) -> None:
        try:
            with open(target_path, 'r') as f:
                self.TARGET = json.load(f)
        except FileNotFoundError:
            print(
                f"{bcolors.FAIL}[-] Config file not found{bcolors.ENDC}")
            exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fuzz api list')
    parser.add_argument('-t', '--target', required=True,
                        help='File path of target.json')
    args = parser.parse_args()
    ApiFuzzer(args.target)
