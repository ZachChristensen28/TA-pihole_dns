# Configure Splunk Input

**Objective**: Set the sourcetype to `pihole` in the inputs.conf file on the forwarder.

## Create an Index

???+ info "Optional"
    If you do not wish to create a new index, skip to [Splunk Universal Forwarder Configuration](#splunk-universal-forwarder-configuration).

Splunk stores data in indexes. This add-on may be configured to send to a custom event index instead of the default index, main. For more information and steps to create a new index, see [Splunk Docs: Create events indexes](https://docs.splunk.com/Documentation/Splunk/latest/Indexer/Setupmultipleindexes#Create_events_indexes_2).

### Purpose for Creating a new index

The out of the box Splunk configuration stores all data in the default index, main. It is encouraged to create a new index to ensure optimal performance, for setting retention policies, and for providing stricter access controls. For more information about how Splunk indexes work with add-ons, see [Splunk Docs: Add-ons and indexes](https://docs.splunk.com/Documentation/AddOns/released/Overview/Add-onsandindexes).

## Splunk Universal Forwarder Configuration

!!! danger "Before Proceeding"
    Ensure the [Pi-hole logging requirement](../../pihole-logging-requirements/) has been completed. Failure to set `log-queries=extra` will cause this add-on to not extract fields properly.

???+ note inline
    Unless utilizing a syslog server, this UF should be installed on the same server as the Pi-Hole server.

Download the latest [Splunk Universal Forwarder (UF)](https://www.splunk.com/en_us/download/universal-forwarder.html) appropriate for your server.

Install the UF according to [Splunk Docs: Install the Universal Forwarder](https://docs.splunk.com/Documentation/Forwarder/latest/Forwarder/Installtheuniversalforwardersoftware).

Once installed the configurations can be made. The following is a sample inputs.conf that can be pushed using a deployment server or configured on the UF itself. Place the following configurations in the `../local/inputs.conf` file.

```cfg title="inputs.conf"
[monitor:///var/log/pihole.log]
disabled = 0
sourcetype = pihole
# optionally specify an index, if configured.
# index = dns

[monitor:///var/log/pihole-FTL.log]
disabled = 0
sourcetype = pihole:ftl
# optionally specify an index, if configured.
# index = dns_system
```

Push the configuration to the forwarder, if using a deployment server, or restart the UF if configuring on the UF itself.

## Verify

Verify the setup has completed successfully by navigating to Splunk web and running a search similar to the following:

```shell
index=<chosen index> sourcetype=pihole*
```

If you see data then you are all set! Proceed to [Configuring Modular Inputs](configure-modinput.md) or start visualizing your data by downloading and installing the [Pihole App for Splunk](https://splunkbase.splunk.com/app/4506).

If you are not seeing your data, see [Troubleshooting Monitoring Inputs](../troubleshooting/troubleshoot-inputs.md).
