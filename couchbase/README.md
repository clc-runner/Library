#Couch
##Version: 4.0.0-4051 Community Edition (build-4051)
This will install a minimally configured instance of CouchBase in the CLC Cloud. The cluster will be initialized to allocate most of the available memory to the Couch installation.  

No buckets or indexes will be instantiated in this installation.

###What is Couchbase Server?
Couchbase Server is a NoSQL document database with a distributed architecture for performance, scalability, and availability. It enables developers to build applications easier and faster by leveraging the power of SQL with the flexibility of JSON.


###Deploy Couchbase Server as a:
* Document Database
Access, index, and query documents while taking advantage of integrated caching for high performance data access.

* Key/Value Store
Meet high performance requirements for read and write data access while maintaining durability and availability.

* Distributed Cache
Provide scalable, low-latency access to large in-memory data sets, optionally via the memcache API and clients.

###Post Provision Access
To access the newly installed CouchBase instance
 * ensure a VPN tunnel is established into the environment
 * locate an IP of any server in the cluster
 * access the UI in a web browser via http://<server IP>:8091
 * use the administrator user / password combination defined in the job

Additional documentation on using CouchBase can be found <http://developer.couchbase.com/guides-and-references>

![](/Users/zaphodbeeblebrox/Desktop/Screen Shot 2016-07-11 at 9.14.10 AM.png)