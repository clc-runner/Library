# WARNING!!
### Servers to be updated must be prepped for management!!
The machine(s) need to be on Powershell 3.x or higher.
WinRM also needs to be configured in accordance with the Ansible documentation to allow for plays to be executed against the server. A script to handle the configuration can be found here: https://github.com/ansible/ansible/blob/devel/examples/scripts/ConfigureRemotingForAnsible.ps1

### DESCRIPTION:
This job will bring a windows server up to date on latest patches and service packs according to the users desire. There are various selectors to account for the depth of updating / patching. Set the selectors to 'true' to enable patching and 'false' to disable patching.

### Update Options
* Definition Updates
* Critical Updates
* Security Updates
* Service Packs
* General Updates
* Update Rollups
* Feature Packs
* Application Updates
* Connector Updates
* Developer Kits
* Tools
* Guidance
