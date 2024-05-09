# Data-Lakehouse

The Code directory has the FIU-lake directory, which contains the following subdirectories and files:

    conf: Contains configuration files.
    data: Stores data files.
    etc: Contains additional configuration files.
    home-hive: Contains volumes for the hive-metastore container.
    warehouse: Reserved for additional data storage.

Additionally, the FIU-lake directory includes the following files:

  	docker-compose.yml: Runs containers using the "docker-compose up -d" command.
  	pyTest.py: Runs the notebook container on the local host.
 

conf:
 
    hive-site.xml: Configuration file for Apache Hive, specifying settings such as metastore connection details, database configurations, and query execution parameters.
    metastore-site.xml: Configuration file for the Hive Metastore service, defining properties related to database connections, authentication, and storage locations.
    
data:

	iris.parq: Data file stored in MiniO.
        
etc/catalog:
  
	hive.properities: Configuration file specifying properties related to Hive Catalog, including storage formats, default database, and catalog implementation details.
	iceberg.properties: Configuration file for Apache Iceberg, containing settings for table management, partitioning, and metadata storage.
	config.properties: General configuration file for the project, containing environment-specific settings such as server addresses, API keys, and service endpoints.
	jvm.config: Java Virtual Machine configuration file, specifying JVM options such as heap size, garbage collection settings, and classpath definitions.
	node properties: Configuration file containing properties related to cluster nodes, such as hostnames, IP addresses, and role assignments.
        
  home-hive:
  
	Contains volumes for the hive-metastore container.
	
 warehouse:
 
	Reserved for additional data storage.

We also have the README file, which explains the directory structure for the main directory, Code. Additionally, there is a detailed Installation Guide titled "SecureHaven Installation Guide" in the Code directory, providing step-by-step instructions with screenshots on project installation, configuration file modifications based on the environment, etc. Furthermore, a User Manual document titled "SecureHaven User Manual" is available.

Component Descriptions:

    Minio: Handles large-scale data storage in an S3-compatible format.
    Hive Metastore: Manages metadata for stored data, ensuring organized data retrieval.
    Apache Iceberg: Provides advanced table format management, improving data access and query efficiency.
    Trino: SQL query engine used for executing complex data analysis queries.
    PostgreSQL: Serves as the backend for the Hive Metastore, storing metadata reliably.



