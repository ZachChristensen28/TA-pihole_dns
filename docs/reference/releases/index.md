# Release notes for the Pi-hole Add-on for Splunk

## v1.3.2 <small>July 20, 2022</small>

### Compatibility

Product | Version
--------- | -------
Splunk platform versions | 9.x, 8.x
CIM | 5.x, 4.x
Pi-hole Versions | Pi-hole® v5.x, FTL 5.x

### New

- Added dest field to map to CIM.
- Added dest_port field to forwarded events.
- Added new special domain block field extractions (see Pi-hole pull request for more info: <https://github.com/pi-hole/FTL/pull/1338>).
- Added query_type field.

### Updated

- Updated to new AOB version.
- Updated pihole eventtype.

### Removed

- Removed pihole_lists script
- Removed special characters from reply_code field.

## Known issues

This version of the Pi-hole Add on for Splunk has the following known issues. If no issues appear here, no issues have been reported. Issues can be reported on the [Pi-hole add on for Splunk's Github page](https://github.com/ZachChristensen28/TA-pihole_dns/issues).
