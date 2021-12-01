# Pi-hole Add-on for Splunk - TA-pihole_dns

![GitHub](https://img.shields.io/github/license/zachchristensen28/TA-pihole_dns)
[![Documentation Status](https://readthedocs.org/projects/splunk-pihole-ta-documentation/badge/?version=latest)](https://splunk-pihole-ta-documentation.readthedocs.io/en/latest/?badge=latest)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/ZachChristensen28/TA-pihole_dns)
[![Splunkbase App](https://img.shields.io/badge/Splunkbase-TA--pihole__dns-blue)](https://splunkbase.splunk.com/app/4505/)
[![Splunk CIM Version](https://img.shields.io/badge/Splunk%20CIM%20Version-4.x-success)](https://docs.splunk.com/Documentation/CIM/latest/User/Overview)

Info | Description
------|----------
Version | 2.0.0 - See on [Splunkbase](https://splunkbase.splunk.com/app/4505/)
Vendor Product Version | [Pi-hole® v6.x, FTL 6.x](https://pi-hole.net/)

Add-on has a web UI | Yes, this Add-on contains a configuration page for the Modular Input.

The Pi-hole Add-on allows Splunk data administrators to map the Pi-Hole® DNS server events to the [CIM](https://docs.splunk.com/Splexicon:CommonInformationModel) enabling the data to be used with other Splunk Apps, such as Splunk® App for Enterprise Security.

## Documentation

Find full documentation for installing this add-on at http://splunk-pihole-ta-documentation.rtfd.io/

## Release Notes

```TEXT
Version 2.0.0

- Adding new modular inputs to support v6 API
    - Get Domains (List all Domains that have been allowed/denied)
    - Get database stats
    - Get group information
    - Get client information
    - Get DNS cache information
    - Get System stats
    - Get block lists
    - Get System Information
- Adding ability to set interval for modular inputs with a cron schedule
- Removed python2 libraries
- Updated AoB version
- Removed legacy API inputs
- Removed legacy list scripted input
- Updating extractions for dnssec queries
- Added metadata field for use in license estimation
- the latest_release api script will query github to pull latest versions
- adding dest field to map to CIM
```

## Bugs/Feature Requests

Please open an issue or submit a feature requests at [github.com](https://github.com/ZachChristensen28/TA-pihole_dns)
