from . import short_versions, data_dir, get_canonical_version

import os
import requests
import bs4

urls = {
    ver: "https://docs.python.org/{}/library/index.html".format(
        ver).replace("2.7", "2") for ver in short_versions
}


def scrape(version=None):

    if version is not None:
        versions_to_scrape = [get_canonical_version(version)]
    else:
        versions_to_scrape = sorted(short_versions)

    for ver in versions_to_scrape:
        response = requests.get(urls[ver])
        soup = bs4.BeautifulSoup(response.text)

        if ver == "2.6":
            l1_selector = "ul > li.toctree-l1"
        else:
            l1_selector = "div.toctree-wrapper.compound > ul > li.toctree-l1"

        l1_tags = soup.select(l1_selector)

        # Weed out the introduction and those covering built-in stuff

        l1_tags = [
            x for x in l1_tags
            if not x.a.text.endswith("Introduction")
            and "Built-in" not in x.a.text
        ]

        # Grab the level 2 TOC list items under each level 1.
        # Note that the list comprehension returns a
        # list of list of tags. The sum(., []) flattens it out.

        l2_tags = sum([x.select("li.toctree-l2") for x in l1_tags], [])

        libraries = sorted(
            list(set([x.text for x in sum([y.select("span.pre")
                                           for y in l2_tags], [])])))

        # There's one reference to a file extension in the same
        # span.pre that we're using for module names, and also mention
        # of methods (eg os.statvfs()). So strip 'em out
        libraries = [
            x for x in libraries if not x.startswith(".")
            and "(" not in x and ")" not in x
        ]

        # Finally, some mentions of modules, such as xml.sax.handler,
        # need to be broken down so that we know that xml.sax and
        # xml are both included.

        dot_libs = [x for x in libraries if "." in x]

        for lib in dot_libs:
            lib_split = lib.split(".")
            # Ensure that all super-modules are included (A, A.B, A.B.C, etc)

            for i in range(len(lib_split)):
                libraries.append(".".join(lib_split[:i]))

        # Dedupe, make sure we have no empty strings, and sort, to
        # make things all pretty-like:

        libraries = sorted(list(set([x for x in libraries if x])))

        # Write to file!

        file_name = os.path.join(data_dir, "{}.txt".format(ver))

        with open(file_name, "w") as f:
            f.write("\n".join(libraries))
