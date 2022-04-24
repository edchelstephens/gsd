# Dockerfile

- A set of build instructions for docker to follow to build the app and it's dependencies into a container image

# Container Image

- So all the the container image is:
  - App Code + App Dependencies all neatly packaged
  - So we can share it and run it!

# The statement: FROM node:current-alpine (See first-container.Dockerfile)

- Start building this image by grabbing the node:current-alpine image
- this is a special container image with node tools preinstalled,
- and we're gonna use it as foundation, or the bottom layer of our image, to build everything else on top of
- node:current-alpine
- node is the docker hub image,
- current-alpine is the tag.
- node:current-alpine is an Alpine Linux constructs & Node. No OS kernel!

# Every container, when it's running:

    - uses the kernel of the host it's running on

# The container itself doesn't come packaged with its own kernel

# The line:

ENTRYPOINT ["node", "app.js"] (See first-container.Dockerfile)

- is the entry point of the contained app
- it's the command to run each time a container will get started from this image

# An image is basically a 'stopped container'

# And a container is basically a 'running image'

# In Object-Oriented Programming

- An image would be a class and a container is an instance of that class

# Images are build-time constructs

# Containers are run-time constructs

# Containerized App

- An application that runs inside a container

# Virtual Machines virtualize hardware

# Containers virtualize Operating Systems :)

# Each container is basically a virtual operating system

- it has it's own process tree
- own root file system
- its own eth0(the first Ethernet interface) and all the rest

# Just like every VM on a host shares the same hardware

# Every container on a host shares the same OS kernel

# Because there's only a single OS kernel in the container model,

# Containers are smaller, faster and more light weight than Virtual Machines

- Meaning more applications per square foot of infrastructure
- It's because containers are just app code and dependencies!!

# Declarative Deployment

- Describing the desired state of your application in a config file that you use to deploy and manage the app

# Docker swarm mode

- cluster multiple docker hosts into a secure highly available cluster
- The cluster comprises managers and workers, and actually we call the cluster a "swarm"

# A swarm is a cluster of one or more manager nodes and some worker nodes

# The manager hosts the control plane features

# Managers should be highly available, usually 3-5

---

# Docker for Web Developers

---

# Docker Images and Containers

# A docker image is something that's used to build a container

- An image will have the necessary files to run something on an operating system like Ubuntu
  and then you have your application framework, your database and the files that support that

Example images:

- Ubuntu with Node.js and Application Code
- Ubuntu with python and django application code

# A docker container is created by using an image

- A container runs your application
- You use docker images to create running instances of containers
- The container is where the live application runs, where database runs, front end app runs etc

# An image is a read-only template composed of layered filesystems used to share common files and create Docker container instances

# A container is an isolated and secured shipping container created from an image that can be run, started, stopped, moved and deleted
