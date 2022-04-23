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
