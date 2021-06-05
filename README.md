# TA-pihole_dns - Pi-hole Add-on for Splunk

![GitHub](https://img.shields.io/github/license/zachchristensen28/TA-pihole_dns)

Info | Description
------|----------
Version | 2.0.0 - See on [Splunkbase](https://splunkbase.splunk.com/app/4505/)
Vendor Product Version | [Pi-hole® v6.x, FTL 6.x](https://pi-hole.net/)
Add-on has a web UI | Yes, this Add-on contains a configuration page for the Modular Input.

The Pi-hole Add-on allows Splunk data administrators to map the Pi-Hole® DNS server events to the [CIM](https://docs.splunk.com/Splexicon:CommonInformationModel) enabling the data to be used with other Splunk Apps, such as Splunk® App for Enterprise Security.

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
- Removed python2 libraries
- Removed legacy API inputs
- Removed legacy list scripted input
```
## Documentation

Find full documentation for installing this add-on at http://splunk-pihole-ta-documentation.rtfd.io/

## Bugs/Feature Requests

Please open an issue or submit a feature requests at [github.com](https://github.com/ZachChristensen28/TA-pihole_dns)