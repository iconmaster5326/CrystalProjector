"""This script automatically fixes some of the issues with generated .py files from Kaitai Struct soruces."""

import keyword
import re
import sys
import glob

LOCAL_DEPS = ["vlq_base128_le"]

for arg in sys.argv[1:]:
    globbed = glob.glob(arg)
    for file in globbed:
        output = []
        with open(file, encoding="UTF-8") as instream:
            for line in instream.readlines():
                match = re.match(r"^import (.+)\n$", line)
                if match and match.group(1) in LOCAL_DEPS:
                    output.append(f"from . import {match.group(1)}\n")
                    continue
                match = re.match(r"^(\s*)([^\s]+) = (\d+)\n$", line)
                if match and match.group(2) in keyword.kwlist:
                    output.append(f"{match.group(1)}{match.group(2)}_ = {match.group(3)}\n")
                    continue
                output.append(line)
        with open(file, "w", encoding="UTF-8") as outstream:
            outstream.writelines(output)
