# region Modules

import argparse
import colorama
from colorama import Fore
import subprocess
import os
import sys

# endregion

# region Functions


def main():
    # Parse arguments
    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument("--namespace", type=str)
    argumentParser.add_argument("--source_block", type=str)
    argumentParser.add_argument("--print_output", action="store_true")
    arguments = argumentParser.parse_args()

    jsonPath: str = "json"

    try:
        # Open each `.json` file in the `json/` directory
        for root, dirs, files in os.walk(jsonPath):
            for file in files:
                if file.lower().endswith("json".lower()):
                    # Find and replace the $NAMESPACE and $SOURCE_BLOCK variables
                    with open(os.path.join(root, file), "r") as newFile:
                        filedata = newFile.read()

                    filedata = filedata.replace("$NAMESPACE", arguments.namespace)
                    filedata = filedata.replace("$SOURCE_BLOCK", arguments.source_block)

                if arguments.print_output:
                    print(f"{Fore.YELLOW}{file}{Fore.RESET}:\n{filedata}\n")

    # Ignore keyboard interruption
    except KeyboardInterrupt():
        pass


# endregion

if __name__ == "__main__":
    main()
