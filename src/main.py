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
        if not os.path.exists("../generated"):
            os.mkdir("../generated")

        # Open each `.json` file in the `json/` directory
        for root, dirs, files in os.walk(jsonPath):
            if not os.path.exists(f"../generated/{root}"):
                os.mkdir(f"../generated/{root}")

            for file in files:
                if file.lower().endswith("json".lower()):
                    # Find and replace the $NAMESPACE and $SOURCE_BLOCK variables
                    with open(os.path.join(root, file), "r") as newFile:
                        fileData = newFile.read()

                    fileData = fileData.replace("$NAMESPACE", arguments.namespace)
                    fileData = fileData.replace("$SOURCE_BLOCK", arguments.source_block)

                if arguments.print_output:
                    print(f"{Fore.YELLOW}{file}{Fore.RESET}:\n{fileData}\n")

                with open(f"../generated/{os.path.join(root, file), 'w'}") as newGeneratedFile:
                    newGeneratedFile.write(fileData)

    # Ignore keyboard interruption
    except KeyboardInterrupt:
        pass


# endregion

if __name__ == "__main__":
    main()
