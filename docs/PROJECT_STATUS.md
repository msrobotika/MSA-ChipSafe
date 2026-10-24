# MSA-ChipSafe · Estado técnico

**Revisión:** 2026-10-24 · **Estado:** Prototipo inicial de auditoría de integridad ESP32.

## Evidencias

- Código y README versionados en main.
- Licencia disponible en archivo LICENSE.
- **CI en main:** disponibles [workflow de pruebas](../.github/workflows/ci.yml) y [workflow de calidad documental](../.github/workflows/repository-quality.yml). No equivalen a ensayos con hardware real.
- **Imágenes:** [`docs/screenshots/chipsafe.png`](../docs/screenshots/chipsafe.png).
- **Procedencia:** La imagen existente es una vista previa; no se ha acreditado una captura de hardware real.

## Límites y acciones siguientes

La herramienta `host/chipsafe.py` enumera puertos, consulta la identidad mediante esptool y calcula SHA-256 de una copia existente. No implementa lectura completa de flash, restauración ni escritura. Backup, pantalla autónoma y microSD siguen en la hoja de ruta. La pantalla de muestra no acredita firmware validado.

Restauración/escritura de flash requiere consentimiento explícito, verificación de imagen y aviso de pérdida de datos.

Para considerarlo validado: pruebas de ejecución y de hardware reproducibles, release versionada y evidencia de capturas obtenidas con el firmware o aplicación real. No confundir simulaciones, vistas previas o imágenes de ejemplo con ensayos de campo.
