# Protocolo inicial de pantalla

Mensajes JSON delimitados por salto de línea sobre UART:

```json
{"type":"identity","chip":"ESP32","mac":"00:00:00:00:00:00","flash_bytes":4194304}
{"type":"integrity","status":"clean","sha256":"...","source":"backup"}
{"type":"event","level":"info","text":"Auditoría iniciada"}
```

La pantalla nunca interpreta una respuesta como autorización de escritura. Una restauración requiere una orden separada, confirmación doble y verificación del hash al terminar.
