---
hide:
    - navigation
    - toc
---
# Pi-hole Add-on (TA-pihole_dns)

!!! quote ""
    __*Disclaimer*__

    *This Splunk app is __not__ affiliated with* [__Pi-hole__®](https://pi-hole.net) *and is not sponsored or sanctioned by the Pi-hole® team. As such, the included documentation does not contain information on how to get started with the Pi-hole DNS server. Rather, this documentation serves as a guide to help visualize the data in Splunk. Please visit [https://pi-hole.net](https://pi-hole.net) for documentation on installing/configuring your own Pi-hole server.*

    Pi-hole is and the Pi-hole logo are [registered trademarks](https://pi-hole.net/trademark-rules-and-brand-guidelines/) of Pi-hole LLC.

The Pi-hole Add-on allows Splunk data administrators to map the Pi-Hole® DNS server events to the CIM enabling the data to be used with other Splunk Apps, such as the [Pihole App for Splunk](https://splunkbase.splunk.com/app/4506).

## Assumptions

This documentation assumes the following:

1. You have a working Pi-hole server.
2. You have a working Splunk environment.
3. Basic understanding of Splunk and Pi-hole.

## About

Info | Description
------|----------
Version | 1.3.3 - [Splunkbase](https://splunkbase.splunk.com/app/4505) \| [GitHub](https://github.com/ZachChristensen28/TA-pihole_dns)
Vendor Product Version | [Pi-hole® v5.x, FTL 5.x](https://pi-hole.net/)
Splunk CIM | 5.x, 4.x
Add-on has a web UI | Yes, this Add-on contains a configuration page for the Modular Input.

[Get Started](getting-started/pihole-logging-requirements.md){ .md-button .md-button--primary }
