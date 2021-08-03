# difference-between-Dockerfile-and-docker-compose.

1. Dockerfile is resposible for creating images
2. docker-compose.yml can also create images. Moreover it creates multiple images/containers.
3. Dockerfile can create only one image. docker-compose.yml can create one or more images.
4. docker-compose triggers Dockerfile and then Dockerfile creates image accordingly.
5. if the code resides on github along with Dockerfile then you can build image outof that Dockerfile. Let`s see how to do that:
    a) open power shell
    b) command syntax: docker build github_url
    c) command example: docker build https://github.com/Chaitanya1Github/difference-between-Dockerfile-and-docker-compose.git
6. Now how this works:
   Ans: the command docker build looks for Dockerfile in the given url(repository). Further, Dockerfile handles the job of creating image. 
        this images appear on our local machine. you can check the image if created using command: docker images
7. Now you may think what if I upload docker-compose.yml on github repository and trigger that file from power shell so that I can achieve as many containers I want. But wait this is not possible (atleast it is what i know). Because there is command like: docker compose build github_url
8. but there is one thing you can do:
    a) upload Dockerfile on github
    b) provide the url of github in docker-compose file
