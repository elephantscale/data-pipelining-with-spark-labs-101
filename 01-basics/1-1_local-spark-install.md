<link rel='stylesheet' href='../assets/css/main.css'/>

# Lab 1-1: Setting up Spark Locally

## Operating System

Setup is easier if you have either **MacOS or Linux**.  
If you are on Windows, download the [docker image](https://hub.docker.com/repository/docker/elephantscale/es-training) and do the setup in the sandbox.

## Software Needed

- Java version 11 or later
- Anaconda Python version 3.x
- A few more python packages
- Spark version 3.0 or latest
- our data files

## Java 11

Download and install JDK (not JRE) v11 or later from [here](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html).  
Verify you have the correct version by doing

```bash
    java -version
```

## Anaconda Python

Download and install Anaconda Python version 3.x from [here](https://www.anaconda.com/download/).

## Install following add-on packages

Open a **new** terminal and run the following command

```bash
$   conda install numpy  pandas  matplotlib  seaborn  jupyter  jupyterlab
$   conda install -c conda-forge findspark
```

## Download Spark

- Download latest Spark from [here](https://spark.apache.org/downloads.html)
- Unzip the downloaded zip file
- where Spark is unzipped is the SPARK_HOME

```bash
$   wget  https://elephantscale-public.s3.amazonaws.com/downloads/spark-3.0.2-bin-hadoop2.7.tgz
$   tar xvf   spark-3.0.2-bin-hadoop2.7.tgz
$   mv  spark-3.0.2-bin-hadoop2.7    spark
```

## Edit  `run-jupyter.sh`

This file is located in the labs directory. 
Edit this file to match your environment.

```bash
# TODO : Edit the following lines   
export PATH=$HOME/anaconda3/bin:$PATH   
export SPARK_HOME=$HOME/apps/spark   
jupyter lab   
```

## Run the labs

```bash
$   ./run-jupyter.sh
```

## Open and run `testing123.ipynb` file

- Run this file under Jupyter environment
- This file will check your setup.  
- If there are no errors here, then you are good to go
