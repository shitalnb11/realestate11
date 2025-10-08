document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");   // ✅ select actual form
  const nameInput = document.querySelector('input[name="name"]');
  const emailInput = document.querySelector('input[name="email"]');
  const contactInput = document.querySelector('input[name="phone"]');
  const messageInput = document.querySelector('textarea[name="message"]');
  const sendButton = document.querySelector('.app-form-button[type="submit"]');
  const cancelButton = document.querySelector('.app-form-button[type="reset"]');
  const appForm = document.querySelector('.app-form');

  // ✅ Email validation
  function isValidEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email.trim());
  }

  // ✅ Phone validation
  function isValidPhone(phone) {
    const regex = /^\+?\d{7,15}$/;
    return regex.test(phone.trim());
  }

  // ✅ Thank-you message box
  const thankYouMessage = document.createElement('div');
  thankYouMessage.classList.add('thank-you-message');
  thankYouMessage.style.display = 'none';
  thankYouMessage.style.textAlign = 'center';
  thankYouMessage.style.padding = '20px';

  thankYouMessage.innerHTML = `
    <h2 style="color: green; margin-bottom: 20px;">✅ Thank you! Your response has been sent.</h2>
    <a href="/" class="homepage-btn" style="
      display: inline-block;
      padding: 10px 20px;
      background-color: #007bff;
      color: white;
      text-decoration: none;
      border-radius: 30px;
      font-weight: bold;
      transition: background 0.3s ease;
    ">Go to Homepage</a>
  `;

  appForm.parentNode.appendChild(thankYouMessage);

  // ✅ SEND button click
  sendButton.addEventListener("click", function (e) {
    // stop for validation check
    e.preventDefault();

    const name = nameInput.value.trim();
    const email = emailInput.value.trim();
    const contact = contactInput.value.trim();
    const message = messageInput.value.trim();

    // --- Validation ---
    if (name === "") {
      alert("Please enter your name.");
      nameInput.focus();
      return;
    }

    if (email === "") {
      alert("Please enter your email.");
      emailInput.focus();
      return;
    }

    if (!isValidEmail(email)) {
      alert("Please enter a valid email address.");
      emailInput.focus();
      return;
    }

    if (contact === "") {
      alert("Please enter your contact number.");
      contactInput.focus();
      return;
    }

    if (!isValidPhone(contact)) {
      alert("Please enter a valid contact number.");
      contactInput.focus();
      return;
    }

    if (message === "") {
      alert("Please enter your message.");
      messageInput.focus();
      return;
    }

    // ✅ If all good → submit form to Django
    form.submit();          // 🔑 this actually sends data to the server
  });

  // ✅ CANCEL button
  cancelButton.addEventListener("click", function (e) {
    e.preventDefault();
    form.reset();   // clears all fields
  });
});
