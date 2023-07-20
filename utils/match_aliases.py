import ullyses_utils
import pandas as pd
import re

RED = "\033[1;31m" 
RESET = "\033[0;0m"

def match_aliases(targname, return_name="ULL_MAST_name"):
    aliases_file = ullyses_utils.__path__[0] + '/data/target_metadata/pd_all_aliases.json'
    aliases = pd.read_json(aliases_file, orient="split")
    # In case we can't find a match
    ull_targname = targname
    
    targ_matched = False
    # The alias file is all uppercase
    targ_upper = targname.upper()
    mask = aliases.apply(lambda row: row.astype(str).str.fullmatch(re.escape(targ_upper)).any(), axis=1)
    if set(mask) != {False}:
        targ_matched = True
        ull_targname = aliases[mask][return_name].values[0]
    if targ_matched is False:
        print(f"{RED}WARNING: Could not match target name {ull_targname} to ULLYSES alias list{RESET}")
    return ull_targname


if __name__ == "__main__":
    alias = match_aliases("[AAOMEGA]_361")
    print(alias)
