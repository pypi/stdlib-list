#!/usr/bin/env python

import inspect
import sys

SEEN_MODS = set()


def walk(mod_name):
    if mod_name in SEEN_MODS:
        return
    else:
        SEEN_MODS.add(mod_name)
        print(mod_name)

    # Try and import it.
    try:
        mod = __import__(mod_name)
        for attr in dir(mod):
            attr_obj = getattr(mod, attr, None)
            # Shouldn't happen, but who knows.
            if attr_obj is None:
                continue

            # If this member isn't a module, skip it.
            if not inspect.ismodule(attr_obj):
                continue

            # To filter "real" submodules from re-exports, we try
            # and import the submodule by its qualified name.
            # If the import fails, we know it's a re-exported module.
            try:
                submod_name = mod_name + "." + attr
                __import__(submod_name)
                walk(submod_name)
            except ImportError:
                # ...but sometimes we do want to include re-exports, since
                # they might be things like "accelerator" modules that don't
                # appear anywhere else.
                # For example, `_bz2` might appear as a re-export.
                walk(attr)
    except ImportError:
        pass


if __name__ == "__main__":
    for mod_name in sys.stdin:
        walk(mod_name.rstrip("\n"))
