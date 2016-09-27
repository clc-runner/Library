Creates a new Centos 6 cluster of servers and deploys Cloudera's CDH v5.8.X agents on each server.

#### Prerequisites  
None  

#### Results  
The job provisions servers with Centos 6 OS installed with the Cloudera agent configured.

The CPU, memory, and disk space can be changed within control (with the exception of Bare Metal) and the cost associated with the different configurations will be incurred on your monthly bill. 

For additional pricing information, you can visit either the [Pricing Catalog](https://control.ctl.io/pricingcatalog#/pricingCatalog) (which requires a Control login) or our [Estimator](https://www.ctl.io/estimator) to look at the cost of different configurations.  

#### Documentation  
* To learn more about Cloudera's CDH distribution of Hadoop see the [Cloudera documentation](http://www.cloudera.com/documentation.html)  

#### Hadoop Server Types  

Clusters are separated into "Manager" servers and "Worker" servers. Manager servers are designed to run the Hadoop management services (NameNode, ResourceManager, etc) and have much lower hard drive requirements than Worker servers which are designed to process and store data.

**Test**  

* 1 Manager standard VM with 8GB RAM, 50GB HDD and 2 cores   
* 1 Worker standard VM with 8GB RAM, 200GB HDD and 4 cores  
* Can be deployed on any data center

**Hyperscale Small**  

* 2 Manager Hyperscale VMs with 16GB RAM, 150GB SSD and 4 cores  
* 4 Worker Hyperscale VMs with 24GB RAM, 1024GB SSD and 8 cores  
* Only deploy to CA3, GB3, IL1, NY1, SG1, UC1, or VA1  

**Hyperscale Large**  
  
* 3 Manager Hyperscale VMs with 32GB RAM, 150GB SSD and 8 cores  
* 10 Worker Hyperscale VMs with 64GB RAM, 1024GB SSD and 16 cores  
* Only deploy to CA3, GB3, IL1, NY1, SG1, UC1, or VA1  

**Bare Metal Medium**  
  
* 3 Manager Hyperscale VMs with 16GB RAM, 150GB SSD and 4 cores  
* 6 Worker Bare Metal servers with 64GB RAM, 8TB HDD and 12 cores  
* Only deploy to GB3 or VA1  

**Bare Metal Large**  

* 3 Manager Hyperscale VMs with 32GB RAM, 150GB SSD and 8 cores  
* 12 Worker Bare Metal servers with 128GB RAM, 12TB HDD and 20 cores  
* Only deploy to GB3 or VA1  

#### Cloudera Manager

When the agent installation is finished, the Hadoop cluster will still need to be configured.

1) In the Control portal, find the lowest-numbered server with the `HDPMGR` prefix.  
2) Get the IP address of this server.  
3) In a web browser, navigate to <ip address>:7180. This is the address for the Clouder Manager server.  
4) Log in with username `admin` password `admin`  
5) Follow the setup process.  
6) Once the setup process is complete, change the admin account login password by clicking `Administration` and selecting `Users`.
