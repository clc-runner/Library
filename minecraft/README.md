# minecraft-playbook
Create a minecraft server in the CLC cloud

### DESCRIPTION:
This playbook will provision a Minecraft game server with public IP address in the Centurylink Cloud. The public address only supports 80 for the time being. The high level tasks are as follows:
* provision a group, server, and public IP (single Ubuntu 14.04 x64)
* installs java
* configure environment for minecraft
* propogates minecraft configs
* installs and starts minecraft
* prints the word "Profit"...because it's fun

### REQUIRED
There are a few things that are intentionally left out of the playbook.
* serverpass: this is the root password of the server

### DEPENDENCIES
* Kind of important to have an account in the CLC Cloud
* Pass --extra-args alias variable

### TYPICAL OVERRIDES:
##
* server_name: base name of server [can only be 6 characters or less] (default == MCRAFT)
* datacenter: locate to provision servers (default == WA1)
* minecraft_user: user to install minecraft on the server (default == minecraft)
* minecraft_group: group to install minecraft on the server (default == minecraft)
* minecraft_server_version: version to install (default == 1.8.7)
* minecraft_java_opts: options for java [heap, garbage collection, threads, etc] (defaults == -Xmx1G -Xms1G -XX:+UseConcMarkSweepGC -XX:+CMSIncrementalPacing -XX:ParallelGCThreads=2)
* minecraft_overlord_user: user to rule them all in the game (default == none)
* minecraft_upstart_respawn_limit: number of spawns and time to spawn (default == 3 120)

## server.properties
* allow-flight: false
* allow-nether: true
* announce-player-achievements: true
* difficulty: 1
* enable-command-block: false
* enbale-query: false
* enable-rcon: false
* force-gamemode: false
* gamemode: 0
* generate-structures: true
* generator-settings:
* hardcore: false
* level-seed:
* level-name: ChocolateCremePies
* level-type: DEFAULT
* max-build-height: 256
* max-players: 20
* motd: Welcome to Thunderdome!
* online-mode: true
* op-permission-level: 2
* player-idle-timeout: 0
* pvp: true
* resource-pack:
* server-ip: ip address of the minecraft server. I dont recommend modifying this unless you plan on just running the minecraft install role
* server-port: 25565
* snooper-enabled: true
* spawn-animals: true
* spawn-monsters: true
* spawn-npcs: true
* spawn-protection: 16
* view-distance: 8
* white-list: false
