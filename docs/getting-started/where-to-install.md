# Installation Overview

There are two components to install on your Splunk software.

 - | Type | Name | Package Name | Splunkbase
-- | ---- | ---- | ------------ | ----------
![App](https://prod.cdn.apps.splunk.com/media/public/icons/4d4113a2-7594-11ec-aaf6-9a0e2e58ec69.png) | App | Pi-hole DNS App for Splunk | `pihole_dns_app` | [https://splunkbase.splunk.com/app/4506](https://splunkbase.splunk.com/app/4506)
![TA](https://prod.cdn.apps.splunk.com/media/public/icons/b19de5b0-08b9-11ed-bfc0-8a78f20287ff.png) | Add-on | Pi-hole DNS Addon for Splunk | `TA-pihole_dns` | [https://splunkbase.splunk.com/app/4505](https://splunkbase.splunk.com/app/4505)

## There are two methods for deployment

1. [Single instance deployment](#single-instance-deployments)
2. [Distributed deployment](#distributed-deployments)

For detailed information on where to install Splunk Apps/add-ons, including best practices, can be found at [Splunk Docs: About Installing Splunk add-ons](https://docs.splunk.com/Documentation/AddOns/released/Overview/Wheretoinstall)

<hr/>

### Single instance Deployments

Install the App and add-on to the single instance. For more information see [Splunk Docs: Install add-on in a single-instance Splunk deployment](https://docs.splunk.com/Documentation/AddOns/released/Overview/Singleserverinstall)

![Standalone Deployment](/images/standalone.svg#only-light){ width="400" }
![Standalone Deployment](/images/dark-standalone.svg#only-dark){ width="400" }

<hr/>

### Distributed Deployments

Splunk Instance type | Install App | Install Add-on | Comments
-------------------- | ----------- | -------------- | --------
Search Heads | Yes | Yes | Install app and add-on to all search heads.
Indexers |  No | Yes | Install only the Add-on.
Heavy Forwarders | No | Yes | Install only the Add-on.
Universal Forwarders (UF) | No | **Not required** | The add-on includes an inputs.conf file that is disabled by default. This can be used to create an input on the forwarder if enabled.

The installation steps for deploying Apps/add-ons in a distributed environment can be found at [Splunk Docs: Install an add-on in a distributed Splunk deployment](https://docs.splunk.com/Documentation/AddOns/released/Overview/Distributedinstall)

![Distributed Deployment](../images/distributed.svg#only-light){ width="400" }
![Distributed Deployment](../images/dark-distributed.svg#only-dark){ width="400" }

<hr/>

### Distributed Deployment Compatibility

Distributed deployment feature | Supported | Comments
------------------------------ | --------- | --------
Search Head Clusters | Yes | You can install this add-on to a search head cluster.
Indexer Clusters | Yes | You can install this add-on to a indexer cluster.
Deployment Server | Yes | You can use a deployment server to push this add-on to Splunk Universal Forwarders.

\* For more information, see Splunk's [documentation](https://docs.splunk.com/Documentation/AddOns/released/Overview/Installingadd-ons) on installing Add-ons.
