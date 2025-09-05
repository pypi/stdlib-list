#!/usr/bin/env python
from __future__ import annotations

import importlib
import inspect
import pkgutil
import sys

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Sequence
    from types import ModuleType

SEEN_MODS = set()


def walk_pkgutil(mod_name: str, locations: Sequence[str]) -> None:
    for pkg in pkgutil.walk_packages(locations, f"{mod_name}."):
        if pkg.name in SEEN_MODS:
            continue
        else:
            # We don't recurse here because `walk_packages` takes care of
            # it for us.
            SEEN_MODS.add(pkg.name)


def walk_naive(mod_name: str, mod: ModuleType) -> None:
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
            submod_name = f"{mod_name}.{attr}"
            importlib.import_module(submod_name)
            walk(submod_name)
        except ImportError:
            # ...but sometimes we do want to include re-exports, since
            # they might be things like "accelerator" modules that don't
            # appear anywhere else.
            # For example, `_bz2` might appear as a re-export.
            try:
                # Again, try and import to avoid module-looking object
                # that don't actually appear on disk. Experimentally,
                # there are a few of these (like "TK").
                importlib.import_module(attr)
                walk(attr)
            except ImportError:
                continue


def walk(mod_name: str) -> None:
    if mod_name in SEEN_MODS:
        return
    else:
        SEEN_MODS.add(mod_name)

    # Try and import it.
    try:
        mod = importlib.import_module(mod_name)
    except ImportError:
        return

    try:
        locations = mod.__spec__.submodule_search_locations
    except AttributeError:
        locations = None

    if locations is not None:
        walk_pkgutil(mod_name, locations)
    else:
        walk_naive(mod_name, mod)


if __name__ == "__main__":
    output = sys.argv[1]

    for mod_name in sys.builtin_module_names:
        walk(mod_name)

    if hasattr(sys, "stdlib_module_names"):
        for mod_name in sys.stdlib_module_names:
            walk(mod_name)
    else:
        for mod_name in sys.stdin:
            # Our precomputed list might not start at the root, since it
            # might be a package rather than a module.
            if "." in mod_name:
                top_mod = mod_name.split(".")[0]
                walk(top_mod)
            walk(mod_name.rstrip("\n"))

    try:
        with open(output, encoding="utf-8") as io:
            SEEN_MODS.update(io.read().splitlines())
    except FileNotFoundError:
        pass

    with open(output, mode="w", encoding="utf-8") as io:
        for line in sorted(SEEN_MODS):
            print(line, file=io)
