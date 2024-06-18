document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('form-registroo');
    
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const correo = document.getElementById('correo-form').value;
        const contrasena = document.getElementById('contra-form').value;
        
        localStorage.setItem('correo', correo);
        localStorage.setItem('contrasena', contrasena);
        
        alert('Registro exitoso!');
        
    });
});