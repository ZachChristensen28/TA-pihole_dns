# TA-pihole_dns - Pi-hole Add-on for Splunk

![GitHub](https://img.shields.io/github/license/zachchristensen28/TA-pihole_dns)

Info | Description
------|----------
Version | 1.3.1 - See on [Splunkbase](https://splunkbase.splunk.com/app/4505/)
Vendor Product Version | [Pi-hole® v5.3.x, FTL 5.8.x](https://pi-hole.net/)
Add-on has a web UI | Yes, this Add-on contains a configuration page for the Modular Input.

The Pi-hole Add-on allows Splunk data administrators to map the Pi-Hole® DNS server events to the [CIM](https://docs.splunk.com/Splexicon:CommonInformationModel) enabling the data to be used with other Splunk Apps, such as Splunk® App for Enterprise Security.

## Release Notes

```TEXT
Version 1.3.1

```

## Navigation

- [Pihole Logging Requirements](#pihole-logging-requirements)
- [Where to Install](#where-to-install)
- [Input Requirements](#input-requirements)
- [Modular Input Setup](#setup-modular-input)
- [Sourcetypes](#sourcetypes)
- [Installation Walkthrough](#installation-walkthrough)
- [Updating to new modular inputs](#updating-to-new-modular-inputs)

## Pihole Logging Requirements

\* ***Failing to perform the following will cause this add-on to not extract fields properly***

Set `log-queries=extra` in the pihole dnsmasq configuration file. Pi-hole® recommends to make any changes to a new configuration file to avoid changes to be overridden during an update.

1. Create a new file: `/etc/dnsmasq.d/02-pihole-splunk.conf`.
1. Add `log-queries=extra` to the file. save and close the file
1. Restart pi-hole with `pihole restartdns`

## Where to Install

Splunk platform Instance type | Supported | Required | Actions required/ Comments
----------------------------- | --------- | -------- | --------------------------
Search Heads | Yes | Yes | Install this add-on to all search heads.
Indexers | Yes | Conditional | Not required if heavy forwarders are used to collect data. Required if using Universal or Light Forwarders.
Heavy Forwarders | Yes | Conditional | Required, if HFs are used to collect this data source.
Universal Forwarders | Yes | Not required | The add-on includes an inputs.conf file that is disabled by default. This can be used to create an input on the forwarder if enabled.

\* For more information, see Splunk's [documentation](https://docs.splunk.com/Documentation/AddOns/released/Overview/Installingadd-ons) on installing Add-ons.

## Input Requirements

Set the sourcetype to `pihole` in the inputs.conf file on the forwarder.

\* ***See [Installation Walkthrough](#Installation-Walkthrough) for more information***

## Setup Modular Input

This modular input interacts with the Pi-hole server's http API. This is currently an unsupported method, however, pi-hole has stated that they have plans to build out the API in the upcoming releases.

**NOTE**: The current Pi-hole HTTP API requires a plaintext API key passed as a parameter and is consided insecure.

The following steps can also be found at the [Modular Input Setup](https://github.com/ZachChristensen28/TA-pihole_dns/wiki/Modular-Input-Setup) Wiki on Github.

```
Tested on: Pi-hole v5.2.4 Web Interface v5.4 FTL v5.7
Add-on Version: 1.3.0
```

If you have setup modular inputs prior to version 1.3.0, please see [Updating to new modular inputs](#updating-to-new-modular-inputs) before proceeding.

### Prerequisites

- Obtain API Credentials.
- FQDN/IP of the Pi-hole Instance(s).
- Splunk must be able to reach the Pi-hole server on port 80/tcp.

#### Obtain API Credentials

If you are not using a password to log in to the Pi-hole web interface the following steps are not needed.

1. Log in to the Pi-hole web interface.
1. Navigate to Settings > API/Web Interface.
1. Click "Show API token."
1. Save this token for later steps.

### Setup Modular Input

#### Create Account

At least one account is needed for the modular input to work.

1. Verify Prerequisites have been completed before proceeding.
1. Log in to the Splunk web interface.
1. Navigate to the Pi-hole Add-on for Splunk > Configuration (Tab).
1. Add a new Account.
1. Enter a name for the account.
1. Enter the API key. **Note**: if you are not using a password to authenticate to your Pi-hole instance, enter any string here.
1. Enter the IP/FQDN of the Pi-hole instance.
1. Click add.

(Optional)
- Configure proxy
- Set logging level

### Create Input

1. Navigate to the Input tab.
2. Click "Create New Input"
3. (optional) Create input for System Summary Events:
  - This input will pull summary information including domains in database, version, and when gravity was last updated.
4. (optional) Create input for Filter Events:
  - This input will pull the configured regex and domain filters create in Pi-hole to block or allow domains.
5. For the selected input, enter a unique name, index, and an interval to run in seconds. min 300 (5 minutes).
6. Click add.

Once completed the modular input will immediately run. To verify open up a search and run a similar query:

```
index=<chosen index> sourcetype=pihole:*
```

### Troubleshooting

If no logs appear in the index you specified after configuring the input, use the following to troubleshoot.

1. Set the logging mode to "Debug" on the Configuration Tab.
1. Search the internal logs for errors:

```
index=_internal sourcetype="tapiholedns:log"
```

## Sourcetypes

Below are a list of sourcetypes which this Add-on uses. The `pihole:dhcp` sourcetype will automatically be transformed when the `pihole` sourcetype is set in the inputs configuration.

Source type | Description | CIM Data Models
----------- | ----------- | ---------------
`pihole` | Pi-hole DNS events | [Network Resolution](https://docs.splunk.com/Documentation/CIM/latest/User/NetworkResolutionDNS)
`pihole:dhcp` | Pi-hole DHCP events | [Network Sessions](https://docs.splunk.com/Documentation/CIM/latest/User/NetworkSessions)
`pihole:ftl` | Pi-hole FTL events | None
`pihole:system` | Pi-hole API data | None
`pihole:lists` | Pi-hole lists | None
`pihole:filters` | Pi-hole regex/domain filters created to block domains | None

## Installation Walkthrough

### Splunk Universal Forwarder Configuration

Download the latest [Splunk Universal Forwarder (UF)](https://www.splunk.com/en_us/download/universal-forwarder.html) appropriate for your server. _This UF should be installed on the same server as the Pi-Hole server_.

Install the UF according to [Splunk Docs](https://docs.splunk.com/Documentation/Forwarder/latest/Forwarder/Installtheuniversalforwardersoftware).

Once installed the configurations can be made. The following is a sample inputs.conf that can be pushed using a deployment server or configured on the UF itself. Place the following configurations in the `../local/inputs.conf` file.

```SHELL
# inputs.conf
[monitor:///var/log/pihole.log]
disabled = 0
sourcetype = pihole
# optionally specify an index, if configured.
# index = dns

[monitor:///var/log/pihole-FTL.log]
disabled = 0
sourcetype = pihole:ftl
# optionally specify an index, if configured.
# index = dns
```

**(Deprecated)** Additionally, it is recommended to enable the scripted input to allow mapping of blocked queries to the originating blocklists.

```SHELL
[script://./bin/pihole_lists.sh]
disabled = 0
sourcetype = pihole:lists
# Everyday at 4:01 AM
interval = 1 4 * * *
# optionally specify an index, if configured.
# index = dns
```

**Note:** The `interval` can be specified as a cron schedule or in seconds. It is recommended to use a cron schedule to avoid the script from executing on startup. For more information see Splunk's documentation for intervals in [inputs.conf](https://docs.splunk.com/Documentation/Splunk/latest/Admin/Inputsconf).

Push the configuration to the forwarder, if using a deployment server, or restart the UF if configuring on the UF itself.

## Updating to new modular Inputs

The included steps are only applicable if you have setup a modular input prior to version 1.3.0. Version 1.3.0 and later can follow the steps included in the [Modular Input Setup](https://github.com/ZachChristensen28/TA-pihole_dns/wiki/Modular-Input-Setup) Wiki.

## Steps

1. After updating to version 1.3.0 proceed to the Pihole DNS Add-on in Splunk Web.
1. Navigate to Configuration > Account (Tab)
1. Add a new account. Steps to create a new account can be found in the [Modular Input Setup](https://github.com/ZachChristensen28/TA-pihole_dns/wiki/Modular-Input-Setup) Wiki.
1. After creating a new account, navigate to Inputs.
1. On the existing Input, click Actions > Edit.
1. for the "Pihole Account" option, select the created account.
1. Click Update.

The existing Input should now function as expected. For any new inputs or accounts follow the instructions in the [Modular Input Setup](https://github.com/ZachChristensen28/TA-pihole_dns/wiki/Modular-Input-Setup) Wiki.

## Bugs/Feature Requests

Please open an issue or submit a feature requests at [github.com](https://github.com/ZachChristensen28/TA-pihole_dns)
