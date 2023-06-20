#!/usr/bin/env python

import inspect
import pkgutil
import sys

SEEN_MODS = set()


def walk_pkgutil(mod_name, mod, io):
    for pkg in pkgutil.walk_packages(mod.__path__, mod_name + "."):
        if pkg.name in SEEN_MODS:
            continue
        else:
            # We don't recurse here because `walk_packages` takes care of
            # it for us.
            SEEN_MODS.add(pkg.name)
            print(pkg.name, file=io)


def walk_naive(mod_name, mod, io):
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
            walk(submod_name, io)
        except ImportError:
            # ...but sometimes we do want to include re-exports, since
            # they might be things like "accelerator" modules that don't
            # appear anywhere else.
            # For example, `_bz2` might appear as a re-export.
            try:
                # Again, try and import to avoid module-looking object
                # that don't actually appear on disk. Experimentally,
                # there are a few of these (like "TK").
                __import__(attr)
                walk(attr, io)
            except ImportError:
                continue


def walk(mod_name, io):
    if mod_name in SEEN_MODS:
        return
    else:
        SEEN_MODS.add(mod_name)
        print(mod_name, file=io)

    # Try and import it.
    try:
        mod = __import__(mod_name)

        if hasattr(mod, "__path__"):
            walk_pkgutil(mod_name, mod, io)
        else:
            walk_naive(mod_name, mod, io)

    except ImportError:
        pass


if __name__ == "__main__":
    output = sys.argv[1]

    with open(output, mode="w") as io:
        for mod_name in sys.builtin_module_names:
            walk(mod_name, io)

        if hasattr(sys, "stdlib_module_names"):
            for mod_name in sys.stdlib_module_names:
                walk(mod_name, io)
        else:
            for mod_name in sys.stdin:
                walk(mod_name.rstrip("\n"), io)
