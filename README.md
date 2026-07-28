# Análisis de Portafolios y PLN en Foros utilizando LLM

## Integrantes

- Emerson Jácome
- Samuel Villa
- Valeria Vera

---

# Descripción del proyecto

Este proyecto implementa un sistema de análisis de textos académicos utilizando un modelo de lenguaje grande (LLM), con el objetivo de procesar mensajes de foros estudiantiles y portafolios digitales.

El sistema permite clasificar intervenciones de estudiantes, generar resúmenes automáticos, identificar estudiantes que requieren ayuda y evaluar la calidad básica de un portafolio académico mediante técnicas de procesamiento de lenguaje natural utilizando un modelo de inteligencia artificial.

Para la integración del modelo de lenguaje se utiliza **Ollama**, ejecutando localmente el modelo **Llama 3.2**, evitando la dependencia de servicios externos mediante API.

---

# Objetivo

Desarrollar una aplicación capaz de analizar textos académicos para:

- Clasificar mensajes de foros.
- Extraer temas principales.
- Generar resúmenes automáticos.
- Detectar estudiantes con posibles dificultades.
- Evaluar la estructura y calidad de portafolios digitales.

---

# Tecnologías utilizadas

- Python 3.12
- Ollama
- Llama 3.2
- Procesamiento de Lenguaje Natural (PLN)
- Arquitectura por capas
- Consola CLI

---

# Arquitectura del sistema

El proyecto está organizado en tres capas principales:


Proyecto
│
├── Capa 1: Entrada de datos
│
├── Capa 2: Procesamiento con LLM
│
└── Capa 3: Interfaz de usuario


---

# Estructura del proyecto


proyecto/
│
├── main.py
├── requirements.txt
│
├── capa1/
│ └── lector.py
│
├── capa2/
│ ├── llm.py
│ ├── prompts.py
│ ├── clasificador.py
│ ├── resumidor.py
│ ├── ayuda.py
│ └── evaluador.py
│
├── capa3/
│ ├── cli.py
│ ├── menu.py
│ ├── salida.py
│ └── validador.py
│
├── datos/
│ ├── foro.txt
│ └── portafolio.txt
│
└── pruebas/
└── ejemplos.py


---

# Funcionamiento del sistema

## 1. Carga de información

La primera capa permite leer archivos de texto con información de:

- Usuarios.
- Fechas.
- Mensajes del foro.
- Fragmentos de portafolios.

Ejemplo:


Usuario,Fecha,Mensaje
Juan,2026-07-20,¿Cómo hago el ejercicio?


---

## 2. Procesamiento mediante LLM

La segunda capa se encarga de enviar los textos al modelo de inteligencia artificial.

Funciones implementadas:

### Clasificación de mensajes

Clasifica cada intervención en:

- Pregunta
- Respuesta
- Otro


Ejemplo:

Entrada:


¿Cómo hago el ejercicio 5?


Salida:


Pregunta



---

### Resumen automático

Analiza varios mensajes y genera:

- Resumen general.
- Temas principales.
- Problemas frecuentes.

---

### Detección de estudiantes que necesitan ayuda

Identifica mensajes relacionados con:

- Confusión.
- Falta de comprensión.
- Solicitudes de ayuda.

Ejemplo:


"No entiendo nada de esta materia"


Resultado:


El estudiante necesita apoyo.


---

### Evaluación de portafolios

Analiza:

- Coherencia.
- Organización.
- Uso de conceptos.
- Recomendaciones de mejora.

---

# Instalación y configuración

## 1. Instalar dependencias

Ejecutar:

```bash
pip install -r requirements.txt
2. Instalar Ollama

Descargar e instalar Ollama desde:

https://ollama.com

3. Descargar el modelo utilizado

Ejecutar:

ollama pull llama3.2

Verificar:

ollama list

Debe aparecer:

llama3.2:latest
Ejecución del proyecto

Desde la carpeta principal:

python main.py

El sistema mostrará un menú:

==============================
 ANALISIS DE PORTAFOLIOS LLM
==============================

1. Clasificar mensajes del foro
2. Generar resumen del foro
3. Detectar estudiantes que necesitan ayuda
4. Evaluar portafolio
5. Salir
Ejemplo de clasificación

Entrada:

Yo lo resolví usando un ciclo for.

Salida:

Clasificación:
Respuesta

Entrada:

No entiendo cómo realizar el ejercicio.

Salida:

Clasificación:
Pregunta
Características principales

✅ Arquitectura modular por capas.
✅ Uso de inteligencia artificial mediante LLM.
✅ Procesamiento automático de lenguaje natural.
✅ Clasificación de mensajes académicos.
✅ Resumen inteligente de información.
✅ Evaluación automática de textos.
✅ Interfaz de consola funcional.

Conclusiones

El proyecto demuestra la integración de modelos de lenguaje con aplicaciones académicas para facilitar el análisis de información textual.

Mediante el uso de un LLM local, el sistema puede interpretar mensajes de estudiantes y generar información útil para docentes o administradores educativos, permitiendo identificar dudas, analizar participación y mejorar el seguimiento académico.

Autores

Proyecto desarrollado por:

Emerson Jácome
Samuel Villa
Valeria Vera