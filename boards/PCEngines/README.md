# What's this

Results for TrenchBoot tests on hardware (specifically, on AMD).

# How they were obtained

By running `trenchboot/` tests from [this OSFV PR][osfv-pr] on a APU2C DUT
with coreboot+SeaBIOS firmware and Linux from meta-trenchboot distribution built
[at this PR][meta-trenchboot-pr] as:

```
CONFIG=pcengines-apu2 RTE_IP=192.168.10.172 SNIPEIT_NO=1 scripts/run.sh trenchboot/ -- -v SEABIOS_BOOT_DEVICE:1
```

[osfv-pr]: https://github.com/Dasharo/open-source-firmware-validation/pull/555
[meta-trenchboot]: https://github.com/3mdeb/meta-trenchboot/pull/45
