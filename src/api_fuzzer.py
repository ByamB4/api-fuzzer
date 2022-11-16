from .colors import bcolors
from .consts import *
import json
from datetime import datetime
from functools import partial

print = partial(print, flush=True)


class ApiFuzzer:
    # target's json file
    TARGET = ''
    # fuzzing wordlist
    WORDLIST = ''

    def __init__(self, target_path: str, wordlist_path: str) -> None:
        self.read_target(target_path)
        self.read_wordlist(wordlist_path)
        self.meta_information()
        self.fuzz_target()
        # for api in target['APIs']:
        #     print(
        #         f"\t{bcolors.WARNING}[*] Endpoint: {api['endpoint']}{bcolors.ENDC}")
        # for method in api['methods']:

    def fuzz_target(self):
        for api in self.TARGET['APIs']:
            self.fuzz_api(api)

    def fuzz_api(self, api):
        print(f"{INFO} API: {bcolors.BOLD}{api['endpoint']}{bcolors.ENDC}")
        payloads = self.generate_json_payloads(api['params'])

    def generate_json_payloads(self, params):
        ret = []
        for payload in self.WORDLIST:
            json_obj = []
            for param in params:
                pass
            # payload.strip()

    def meta_information(self) -> None:
        print(
            f"{INFO} Start time:\t\t {datetime.now().strftime('%H:%M:%S /%Y-%m-%d/')}")
        print(f"{INFO} API length:\t\t {len(self.TARGET['APIs'])}")
        print(f"{INFO} Wordlist length:\t\t {len(self.WORDLIST)}")

    def read_target(self, target_path: str) -> None:
        try:
            with open(target_path, 'r') as f:
                self.TARGET = json.load(f)
        except FileNotFoundError:
            print(
                f"{bcolors.FAIL}[-] Target file not found{bcolors.ENDC}")
            exit()

    def read_wordlist(self, wordlist_path: str) -> None:
        try:
            with open(wordlist_path, 'r') as f:
                self.WORDLIST = f.readlines()
        except FileNotFoundError:
            print(
                f"{bcolors.FAIL}[-] Fuzzing file not found{bcolors.ENDC}")
            exit()
