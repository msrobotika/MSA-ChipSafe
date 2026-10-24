[![MS ROBOTIKA · ChipSafe](https://raw.githubusercontent.com/msrobotika/msrobotika/main/assets/projects/msa-chipsafe.svg)](https://github.com/msrobotika/msrobotika/blob/main/PROJECTS.md)

[MS ROBOTIKA](https://github.com/msrobotika/msrobotika/blob/main/PROJECTS.md) · [AB Suite](https://github.com/msrobotika/AB-Suite-Core-arquitectura-de-integraci-n) · [Contribuir / Contribute](CONTRIBUTING.md) · [Seguridad / Security](SECURITY.md)

# ChipSafe

**Identifica una placa ESP32 y documenta sus evidencias desde el ordenador.**

**Identify an ESP32 board and document its evidence from your computer.**

[Empezar / Start](#empezar--start) · [Código de la herramienta / Tool source](host/chipsafe.py) · [Estado / Status](docs/PROJECT_STATUS.md) · [Licencia / Licence](LICENSE)

![Vista previa de la interfaz ChipSafe](docs/screenshots/chipsafe.png)

*Vista previa de interfaz; no es una captura de firmware validado en una placa. / Interface preview, not a validated on-device firmware capture.*

## Disponible ahora · Available now

| Operación / Operation | Implementación / Implementation |
| --- | --- |
| Enumerar puertos / List ports | USB-UART mediante pyserial |
| Identificar chip / Identify chip | Consulta de lectura mediante esptool |
| Revisar un archivo / Inspect a file | Tamaño y SHA-256 de una copia existente / Size and SHA-256 of an existing file |
| Guardar informe / Save report | JSON local con fecha, puertos y resultado / Local timestamped JSON |

El ejecutable Python actual no lee una copia completa de flash, no restaura firmware y no escribe en la placa. La pantalla autónoma, microSD y comparación guiada de imágenes pertenecen a la hoja de ruta. / The current Python tool does not perform full flash backup, restore or device writes. Standalone display, microSD and guided image comparison remain roadmap items.

## Empezar · Start

Requiere Python y las dependencias declaradas. / Requires Python and the declared dependencies.

```sh
python -m pip install -r host/requirements.txt
python host/chipsafe.py --help
python host/chipsafe.py --hash copia-existente.bin --out informe.json
```

Sustituye el archivo por una copia que ya tengas. Para consultar una placa propia, elige su puerto: / Replace the file with an existing copy. To query your own board, choose its port:

```sh
python host/chipsafe.py --device COM4 --out placa.json
```

Comprueba `returncode` y el resultado de identificación del informe. Que se genere JSON no garantiza que la consulta a la placa haya funcionado. / Check the identification result and its `returncode`; a saved JSON file alone does not prove a successful device query.

## Desarrollo · Development

Prototipo inicial: las pruebas de CI son estáticas y no acreditan compatibilidad física por modelo. Consulta [protocolo](docs/PROTOCOL.md), [hoja de ruta](docs/ROADMAP.md) y [estado verificable](docs/PROJECT_STATUS.md).

Initial prototype. Static CI does not establish physical compatibility. Original code under [MIT](LICENSE).
