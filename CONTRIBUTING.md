# Contribuir a MSA-ChipSafe

Este repositorio forma parte de MS ROBOTIKA. Se aceptan mejoras verificables a través de issues y pull requests. La prioridad es la trazabilidad y la claridad sobre lo que funciona.

## Procedimiento

1. Abre un issue para cambios importantes, con el contexto y un caso reproducible.
2. Trabaja en una rama distinta de `main` y mantén las modificaciones acotadas.
3. Documenta la configuración, la prueba y su resultado; adjunta capturas reales solo cuando puedas indicar su origen y modo de obtención.
4. Si se modifican funciones, añade pruebas apropiadas y actualiza README, documentación y registro de cambios.
5. Completa la plantilla del pull request, indicando los casos que no han podido probarse.

## Hardware, radio y seguridad

Solo probar sobre dispositivos o redes propios o autorizados. Documentar placa exacta, firmware, cableado, alimentación, reproducibilidad y si la captura procede de framebuffer, emulador o dispositivo físico. No publicar identificadores de terceros ni secretos Wi-Fi. No presentar alertas heurísticas como prueba de ataque.

## Calidad y derechos

- No publicar claves, tokens, contraseñas, datos personales, rutas privadas, resultados sensibles ni ficheros de compilación accidentales.
- No incluir código de terceros, imágenes, datos o modelos sin verificar derechos de uso y atribuciones.
- Respeta **la licencia realmente presente en este repositorio**. Si no hay archivo LICENSE, solicita aclaración de derechos antes de reutilizar el material; la mera visibilidad pública no otorga licencia de uso.
- No declarar un resultado científico, clínico, industrial o de hardware como certificado si solo se ha ejecutado una demo.
- No añadir dependencias sin justificar su licencia, superficie de ataque, tamaño y compatibilidad.

## Cómo informar de fallos

Incluye versión o commit, plataforma, comportamiento esperado/observado, instrucciones mínimas y registros despersonalizados. Para vulnerabilidades, utiliza el mecanismo privado indicado en [SECURITY.md](SECURITY.md) cuando exista; no pegues exploits, credenciales ni datos confidenciales en issues públicos.
