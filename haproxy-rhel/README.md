# haproxy-rhel

### Description
This playbook will provision a single HAProxy server with a public IP on the CenturyLink Cloud. It performs the following actions:
* provisions a group
* provisions a server
* installs HAProxy with a basic configuration

### Playbook Variables (defaults in parenthesis)
#### provision_server role
* server_group: (HAProxy) Name of the group the servers will be provisioned in
* datacenter: (VA1) Datacenter server(s) will be provisioned in
* server_name: (HAPXY) Base name of the servers to be provisioned. Max 6 characters
* serverpass: (P@s$w0Rd!) HIGHLY RECOMMEND CHANGING FOR EACH EXECUTION!! This is the root password of the server.
* server_count: (1) The number of servers to provision
* cpu_count: (1) The number of CPU's allocated to each server
* memory_count: (1) The amount of memory allocated to each server
* ports: (80) 'dictionary' The ports to be exposed via the public IP address. Add overrides to this with the following syntax ["-80","-443"]
