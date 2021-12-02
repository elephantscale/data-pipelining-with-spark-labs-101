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

## Create a seperate environment for Spark libraries

It is a good practice to have seperate environments for different developmnet needs.  This way, we can have clean dev environments and minimize version conflicits.

Here is how to create one using Anaconda

```bash
# list all environments
$   conda env list

# create a new env for Spark with python 3.8
# this will create the env called 'pyspark'
$   conda create --name pyspark  python=3.8

# activate the new env
$   conda activate pyspark

# you will most likely see the terminal prompt change to 'pyspark' indicating that you are in the right dev environment
```

**Note**: Run all the following commands within 'pyspark' environment you just created.

Here are some handy commands to deal with conda environments:

```bash
# list all environments
# The currently active env will have a * next to it
$   conda env list

# activate an env
$   conda activate pyspark

# deactivate
$   conda decativate

# to see all installed packages
$   conda list
```


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
