<!--
SPDX-FileCopyrightText: 2024 3mdeb Sp. z o. o.

SPDX-License-Identifier: CC-BY-SA-4.0
-->

# osfv-results

This repository contains test results for Dasharo firmware for the following
mainboards:

- [MSI Z690-A PRO](./boards/msi/ms7d25) -- project [Alder Lake Desktop](https://nlnet.nl/project/AlderLake/)
- [MSI Z790-P PRO](./boards/msi/ms7e06) -- project [Raptor Lake Desktop](https://nlnet.nl/project/RaptorLake/)
- [NovaCustom NV41PZ](./boards/NovaCustom/ADL_12th_Gen/NV41PZ/)
- [NovaCustom V540TU](./boards/NovaCustom/MTL_14th_Gen/V540TU/)
- [NovaCustom V560TU](./boards/NovaCustom/MTL_14th_Gen/V560TU/)
- [NovaCustom V540TNx](./boards/NovaCustom/MTL_14th_Gen/V540TNX/)
- [NovaCustom V560TNx](./boards/NovaCustom/MTL_14th_Gen/V560TNX/)
- [Protectli VP2420](./boards/Protectli/VP2420/)
- [Protectli VP66xx](./boards/Protectli/VP66xx/)
- [Dell OptiPlex 7010/9010](./boards/Dell/OptiPlex_7010_9010/)
- [QEMU Q35](./boards/QEMU/Q35/)

The `boards` directory contains the current test results retrieved from the
[Dasharo Test & Feature Matrix](https://docs.google.com/spreadsheets/d/1wSE6xA3K3nXewwLn5lV39_2wZL1kg5AkGb4mvmG3bwE/edit#gid=736501945)
sheet.

Tests which were not performed (such as `NOT TESTED`, `SKIP`, `BLANK`) are
not included in the repository.

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
