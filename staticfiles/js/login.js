document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('loginForm');
  const passField = document.getElementById('password');
  const togglePass = document.getElementById('togglePass');

  // Bootstrap validation
  form.addEventListener('submit', e => {
    if (!form.checkValidity()) {
      e.preventDefault();
      e.stopPropagation();
    }
    form.classList.add('was-validated');
  });

  // Toggle password visibility
  togglePass.addEventListener('click', () => {
    const icon = togglePass.querySelector('i');
    if (passField.type === 'password') {
      passField.type = 'text';
      icon.classList.replace('bi-eye', 'bi-eye-slash');
    } else {
      passField.type = 'password';
      icon.classList.replace('bi-eye-slash', 'bi-eye');
    }
  });
});



// validation for register form

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('registerForm');
  const passField = document.getElementById('password');
  const confirmField = document.getElementById('confirmPassword');
  const togglePass = document.getElementById('togglePass');
  const confirmFeedback = document.getElementById('confirmFeedback');

  // Form validation
  form.addEventListener('submit', e => {
    // Confirm password check
    if (passField.value !== confirmField.value) {
      confirmField.setCustomValidity('Passwords do not match');
      confirmFeedback.textContent = 'Passwords do not match.';
    } else {
      confirmField.setCustomValidity('');
    }

    if (!form.checkValidity()) {
      e.preventDefault();
      e.stopPropagation();
    }
    form.classList.add('was-validated');
  });

  // Toggle password visibility
  togglePass.addEventListener('click', () => {
    const icon = togglePass.querySelector('i');
    if (passField.type === 'password') {
      passField.type = 'text';
      icon.classList.replace('bi-eye', 'bi-eye-slash');
    } else {
      passField.type = 'password';
      icon.classList.replace('bi-eye-slash', 'bi-eye');
    }
  });

  // Live confirm password validation
  confirmField.addEventListener('input', () => {
    if (passField.value === confirmField.value) {
      confirmField.setCustomValidity('');
    }
  });
});
