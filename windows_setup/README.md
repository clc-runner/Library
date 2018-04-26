# Ansible Windows Prep
Configure WinRM and Powershell 3 so Ansible plays can be executed against Windows machines.
## NOTE: Your server will restart after the Powershell 3 upgrade has completed

### Description
This job will configure WinRM and install / upgrade to Powershell 3.0. In doing this it will allow for Ansible to be able to perform actions against the Windows servers this has been executed against.

Documentation on the requirements to allow Ansible execution against Windows servers can be found here:
http://docs.ansible.com/ansible/intro_windows.html
