# region Modules

import argparse
import subprocess
import os

# endregion

# region Functions


def main():
    # Parse arguments
    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument("--namespace", type=str)
    argumentParser.add_argument("--source_block", type=str)
    arguments = argumentParser.parse_args()

    jsonPath: str = "json"

    # Open each `.json` file in the `json/` directory
    for root, dirs, files in os.walk(jsonPath):
        for file in files:
            if file.lower().endswith("json".lower()):
                # Find and replace the $NAMESPACE and $SOURCE_BLOCK variables
                with open(os.path.join(root, file), "r") as newFile:
                    filedata = newFile.read()

                filedata = filedata.replace("$NAMESPACE", arguments.namespace)
                filedata = filedata.replace("$SOURCE_BLOCK", arguments.source_block)
                print(filedata)

    # Save the generated string as a new `.json` file...
    # ... with the appropriate file prefix...
    # I.E $SOURCE_BLOCK, generating...
    # ... $SOURCE_BLOCK_block.json.

    pass


# endregion

if __name__ == "__main__":
    main()
