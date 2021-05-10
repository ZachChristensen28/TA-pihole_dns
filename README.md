# TA-pihole_dns - Pi-hole Add-on for Splunk

![GitHub](https://img.shields.io/github/license/zachchristensen28/TA-pihole_dns)
[![Documentation Status](https://readthedocs.org/projects/splunk-pihole-ta-documentation/badge/?version=latest)](https://splunk-pihole-ta-documentation.readthedocs.io/en/latest/?badge=latest)

Info | Description
------|----------
Version | 1.3.0 - See on [Splunkbase](https://splunkbase.splunk.com/app/4505/)
Vendor Product Version | [Pi-hole® v5.3.x, FTL 5.8.x](https://pi-hole.net/)
Add-on has a web UI | Yes, this Add-on contains a configuration page for the Modular Input.

The Pi-hole Add-on allows Splunk data administrators to map the Pi-Hole® DNS server events to the [CIM](https://docs.splunk.com/Splexicon:CommonInformationModel) enabling the data to be used with other Splunk Apps, such as Splunk® App for Enterprise Security.

## Release Notes

```TEXT
Version 1.3.0

NOTE: This update changes the way the modular input works. If existing modular inputs were setup prior to this version, action must be taken to ensure those inputs continue to function correctly. See Updating to new modular inputs below or at https://github.com/ZachChristensen28/TA-pihole_dns/wiki/Updating-to-new-modular-Inputs.

New
- Added ability to pull regex and domain filters created in the Pi-hole server.

Updated
- Updated the Modular input to make more flexible.

Deprecated
- With the upcoming version of Pi-hole® 6.0, the scripted input "pihole_lists.sh" will be deprecated. This information will be available through the REST API in the upcoming release.
```

## Documentation

Find full documentation for installing this add-on at http://splunk-pihole-ta-documentation.rtfd.io/

## Bugs/Feature Requests

Please open an issue or submit a feature requests at [github.com](https://github.com/ZachChristensen28/TA-pihole_dns)
