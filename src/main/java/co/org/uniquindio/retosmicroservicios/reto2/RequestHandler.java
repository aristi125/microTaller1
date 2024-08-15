package co.org.uniquindio.retosmicroservicios.reto2;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;

import java.io.IOException;
import java.io.OutputStream;
import java.util.HashMap;
import java.util.Map;

public class RequestHandler implements HttpHandler {
    @Override
    public void handle(HttpExchange exchange) throws IOException {
        String response;
        int statusCode;

        if ("GET".equals(exchange.getRequestMethod())) {
            String query = exchange.getRequestURI().getQuery();
            Map<String, String> queryParams = parseQueryParams(query);

            if (queryParams.containsKey("nombre")) {
                String nombre = queryParams.get("nombre");
                response = "Hola " + nombre;
                statusCode = 200;
            } else {
                response = "Solicitud no valida: El nombre es obligatorio";
                statusCode = 400;
            }
        } else {
            response = "Recurso no encontrado";
            statusCode = 404;
        }

        exchange.sendResponseHeaders(statusCode, response.length());
        OutputStream os = exchange.getResponseBody();
        os.write(response.getBytes());
        os.close();
    }

    private Map<String, String> parseQueryParams(String query) {
        Map<String, String> queryParams = new HashMap<>();
        if (query != null && !query.isEmpty()) {
            String[] pairs = query.split("&");
            for (String pair : pairs) {
                String[] keyValue = pair.split("=");
                if (keyValue.length > 1) {
                    queryParams.put(keyValue[0], keyValue[1]);
                } else {
                    queryParams.put(keyValue[0], "");
                }
            }
        }
        return queryParams;
    }
}
