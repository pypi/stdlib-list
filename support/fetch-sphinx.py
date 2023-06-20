#!/usr/bin/env python

# fetch-sphinx.py: retrieve a particular Python version's stdlib list
# using its hosted Sphinx inventory.

import sys
import sphobjinv as soi

if __name__ == "__main__":
    vers = sys.argv[1]
    inv = soi.Inventory(url=f"https://docs.python.org/{vers}/objects.inv")
    modules = list(sorted(obj.name for obj in inv.objects if obj.role == "module"))
    print("\n".join(modules))
