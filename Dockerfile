# Usa una imagen base de OpenJDK 17
FROM eclipse-temurin:17

# Copia el archivo JAR de tu aplicación al contenedor
COPY build/libs/retosMicroservicios-0.0.1-SNAPSHOT.jar app.jar

# Expone el puerto en el que la aplicación escuchará

# Ejecuta la aplicación Java
ENTRYPOINT ["java", "-jar", "app.jar"]
