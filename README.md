# Understaning Your Data Lakehouse

## Installing Docker Desktop on Your OS

For Windows users, although Docker is not natively supported on Windows, we can utilize Windows Subsystem for Linux (WSL2) to run Docker Desktop efficiently on Windows systems. This setup allows us to create a Linux-like environment where Docker can operate seamlessly.

### Step 1: Enable Virtualization (Both Windows & macOS) 
Before beginning, make sure virtualization is enabled in your computer's BIOS settings, which is essential for running Docker.

### Step 2: Install WSL2 (Windows)
Windows Subsystem for Linux (WSL2) provides the necessary compatibility layer to run Linux binaries on Windows. Install it by executing the following command in command line as Administrator:

	wsl --install
 
You may need to restart your computer to complete the installation.

### Step 3: Install Docker Desktop (Both Windows & macOS)
Visit the official Docker website to download Docker Desktop for your OS. 
For Windows, launch the installer and select the option to use WSL2 during the setup process.

### Step 4: Verify Installation (Both Windows & macOS)
Once installed, open Docker Desktop.
Agree to the terms, configure your preferences, and allow Docker to finalize the setup.

### Step 5: Access Docker CLI (Both Windows & macOS)
Docker CLI can be accessed by typing docker in your designated OS. This interface allows you to manage Docker containers, images, and more via command line.

## Downloading the Data Lakehouse

### Download this Repository to Your Local Machine
This repository includes a README.md file and a Data-Lakehouse directory. Within the Data-Lakehouse directory, you'll find separate folders for macOS and Windows. Select the folder corresponding to your operating system, copy it to your desired location, then right-click and choose "Open in Terminal." Ignore the folder for the OS you're not using.

Depending on your chosen directory of operating system, the following subdirectories and files contain:

    conf: Contains configuration files.
    data: Stores data files.
    etc: Contains additional configuration files.
    home-hive: Contains volumes for the hive-metastore container.
    warehouse: Reserved for additional data storage.

Additionally, your chosen OS directory includes the following files:

  	docker-compose.yml: Runs containers using the "docker-compose up -d" command.
  	pyTest.py: Runs the notebook container on the local host.
 
conf:
 
    hive-site.xml: Configuration file for Apache Hive, specifying settings such as metastore connection details, database configurations, and query execution parameters.
    metastore-site.xml: Configuration file for the Hive Metastore service, defining properties related to database connections, authentication, and storage locations.
    
data:

	iris.parq: Data file stored in MiniO.

 etc:
 
	catalog
	config.properties: General configuration file for the project, containing environment-specific settings such as server addresses, API keys, and service endpoints.
	jvm.config: Java Virtual Machine configuration file, specifying JVM options such as heap size, garbage collection settings, and classpath definitions.
	node properties: Configuration file containing properties related to cluster nodes, such as hostnames, IP addresses, and role assignments.
        
etc/catalog:

	hive.properities: Configuration file specifying properties related to Hive Catalog, including storage formats, default database, and catalog implementation details.
	iceberg.properties: Configuration file for Apache Iceberg, containing settings for table management, partitioning, and metadata storage.
        
  home-hive:
  
	Contains volumes for the hive-metastore container.
	
 warehouse:
 
	Reserved for additional data storage.

Component Descriptions:

    Minio: Handles large-scale data storage in an S3-compatible format.
    Hive Metastore: Manages metadata for stored data, ensuring organized data retrieval.
    Apache Iceberg: Provides advanced table format management, improving data access and query efficiency.
    Trino: SQL query engine used for executing complex data analysis queries.
    PostgreSQL: Serves as the backend for the Hive Metastore, storing metadata reliably.

## Running Containers with Docker Compose

### Step 1: Start Services with Docker Compose
In your terminal, navigate to the directory containing your docker-compose.yml.

Execute the following command to start your services in detached mode:

	docker-compose up -d

### Step 3: Verify Running Containers
Confirm your containers are up and running with:

	docker ps
 
If your service includes a web application, try accessing it through your web browser.

### Step 4: Managing with Docker Desktop
Docker Desktop provides a user-friendly GUI to manage containers, images, and other Docker elements.
Use the interface to monitor container status and manage Docker resources.

### Step 5: Conclusion
You've successfully set up Docker Desktop on your OS, ready to launch your containers. Docker is now at your fingertips to aid in development, testing, and more. Enjoy exploring the capabilities of Docker on your Windows machine.


### To access the Trino CLI inside a Docker container, use the following command:

	docker exec -it DOCKER_ID trino

Once inside the Trino CLI, you can execute various commands:

	show catalogs;
	show schemas in hive;
	show tables in hive.iris;
	SELECT COUNT(*) FROM hive.iris.iris_parquet2 WHERE class='Iris-setosa';

### Configuring the Trino Metastore

To configure the Trino metastore, follow these steps:

Start a Docker container with a bash shell:
  
	docker run -it --entrypoint /bin/bash --name metastore-test2 --network trino-minio-iceberg-example_default b97ef5736782
 
 To access the container as root:

	docker exec -it -u root [container-id] bash
 

### Inside the container, execute the following commands:

	  $ $HADOOP_HOME/bin/hadoop fs -mkdir /tmp
	  $ $HADOOP_HOME/bin/hadoop fs -mkdir /user/hive/warehouse
	  $ $HADOOP_HOME/bin/hadoop fs -mkdir /home/hive/warehouse
	  $ $HADOOP_HOME/bin/hadoop fs -chmod g+w /tmp
	  $ $HADOOP_HOME/bin/hadoop fs -chmod g+w /user/hive/warehouse

	  wget https://jdbc.postgresql.org/download/postgresql-42.7.2.jar

	  apt install wget
	  apt install postgresql-client
	
	  psql -h postgres -p 5432 -U postgres
	
	  apt install libpostgresql-jdbc-java
	
	  schematool -dbType postgres -initSchema


## Creating Schemas and Tables

### To create schemas in Trino for data storage, use the following SQL commands:

	CREATE SCHEMA IF NOT EXISTS iris.default WITH (location = 's3a://iris/');
	CREATE SCHEMA IF NOT EXISTS iceberg.iris WITH (location = 's3a://iris/');
	CREATE SCHEMA IF NOT EXISTS hive.iris WITH (location = 's3a://iris/');
	CREATE SCHEMA IF NOT EXISTS hive.fdep WITH (location = 's3a://fdep/');


## To create tables in Trino, use SQL "CREATE TABLE" statements. Here are examples:

### Iceberg Table Creation:

	CREATE TABLE IF NOT EXISTS iceberg.iris.iris_parquet (
	    sepal_length DOUBLE,
	    sepal_width  DOUBLE,
	    petal_length DOUBLE,
	    petal_width  DOUBLE,
	    class        VARCHAR
	) WITH (location = 's3a://iris/iris.parq', format = 'PARQUET');

### Hive Table Creation

	CREATE TABLE IF NOT EXISTS hive.iris.iris_parquet (
	    sepal_length DOUBLE,
	    sepal_width  DOUBLE,
	    petal_length DOUBLE,
	    petal_width  DOUBLE,
	    class        VARCHAR
	) WITH (external_location = 's3a://iris/iris.parq', format = 'PARQUET');

### External Table Creation

	CREATE EXTERNAL TABLE iris_parquet (
	    sepal_length DOUBLE,
	    sepal_width  DOUBLE,
	    petal_length DOUBLE,
	    petal_width  DOUBLE,
	    class        VARCHAR
	) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE LOCATION 's3a://iris/';
 
	CREATE SCHEMA IF NOT EXISTS hive.fdep WITH (location = 's3a://fdep/');

## Running the Notebook Container:

Run the command, then access the images's GUI via Docker Desktop:

	docker run -p 8888:8888 --network fiu-lake_trino quay.io/jupyter/scipy-notebook:2024-03-14 
 
Open the terminal and install pip, using the following command:

	pip install trino

Now, you are able to run the Python notebook to retrieve vast amounts of data. For example, this command: 

	from trino.dbapi import connect
	conn = connect(host="fiu-lake-trino-coordinator-1", port=8080, user="test2", catalog="hive", schema="iris")
	cur = conn.cursor()
	cur.execute("select * from iris_parquet2 where sepal_length>5")
	rows = cur.fetchall()
	print(rows)









