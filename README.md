<!--
SPDX-FileCopyrightText: 2024 3mdeb Sp. z o. o.

SPDX-License-Identifier: CC-BY-SA-4.0
-->

# osfv-results

This repository contains test results for Dasharo firmware for the following
mainboards:

- [ASRock SPC741D8-2L2T/BCM](./boards/ASRock/SPC741D8-2L2T-BCM/)
- [MSI Z690-A PRO](./boards/msi/ms7d25) -- project [Alder Lake Desktop](https://nlnet.nl/project/AlderLake/)
- [MSI Z790-P PRO](./boards/msi/ms7e06) -- project [Raptor Lake Desktop](https://nlnet.nl/project/RaptorLake/)
- [NovaCustom NV41PZ](./boards/NovaCustom/ADL_12th_Gen/NV41PZ/)
- [NovaCustom V540TU](./boards/NovaCustom/MTL_14th_Gen/V540TU/)
- [NovaCustom V560TU](./boards/NovaCustom/MTL_14th_Gen/V560TU/)
- [NovaCustom V540TNx](./boards/NovaCustom/MTL_14th_Gen/V540TNX/)
- [NovaCustom V560TNx](./boards/NovaCustom/MTL_14th_Gen/V560TNX/)
- [Protectli VP2420](./boards/Protectli/VP2420/)
- [Protectli VP66xx](./boards/Protectli/VP66xx/)
- [Hardkernel ODROID-H4](./boards/Hardkernel/Odroid_H4/)
- [Dell OptiPlex 7010/9010](./boards/Dell/OptiPlex_7010_9010/)
- [QEMU Q35](./boards/QEMU/Q35/)

The `boards` directory contains the current test results retrieved from the
[Dasharo Test & Feature Matrix](https://docs.google.com/spreadsheets/d/1wSE6xA3K3nXewwLn5lV39_2wZL1kg5AkGb4mvmG3bwE/edit#gid=736501945)
sheet.

Tests which were not performed (such as `NOT TESTED`, `SKIP`, `BLANK`) are
not included in older files. Files in the layout described below list the
whole test scope of a release, so `NOT TESTED` rows are expected there.

## Release scope files

Files placed as

```text
boards/<vendor>/<platform>/<dut>/<version>_results.csv
```

are also the source of release scopes for the
[OSFV dashboard](https://git.3mdeb.com/dasharo/osfv-dashboard). Columns:

```text
Test name,Test ID,Automation,Result,Comments
```

- `Test ID` must exist in the dashboard test case database (it is populated
  from `test_cases.json` in OSFV).
- `Automation` is one of `automated`, `semi-automated`, `manual`. It records
  how the test is executed in the test plan. A manual result has the same
  standing as an automated one; do not add "manual" remarks to `Comments`.
- `Result` and `Comments` are ignored when creating the scope and come back
  from the dashboard once testing is done.

A new release starts as a pull request adding the file with every `Result` set
to `NOT TESTED`. The easiest way to get one is to export the previous release
from the dashboard viewer, rename it and edit the rows. CI validates the file
and prints the tests added and dropped against the previous release of the
same DUT. After the merge CI creates the release in the dashboard, or updates
its scope if a release with the same platform, version and DUT already exists.
Commits that only change results do not touch the dashboard.

Platform and DUT names in the dashboard are taken verbatim from the directory
names, unless a `dashboard.json` next to the CSV provides them:

```json
{
  "platform": "VP32xx",
  "dut": "VP3230 Protectli #2"
}
```

Renaming a directory or changing these strings creates a new release rather
than renaming the existing one. `scripts/export_release_scope.py` in
osfv-dashboard writes the CSV and the sidecar for an existing release.

The `archive` section contains archival test results retrieved from previous
iterations of the test sheets and is preserved here for historical purposes.

## Links

- [Dasharo Test Specification](https://docs.dasharo.com/unified-test-documentation/overview/)

## Funding

### Raptor Lake Desktop -  MSI PRO Z690-A/Z790-P WIFI DDR4/DDR5

This project is partially funded through
[NGI0 Entrust](https://nlnet.nl/entrust), a fund established by
[NLnet](https://nlnet.nl) with financial support from the European Commission's
[Next Generation Internet](https://ngi.eu) program. Learn more at the
[NLnet project page](https://nlnet.nl/project/RaptorLakeDesktop).

### UEFI Capsule Update for coreboot with EDK II

This project is partially funded through
[NGI0 Entrust](https://nlnet.nl/entrust), a fund established by
[NLnet](https://nlnet.nl) with financial support from the European Commission's
[Next Generation Internet](https://ngi.eu) program. Learn more at the
[NLnet project page](https://nlnet.nl/project/UEFICapsuleUpdate/).

<p align=center>
    <a href="https://nlnet.nl"><img src="https://nlnet.nl/logo/banner.png" alt="NLnet foundation logo" height="75" /></a>
    <a href="https://nlnet.nl/entrust"><img src="https://nlnet.nl/image/logos/NGI0_tag.svg" alt="NGI Zero logo" height="75" /></a>
</p>
