# TA-pihole_dns - Pi-hole Add-on for Splunk

![GitHub](https://img.shields.io/github/license/zachchristensen28/TA-pihole_dns)
[![Documentation Status](https://readthedocs.org/projects/splunk-pihole-ta-documentation/badge/?version=latest)](https://splunk-pihole-ta-documentation.readthedocs.io/en/latest/?badge=latest)

Info | Description
------|----------
Version | 1.3.2 - See on [Splunkbase](https://splunkbase.splunk.com/app/4505/)
Vendor Product Version | [Pi-hole® v5.x, FTL 5.x](https://pi-hole.net/)
Add-on has a web UI | Yes, this Add-on contains a configuration page for the Modular Input.

The Pi-hole Add-on allows Splunk data administrators to map the Pi-Hole® DNS server events to the [CIM](https://docs.splunk.com/Splexicon:CommonInformationModel) enabling the data to be used with other Splunk Apps, such as Splunk® App for Enterprise Security.

## Release Notes

```text
Version 1.3.2

NOTE: v1.3.0 of this add-on changed the way the modular input works. If existing modular inputs were setup prior to version v1.3.0, action must be taken to ensure those inputs continue to function correctly. See the docs for updating to new modular inputs (https://splunk-pihole-ta-documentation.readthedocs.io/en/latest/getting-started/configure-inputs/configure-modinput/#updating-to-new-modular-inputs)

- adding dest field to map to CIM
```

## Documentation

Find full documentation for installing this add-on at http://splunk-pihole-ta-documentation.rtfd.io/

## Bugs/Feature Requests

Please open an issue or submit a feature requests at [github.com](https://github.com/ZachChristensen28/TA-pihole_dns)
