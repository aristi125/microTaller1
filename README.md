Abrir una Terminal en la ubicacion raiz del proyecto y ejecutar el siguiente comando:

docker build -t imagendocker .

Verificar la creacion de la imagen con:

docker images

Una vez creada la imagen ejecutamos el contenedor a partir de la imagen

docker run -d -p 8082:8082 --name dockercontenedor imagendocker

Verificar correcto funcionamiento con:

docker ps -a
docker logs dockercontenedor
