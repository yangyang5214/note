## docker file base

> docker 镜像的描述文件，主要用来构建docker镜像的构建文件

### docker file 解析


- docker file build (Context)
- Docker Server
- image(cache)
- image
- .dockerIgnore


### 命令

https://docs.docker.com/engine/reference/builder

- FROM  基于 Base image 构建新的镜像
- MAINTAINER（deprecated）

```
LABEL

https://docs.docker.com/engine/reference/builder/#maintainer-deprecated
```
- RUN 构建镜像时需要的指令
- EXPOSE 

```
EXPOSE <port> [<port>/<protocol>...]

EXPOSE 80/tcp
EXPOSE 80/udp
```

— WORKDIR 

进入容积默认的位置
```
WORKDIR /path/to/workdir
```

- ENV

```
ENV <key> <value>
ENV <key>:<value>
```

- ADD

The ADD instruction copies new files, directories or remote file URLs from <src> and adds them to the filesystem of the image at the path <dest>.

```
- 自动处理 URL
- 解压 tar
```

- COPY

```
--from=<name>
```

- VOLUMME

允许外部挂载的目录

- CMD

多个 CMD, 最后一个生效

设置容器的第一个命令的第一个参数

- ENTRYPOINT

容器启动的第一个命令


### docker test


- CMD

```
# 容器启动执行命令
pi@raspberrypi:~/sda1/docker-file/test$ docker run beer_test3
hello beer!

pi@raspberrypi:~/sda1/docker-file/test$ cat Dockerfile 

FROM ubuntu

RUN echo readme

WORKDIR /opt/beer

CMD ["echo", "hello beer!"]
EXPOSE 80
```












