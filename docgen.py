#!/usr/bin/env python3
# TODO: gendoc CI on push?
import re

def strip_head(s):
    return s.strip().lower().replace("`", "").replace("*", "").replace(" ", "-")

with open('./norg_tutorial.norg') as file:
    lines = file.read().strip()

headings = re.findall(r"^\s*(\*+ [a-zA-Z0-9_\-\.\ :`\/\+\(\)]+)", lines, re.MULTILINE)

res = ""
for head in headings:
    res += f"norg-tutorial-{strip_head(head)}\t../norg_tutorial.norg\t/{head}\n"


with open('./doc/tags', 'w') as f:
    f.write(res)
