# Sourcetypes

Below are a list of sourcetypes which this Add-on uses. It is not necessary to manually set the sourcetype to anything other than `pihole` as this add-on will automatically transform the sourcetype to the appropriate value.

Sourcetype | Description | CIM Data Models
----------- | ----------- | ---------------
`pihole` | Pi-hole DNS events | [Network Resolution](https://docs.splunk.com/Documentation/CIM/latest/User/NetworkResolutionDNS)
`pihole:dhcp` | Pi-hole DHCP events | [Network Sessions](https://docs.splunk.com/Documentation/CIM/latest/User/NetworkSessions)
`pihole:ftl` | Pi-hole FTL events | None
`pihole:system` | Pi-hole API data | None
`pihole:filters` | Pi-hole API data for filters | None
`pihole:lists` | Pi-hole lists | None