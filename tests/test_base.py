from importlib import resources

import pytest

import stdlib_list


@pytest.mark.parametrize(
    ("version", "canonicalized"),
    [("2.7", "2.7"), ("3.10", "3.10")],
)
def test_get_canonical_version(version, canonicalized):
    assert stdlib_list.get_canonical_version(version) == canonicalized


@pytest.mark.parametrize("version", ["nonsense", "1.2.3", "3.1000"])
def test_get_canonical_version_raises(version):
    with pytest.raises(ValueError, match=rf"No such version: {version}"):
        stdlib_list.get_canonical_version(version)


@pytest.mark.parametrize("version", [*stdlib_list.short_versions, *stdlib_list.long_versions])
def test_self_consistent_unordered(version):
    list_path = f"lists/{stdlib_list.get_canonical_version(version)}.txt"
    file = resources.files("stdlib_list") / list_path
    modules = frozenset(file.read_text(encoding="utf-8").splitlines())

    for mod_name in modules:
        assert stdlib_list.in_stdlib(mod_name, version)

    assert modules == stdlib_list.stdlib_modules(version)


@pytest.mark.parametrize("version", [*stdlib_list.short_versions, *stdlib_list.long_versions])
def test_self_consistent_ordered(version):
    list_path = f"lists/{stdlib_list.get_canonical_version(version)}.txt"
    file = resources.files("stdlib_list") / list_path
    modules = list(file.read_text(encoding="utf-8").splitlines())

    for mod_name in modules:
        assert stdlib_list.in_stdlib(mod_name, version)

    assert modules == stdlib_list.stdlib_list(version)


@pytest.mark.parametrize(
    "version_file", [f.name for f in resources.files("stdlib_list").joinpath("lists").iterdir()]
)
def test_self_consistent_reverse(version_file):
    version = version_file.removesuffix(".txt")
    assert stdlib_list.stdlib_list(version)
