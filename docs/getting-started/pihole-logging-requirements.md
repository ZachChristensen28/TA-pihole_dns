# Pi-hole Logging Requirements

!!! danger "[Danger, Will Robinson](https://cultural-phenomenons.fandom.com/wiki/Danger,_Will_Robinson)"
    Failing to perform the following will cause this add-on to not extract fields properly

Set `log-queries=extra` in the pihole dnsmasq configuration file. Pi-hole® recommends to make any changes to a new configuration file to avoid changes to be overridden during an update.

1. Create a new file: `/etc/dnsmasq.d/02-pihole-splunk.conf`.
1. Add `log-queries=extra` to the file. save and close the file
1. Restart pi-hole with `pihole restartdns`
