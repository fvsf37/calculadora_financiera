# Simulador de Préstamos

¡Bienvenido al **Simulador de Préstamos**!  
Este proyecto es una aplicación web que permite simular préstamos financieros, calcular cuotas mensuales, pagos durante el periodo de carencia y la fecha estimada de finalización del préstamo. Está diseñado con un backend en **FastAPI** y un frontend moderno utilizando **TailwindCSS**.

---

## **Características**

- Cálculo de cuotas mensuales según el sistema de amortización francesa.
- Configuración de periodo de carencia (pago solo de intereses).
- Fecha estimada de finalización del préstamo.
- Interfaz visualmente atractiva y responsiva.
- Backend robusto y fácil de integrar con otras aplicaciones.

---

## **Tecnologías utilizadas**

### Backend:

- **Python**: Lógica de cálculo y API.
- **FastAPI**: Framework para construir la API del backend.
- **Uvicorn**: Servidor ASGI para ejecutar el backend.

### Frontend:

- **HTML5 y JavaScript**: Estructura e interacción.
- **TailwindCSS**: Framework de diseño para estilos rápidos y modernos.
- **Google Fonts**: Para una tipografía profesional.

---

## **Requisitos previos**

### **1. Instalación de Node.js**

- Asegúrate de tener instalado Node.js para el frontend. Descárgalo desde [Node.js](https://nodejs.org/).

### **2. Instalación de Python**

- Requiere Python 3.9 o superior. Descárgalo desde [Python.org](https://www.python.org/).

### **3. Clonar el proyecto**

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/simulador_prestamos.git
cd simulador_prestamos
```

---

## **Configuración del proyecto**

### **1. Configuración del backend**

1. Navega a la carpeta raíz del proyecto:

   ```bash
   cd calculadora_financiera
   ```

2. Crea un entorno virtual:

   ```bash
   python -m venv venv
   ```

3. Activa el entorno virtual:

   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Instala las dependencias del backend:

   ```bash
   pip install -r requirements.txt
   ```

5. Ejecuta el servidor del backend:

   ```bash
   uvicorn app.main:app --reload
   ```

6. Accede a la API en:
   - Documentación interactiva: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Punto de inicio: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

### **2. Configuración del frontend**

1. Navega a la carpeta `frontend`:

   ```bash
   cd frontend
   ```

2. Instala las dependencias de Node.js:

   ```bash
   npm install
   ```

3. Compila los estilos de TailwindCSS:

   ```bash
   npx tailwindcss -i ./src/styles.css -o ./dist/styles.css --watch
   ```

4. Abre el archivo `index.html` en tu navegador.

   - O usa un servidor de desarrollo local, como **Live Server** (extensión de Visual Studio Code), para probar la aplicación en tu navegador.

---

## **Uso de la aplicación**

1. Completa el formulario:

   - Ingresa el capital del préstamo.
   - Proporciona la tasa de interés anual (%).
   - Especifica la duración en meses.
   - Selecciona la fecha de inicio del préstamo.
   - (Opcional) Configura un periodo de carencia.

2. Haz clic en el botón "Simular Préstamo".

3. Obtendrás:
   - La cuota mensual.
   - Los pagos durante el periodo de carencia (si aplica).
   - La fecha estimada de finalización del préstamo.

---

## **Estructura del proyecto**

```plaintext
calculadora_financiera/
├── backend/
│   ├── app/
│   │   ├── main.py               # Punto de entrada del backend
│   │   ├── routes/
│   │   │   ├── prestamos.py      # Rutas relacionadas con préstamos
│   │   ├── utils/                # Lógica de cálculo y utilidades
│   │   │   ├── calculos.py
│   │   │   ├── constantes.py
│   │   │   ├── ...
│   └── requirements.txt          # Dependencias del backend
├── frontend/
│   ├── src/
│   │   ├── index.html            # Página principal
│   │   ├── app.js                # Lógica del frontend
│   │   ├── styles.css            # Estilos base con TailwindCSS
│   ├── dist/                     # CSS compilado por TailwindCSS
│   ├── package.json              # Dependencias de Node.js
│   ├── tailwind.config.js        # Configuración de TailwindCSS
└── README.md                     # Información del proyecto
```

---

## **Capturas del proyecto**

_(Agrega capturas de pantalla del diseño y de la API en funcionamiento para que se vea más profesional.)_

---

## **Contribuciones**

Si deseas contribuir al proyecto:

1. Haz un fork del repositorio.
2. Crea una nueva rama:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus cambios y haz un commit:
   ```bash
   git commit -m "Agrega nueva funcionalidad"
   ```
4. Sube los cambios a tu repositorio:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
5. Crea un pull request.

---

## **Licencia**

Este proyecto está bajo la licencia MIT. Puedes consultar el archivo `LICENSE` para más información.
