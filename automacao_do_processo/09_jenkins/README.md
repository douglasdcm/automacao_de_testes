# Instalação
- Builde a imagem
```
docker build -t myjenkins-blueocean:2.452.2-1 .
```
- Execute o container
```
docker run \
  --name jenkins-blueocean \
  --restart=on-failure \
  --detach \
  --network jenkins \
  --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client \
  --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 \
  --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  myjenkins-blueocean:2.452.2-1
```

# Configuração
- Baixe e extraia o zip [_data.zip](https://drive.google.com/file/d/1IawpLza0dw1UbS8-87yyXuCHR9ZRIewq/view?usp=sharing)
- Entre na pasta `_data`, copie o conteúdo para a dentro do container
```
docker cp . jenkins-blueocean:/var/jenkins_home/
```
- Reincie o container
```
docker stop jenkins-blueocean
docker start jenkins-blueocean
```
- Acesse `localhost:8080` e faça login com o usuário `admin` e senha `admin`
- Execute os jobs e analise os resultados


# Referências
 - [Build cron jobs](https://crontab.guru/)
 - [Instalação docker padrão](https://www.jenkins.io/doc/book/installing/docker/)
 - [Docker](https://docs.docker.com/guides/docker-overview/)