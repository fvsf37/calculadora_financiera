// Seleccionar el formulario
const form = document.getElementById("loan-form");

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
  const fechaInicio = document.getElementById("fecha-inicio").value;

  // Validar los campos
  if (isNaN(capital) || capital <= 0) {
    alert("Por favor, ingresa un valor válido para el capital.");
    return;
  }

  if (isNaN(tasaInteres) || tasaInteres <= 0) {
    alert("Por favor, ingresa un valor válido para la tasa de interés.");
    return;
  }

  if (isNaN(duracionMeses) || duracionMeses <= 0) {
    alert("Por favor, ingresa un valor válido para la duración del préstamo.");
    return;
  }

  if (periodoCarencia && (isNaN(mesesCarencia) || mesesCarencia < 0)) {
    alert("Por favor, ingresa un valor válido para los meses de carencia.");
    return;
  }

  if (!fechaInicio) {
    alert("Por favor, ingresa una fecha de inicio válida.");
    return;
  }

  // Crear el objeto de datos para enviar al backend
  const requestData = {
    capital,
    tasa_interes: tasaInteres,
    duracion_meses: duracionMeses,
    periodo_carencia: periodoCarencia,
    meses_carencia: mesesCarencia,
    fecha_inicio: fechaInicio, // Debe estar en formato DD/MM/AAAA
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

    // Manejar errores del servidor
    if (!response.ok) {
      const errorData = await response.json();
      alert(`Error del servidor: ${errorData.detail}`);
      return;
    }

    // Obtener la respuesta del backend
    const data = await response.json();

    // Mostrar los resultados al usuario
    alert(
      `Simulación completada:\n\n` +
        `Cuota mensual: ${data.cuota_mensual.toFixed(2)} EUR\n` +
        `Pagos durante carencia: ${data.pagos_carencia.join(", ")} EUR\n` +
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
