#!/bin/scons

# region Modules

import subprocess

# endregion


# region Functions


def main():
    pass


# endregion

if __name__ == "__main__":
    print(f":: Running as a {Fore.YELLOW}Python{Fore.RESET} script.")
    main()
elif __name__ == "SCons.Script":
    print(f":: Running as a {Fore.YELLOW}SCons{Fore.RESET} script.")
    main()
elif __name__ == "SConstruct":
    print(
        f":: {Fore.RED}Error{Fore.RESET}: The {Fore.YELLOW}SConstruct{Fore.RESET} file should not be used as a module."
    )
    raise ImportError
    sys.exit(1)
else:
    print(
        f":: {Fore.RED}Error{Fore.RESET}: The {Fore.YELLOW}SConstruct{Fore.RESET} script seems to have been used abnormally, exiting..."
    )
    sys.exit(1)
