# Configure Modular Input

The TA-pihole_dns modular input will interact with the Pi-hole FTL API using GET requests. 

!!! warning
    The current Pi-hole HTTP API requires a plaintext API key passed as a parameter. 

## Add-on Prerequisites

The Pihole Add-on for Splunk must be set to visible in order to configure the modular input.

1. In Splunk web, navigate to the "Manage Apps" view by clicking the gear icon on the Launcher page or click "Manage Apps" from the "Apps" dropdown next to the Splunk logo on the top left of the screen.
2. In the app list search for "Pihole DNS Add-on" and click "Edit properties" on the right side.
3. Ensure "Visible" is set to Yes and save.

## Updating to new modular Inputs

The following steps are only applicable if you have setup a modular input prior to version 1.3.0. Version 1.3.0 and later can skip to [Setting up new Modular Inputs](#setting-up-new-modular-input)

1. After updating to version 1.3.0 proceed to the Pihole DNS Add-on in Splunk Web.
1. Navigate to Configuration > Account (Tab)
1. Add a new account. The Steps to add a new account can be found below under [Create Account](#create-account)
1. After creating a new account, navigate to Inputs.
1. On the existing Input, click Actions > Edit.
1. for the "Pihole Account" option, select the created account.
1. Click Update.
1. Complete! To add additional Pi-hole servers, continue on to the next steps.

## Setting up new Modular Input

???+ info "Tested Versions"
    Pi-hole **v5.2.4** | Web Interface **v5.4** | FTL **v5.7**
    
    Add-on Version **1.3.0**


### Modular Input Prerequisites

- [Obtain API Credentials](#obtain-api-credentials)
- FQDN/IP of the Pi-hole Instance(s).
- Splunk must be able to reach the Pi-hole server on port 80/tcp.

### Obtain API Credentials

If you are not using a password to log in to the Pi-hole web interface, skip to [Create Account](#create-account)

1. Log in to the Pi-hole web interface.
1. Navigate to Settings > API/Web Interface.
1. Click "Show API token."
1. Save this token for later steps.

### Create Account

At least one account is needed for the modular input to work.

1. Verify Prerequisites have been completed before proceeding. 
1. Log in to the Splunk web interface.
1. Navigate to the Pi-hole Add-on for Splunk > Configuration (Tab).

    ??? question "Not seeing the Pihole Add-on?" 
        Verify the [Add-on Prerequistes](#add-on-prerequisites) have been completed.

1. Add a new Account.
1. Enter a name for the account.
1. Enter the API key. **Note**: if you are not using a password to authenticate to your Pi-hole instance, enter any text here.
1. Enter the IP/FQDN of the Pi-hole instance.
1. Click add.
1. <small>_(optional)_</small> Configure proxy
1. <small>_(optional)_</small> Set logging level

### Create Input

1. Navigate to the Input tab.
2. Click "Create New Input"
3. <small>_(optional)_</small> Create input for System Summary Events see [Modular Input Reference](../../reference/mod-input-reference.md).
4. <small>_(optional)_</small> Create input for Filter Events see [Modular Input Reference](../../reference/mod-input-reference.md).
5. For the selected input, enter a unique name, index, and an interval to run in seconds. <small>_Minimum: 300 (5 minutes)_</small>.
6. Click add.

### Verify 

Once completed the modular input will immediately run. To verify open up a search and run a similar query:

```
index=<chosen index> sourcetype=pihole:*
```

If data does not appear within a few minutes, see [Troubleshooting Modular Inputs](../troubleshooting/troubleshoot-modinputs.md).