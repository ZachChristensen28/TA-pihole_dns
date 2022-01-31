# TA-pihole_dns - Pi-hole Add-on for Splunk

![GitHub](https://img.shields.io/github/license/zachchristensen28/TA-pihole_dns)
[![docs](https://github.com/ZachChristensen28/splunk-pihole-ta-documentation/actions/workflows/ci.yml/badge.svg)](https://splunk-pihole-ta.ztsplunker.com/)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/ZachChristensen28/TA-pihole_dns)
[![Splunkbase App](https://img.shields.io/badge/Splunkbase-TA--pihole__dns-blue)](https://splunkbase.splunk.com/app/4505/)
[![Splunk CIM Version](https://img.shields.io/badge/Splunk%20CIM%20Version-4.x-success)](https://docs.splunk.com/Documentation/CIM/latest/User/Overview)

## Documentation

Find full documentation for installing this add-on at [https://splunk-pihole-ta.ztsplunker.com/](https://splunk-pihole-ta.ztsplunker.com/)

## About

Info | Description
------|----------
Version | 1.3.1 - See on [Splunkbase](https://splunkbase.splunk.com/app/4505/)
Vendor Product Version | [Pi-hole® v5.x, FTL 5.x](https://pi-hole.net/)
Add-on has a web UI | Yes, this Add-on contains a configuration page for the Modular Input.

The Pi-hole Add-on allows Splunk data administrators to map the Pi-Hole® DNS server events to the [CIM](https://docs.splunk.com/Splexicon:CommonInformationModel) enabling the data to be used with other Splunk Apps, such as Splunk® App for Enterprise Security.

## Release Notes

```text
Version 1.3.1

NOTE: v1.3.0 of this add-on changed the way the modular input works. If existing modular inputs were setup prior to version v1.3.0, action must be taken to ensure those inputs continue to function correctly. See the docs for updating to new modular inputs (https://splunk-pihole-ta-documentation.readthedocs.io/en/latest/getting-started/configure-inputs/configure-modinput/#updating-to-new-modular-inputs)

- fixed issue causing internal logs to produce a checkpointer not defined error #28
- updated field extractions to include dnssec query events introduced in new Pi-Hole version (Core: v5.4, FTL v5.9).
```

## Bugs/Feature Requests

Please open an issue or submit a feature requests at [github.com](https://github.com/ZachChristensen28/TA-pihole_dns/issues)
