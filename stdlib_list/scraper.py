from . import short_versions, data_dir, get_canonical_version

import os
import requests
import bs4
import csv
import re

urls = {}
_url_base = "https://docs.python.org/"

for ver in short_versions:
    url = _url_base
    suffix = "py-modindex.html"

    if ver == "2.6":
        suffix = "modindex.html"

    url += "{}/{}".format(ver, suffix)

    urls[ver] = url


def scrape(version=None):
    """
    Scrapes the Python Module Index for the specified version(s) of Python, and stores the resulting data within the ``lists`` subdirectory of this package.

    :param version: A specified version of Python whose module index is to be scraped. If this is not set, then all avaliable versions are scraped.
    :type version: one of ``"2.6"``, ``"2.7"``, ``"3.2"``, ``"3.3"``, or ``"3.4"``, or ``None``
    """

    if version is not None:
        versions_to_scrape = [get_canonical_version(version)]
    else:
        versions_to_scrape = sorted(short_versions)

    for ver in versions_to_scrape:
        response = requests.get(urls[ver])
        soup = bs4.BeautifulSoup(response.text)

        # Grab the table
        table = soup.find("table")

        # Only take the rows that:
        #
        # * Aren't section headers (first two parenthesized conditions), and
        # * Have a section name ("td > a > tt")

        table_rows = [
            x for x in table.select("tr")
            if ("class" not in x.attrs
                or x["class"] not in [["pcap"], ["cap"]])
            and x.select("td > a > tt")
        ]

        metadata = {}
        # module: {
        #     "os": (Windows/Unix/etc/default of None),
        #     "description": description,
        #     "deprecated": (default of None)
        # }

        for row in table_rows:
            os_name = None
            description = None
            deprecated = None

            td_a = [x for x in row("td") if x.select("a")][0]
            a = td_a.select("a")[0]
            module = a.text

            os_select = td_a.select("em")
            if os_select:
                os_name = os_select[0].text.replace("(", "").replace(")", "")

            description = td_a.next_sibling.select("em")[0].text

            # Some longer descriptions have EOL characters built into them...
            description = re.sub("\r?\n", " ", description)

            if td_a.next_sibling.select("strong"):
                if td_a.next_sibling.select(
                        "strong")[0].text.lower().startswith("deprecated"):
                    deprecated = 1

            metadata[module] = {
                "os": os_name,
                "description": description,
                "deprecated": deprecated
            }

        # Write to file!

        file_name = os.path.join(data_dir, "{}.csv".format(ver))

        with open(file_name, "w") as f:
            writer = csv.writer(f, lineterminator="\n")
            writer.writerow(["module", "os", "description", "deprecated"])

            for module in sorted(metadata.keys()):
                writer.writerow(
                    [module] + [metadata[module][x]
                                for x in ["os", "description", "deprecated"]]
                )
