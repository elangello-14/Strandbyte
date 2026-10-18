# Strandbyte

**Strandbyte** es una colección en evolución de ejercicios y mini-herramientas de bioinformática desarrollados en Python. El repositorio documenta un itinerario práctico de aprendizaje: desde operaciones fundamentales sobre ADN hasta el trabajo con archivos FASTA, comparación de secuencias y análisis de *k-mers*.

> Proyecto personal de aprendizaje vinculado a un perfil científico. No pretende sustituir herramientas validadas para investigación, diagnóstico o uso clínico.

## Objetivos

- Consolidar fundamentos de programación aplicados a datos biológicos.
- Practicar manipulación y validación básica de secuencias de ADN.
- Desarrollar utilidades pequeñas, legibles y progresivas.
- Mantener un registro público y reproducible del aprendizaje.

## Contenido

| Fase | Enfoque | Ejemplos |
| --- | --- | --- |
| **Fase 1** | Fundamentos de secuencias de ADN | longitud, conteo de bases, contenido GC, complemento, reverso complementario, validación y menú interactivo |
| **Fase 2** | Análisis de secuencias y FASTA | lectura de FASTA, traducción básica, *k-mers*, comparación de secuencias, mutaciones y resúmenes estadísticos |
| **Otros** | Experimentos de Python | módulos, importaciones y ejercicios aislados |

Los scripts están numerados para reflejar el progreso del itinerario. Los archivos FASTA incluidos son ejemplos pequeños para practicar; no contienen datos clínicos ni identificables.

## Requisitos

- Python 3.11 o superior.
- No se requieren paquetes externos para los ejercicios actuales.

## Uso

Clona el repositorio y ejecuta un script desde la raíz del proyecto:

```bash
git clone https://github.com/elangello-14/Strandbyte.git
cd Strandbyte
python "Fase 1/Proyecto_10.py"
```

Algunos ejercicios de la Fase 2 solicitan por consola la ruta de un archivo FASTA. Puedes usar los archivos de ejemplo disponibles en `Fase 2/`.

## Estado del proyecto

El repositorio está en aprendizaje activo. El código prioriza la práctica y la claridad didáctica sobre ser una biblioteca de producción. La organización, las rutas de importación y las pruebas automatizadas se irán consolidando a medida que avance el proyecto.

## Buenas prácticas

- Valida siempre las secuencias antes de interpretar resultados.
- Trata los resultados como ejercicios computacionales, no como conclusiones biológicas o clínicas.
- No añadas datos personales, datos de pacientes, credenciales ni archivos de configuración local al repositorio.
- Antes de contribuir, comprueba que no se incluyen carpetas `__pycache__`, entornos virtuales ni resultados generados.

## Próximos pasos

- [x] Añadir pruebas automatizadas para las funciones principales.
- [x] Unificar el manejo de rutas e importaciones entre fases.
- [x] Añadir una licencia adecuada antes de aceptar contribuciones.
- [ ] Documentar cada ejercicio con ejemplos de entrada y salida.

## Licencia

Este proyecto está licenciado bajo los términos de la [MIT License](LICENSE).
Hasta que se añada una licencia, el contenido se publica con todos los derechos reservados por defecto.

---

Si te interesa la bioinformática, las sugerencias de mejora, revisiones de código y conversaciones sobre enfoques reproducibles son bienvenidas.
