# SCADA & IoT Industrial Network Infrastructure (INACAP 2026)

## 📖 Descripción del Proyecto
Este repositorio contiene el diseño, configuración y simulación de una arquitectura de red industrial convergente (IT/OT). El proyecto implementa segmentación de red bajo el **Modelo Purdue (ISA-95)** para entornos SCADA, integrando pasarelas de seguridad perimetral (**FortiGate**), conmutación industrial Cisco y microservicios IoT desplegados en contenedores para la supervisión y control de procesos en tiempo real.

---

## 🗺️ Topología de la Red
![Topología GNS3](configuraciones-e-interfaces/topologia.png)

---

## 📂 Estructura del Repositorio
* **`configuraciones-e-interfaces/`** - Plantillas CLI depuradas para switches Cisco y el firewall FortiGate.
* **`scripts-docker/`** - Código y scripts de simulación para PLCs, sensores y actuadores industriales.
* **`ec2/`** - Configuración e integración con servicios en la nube (AWS) para telemetría.

---
**Autor:** Martín Ariel Vásquez Márquez  
**Institución:** INACAP — Ingeniería en Telecomunicaciones, Conectividad y Redes (2026)
