// Seleccionar el formulario
const form = document.getElementById("loan-form");

// Agregar el evento "submit" al formulario
form.addEventListener("submit", async (event) => {
  event.preventDefault(); // Evitar que el formulario recargue la página

  // Capturar los valores de los campos del formulario
  const capital = parseFloat(document.getElementById("capital").value);
  const tasaInteres = parseFloat(document.getElementById("tasa-interes").value);
  const duracionMeses = parseInt(
    document.getElementById("duracion-meses").value
  );
  const periodoCarencia = document.getElementById("periodo-carencia").checked;
  const mesesCarencia = periodoCarencia
    ? parseInt(document.getElementById("meses-carencia").value)
    : 0;

  // Capturar y convertir la fecha al formato DD/MM/AAAA
  const fechaInicioRaw = document.getElementById("fecha-inicio").value; // Formato AAAA-MM-DD
  let fechaInicio = "";
  if (fechaInicioRaw) {
    const [year, month, day] = fechaInicioRaw.split("-"); // Separar los componentes
    fechaInicio = `${day}/${month}/${year}`; // Reorganizar en formato DD/MM/AAAA
  }

  // Validar los campos del formulario
  const errores = [];
  if (isNaN(capital) || capital <= 0) {
    errores.push("Por favor, ingresa un valor válido para el capital.");
  }
  if (isNaN(tasaInteres) || tasaInteres <= 0) {
    errores.push("Por favor, ingresa un valor válido para la tasa de interés.");
  }
  if (isNaN(duracionMeses) || duracionMeses <= 0) {
    errores.push(
      "Por favor, ingresa un valor válido para la duración del préstamo."
    );
  }
  if (periodoCarencia && (isNaN(mesesCarencia) || mesesCarencia < 0)) {
    errores.push(
      "Por favor, ingresa un valor válido para los meses de carencia."
    );
  }
  if (!fechaInicioRaw) {
    errores.push("Por favor, selecciona una fecha de inicio válida.");
  }

  // Mostrar errores si existen
  if (errores.length > 0) {
    alert(errores.join("\n"));
    return;
  }

  // Crear el objeto de datos para enviar al backend
  const requestData = {
    capital,
    tasa_interes: tasaInteres,
    duracion_meses: duracionMeses,
    periodo_carencia: periodoCarencia,
    meses_carencia: mesesCarencia,
    fecha_inicio: fechaInicio, // Usar la fecha formateada correctamente
  };

  try {
    // Realizar la solicitud al backend
    const response = await fetch(
      "http://127.0.0.1:8000/api/prestamos/simular",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(requestData),
      }
    );

    // Manejar errores de respuesta del servidor
    if (!response.ok) {
      const errorData = await response.json();
      alert(`Error del servidor: ${errorData.detail}`);
      return;
    }

    // Obtener la respuesta del backend
    const data = await response.json();

    // Formatear los pagos durante la carencia para mostrar correctamente
    const pagosCarencia =
      data.pagos_carencia.length > 0
        ? data.pagos_carencia.map((pago) => `${pago.toFixed(2)} EUR`).join(", ")
        : "Ninguno";

    // Mostrar los resultados al usuario
    alert(
      `Simulación completada:\n\n` +
        `Cuota mensual: ${data.cuota_mensual.toFixed(2)} EUR\n` +
        `Pagos durante carencia: ${pagosCarencia}\n` +
        `Fecha de finalización: ${data.fecha_finalizacion}`
    );
  } catch (error) {
    // Manejar errores de red u otros problemas
    alert(
      "Ocurrió un error al intentar conectar con el servidor. Inténtalo de nuevo."
    );
    console.error("Error:", error);
  }
});
