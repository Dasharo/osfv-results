<!--
SPDX-FileCopyrightText: 2024 3mdeb Sp. z o. o.

SPDX-License-Identifier: CC-BY-SA-4.0
-->

# osfv-results

This repository contains test results for Dasharo firmware for the following
mainboards:

- [MSI Z690-A PRO](./boards/msi/ms7d25) -- project [Alder Lake Desktop](https://nlnet.nl/project/AlderLake/)
- [MSI Z790-P PRO](./boards/msi/ms7e06) -- project [Raptor Lake Desktop](https://nlnet.nl/project/RaptorLake/)
- [NovaCustom V54](./boards/NovaCustom/V54x_MTL/)
- [NovaCustom V56](./boards/NovaCustom/V56x_MTL/)

The `boards` directory contains the current test results retrieved from the
[Dasharo Test & Feature Matrix](https://docs.google.com/spreadsheets/d/1wSE6xA3K3nXewwLn5lV39_2wZL1kg5AkGb4mvmG3bwE/edit#gid=736501945)
sheet.

Tests which were not performed (such as `NOT TESTED`, `SKIP`, `BLANK`) are
not included in the repository.

The `archive` section contains archival test results retrieved from previous
iterations of the test sheets and is preserved here for historical purposes.

## Updating

The results can be updated manually or using a script `update_results.py`.
To use it simply launch it using python.

### New boards

When adding a new board family, for which a seperate `results.csv` file
should be kept, like `V54x_MTL`, the `results.csv` file has to be created
manually. The file only needs to contain the column names identical to full
names in the test matrix. Then the script will be able to update the file 
automatically according to column names present in it.

### Manual updating

If a board family should be excluded from the automated updates there
are two ways to make the script ignore it:
- Add an empty file called `manual_update` to the directory containing 
`results.csv`
- Add the name of the directory containing the `results.csv` file to 
`IGNORE_BOARDS` list in the `update_results.py` script.

## Links

- [Dasharo Test Specification](https://docs.dasharo.com/unified-test-documentation/overview/)

## Funding

This project is partially funded through
[NGI0 Entrust](https://nlnet.nl/entrust), a fund established by
[NLnet](https://nlnet.nl) with financial support from the European Commission's
[Next Generation Internet](https://ngi.eu) program. Learn more at the
[NLnet project page](https://nlnet.nl/project/RaptorLakeDesktop).

<p align=center>
    <a href="https://nlnet.nl"><img src="https://nlnet.nl/logo/banner.png" alt="NLnet foundation logo" height="75" /></a>
    <a href="https://nlnet.nl/entrust"><img src="https://nlnet.nl/image/logos/NGI0_tag.svg" alt="NGI Zero logo" height="75" /></a>
</p>
