# Release history for the Pi-hole Addon for Splunk

The latest version of the Pi-hole Addon for Splunk is version 1.3.3. See [Release notes for the Pi-hole Add on for Splunk](../../releases/) of the latest version.

## v1.3.2 <small>July 20, 2022</small>

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

## v1.3.1 <small>July 8, 2021</small>

- updated field extractions to include dnssec query events introduced in new Pi-Hole version (Core: v5.4, FTL v5.9).
- fixed issue causing internal logs to produce a checkpointer not defined error [#28](https://github.com/ZachChristensen28/TA-pihole_dns/issues/28)

## v1.3.0 <small>April 28, 2021</small>

!!! note
    This update changes the way the modular input works. If existing modular inputs were setup prior to this version, action must be taken to ensure those inputs continue to function correctly. See [Updating to new modular inputs](/getting-started/configure-inputs/configure-modinput/#updating-to-new-modular-inputs) for more information.

- Added ability to pull regex and domain filters created in the Pi-hole server.
- Updated the Modular input to make more flexible.
- With the upcoming version of Pi-hole® 6.0, the scripted input "pihole_lists.sh" will be deprecated. This information will be available through the REST API in the upcoming release.

## v1.2.8 <small>Feb 20, 2021</small>

- Added scripted input to ingest lists which enable the mapping of blocked queries to originating blocklists -> [#21](https://github.com/ZachChristensen28/TA-pihole_dns/issues/21)

## v1.2.7 <small>Dec 21, 2020</small>

- Added Modular Input for pulling select data from the HTTP API.

## v1.2.6 <small>Oct 18, 2020</small>

- Fixed Regex/Exact query blacklist events not being extracted -> Issue [#9](https://github.com/ZachChristensen28/TA-pihole_dns/issues/9)
- Fixed HTTPS record types fixed (type=65) -> Issue [#10](https://github.com/ZachChristensen28/TA-pihole_dns/issues/10)

## v1.2.5 <small>Sept 1, 2020</small>

- Added compatibility for DHCP events.
- New sourcetype: pihole:dhcp.
