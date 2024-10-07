document.addEventListener('DOMContentLoaded', function () {
  setTimeout(function () {
      // Ocultar el spinner
      document.getElementById('spinner').style.display = 'none';
      // Mostrar el contenido del login
      document.getElementById('login-content').style.display = 'block';
  }, 5000); // 5000 ms = 5 segundos
});