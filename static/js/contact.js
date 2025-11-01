document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const nameInput = document.querySelector('input[name="name"]');
  const emailInput = document.querySelector('input[name="email"]');
  const contactInput = document.querySelector('input[name="phone"]');
  const messageInput = document.querySelector('textarea[name="message"]');
  const sendButton = document.querySelector('.app-form-button[type="submit"]');
  const cancelButton = document.querySelector('.app-form-button[type="reset"]');
  const appForm = document.querySelector('.app-form-group.buttons');

  // ✅ Validation functions
  function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.trim());
  }

  function isValidPhone(phone) {
    return /^\+?\d{7,15}$/.test(phone.trim());
  }

  // ✅ Thank-you message
  const thankYouMessage = document.createElement('div');
  thankYouMessage.classList.add('thank-you-message');
  thankYouMessage.style.display = 'none';
  thankYouMessage.style.textAlign = 'center';
  thankYouMessage.style.padding = '20px';
  thankYouMessage.innerHTML = `
    <h2 style="color: green; margin-bottom: 20px;">✅ Thank you! Your response has been sent successfully.</h2>
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
  form.parentNode.appendChild(thankYouMessage);

  // ✅ Send button click
  sendButton.addEventListener("click", function (e) {
    e.preventDefault();

    // --- validation ---
    const name = nameInput.value.trim();
    const email = emailInput.value.trim();
    const contact = contactInput.value.trim();
    const message = messageInput.value.trim();

    if (!name) return alert("Please enter your name.");
    if (!email) return alert("Please enter your email.");
    if (!isValidEmail(email)) return alert("Please enter a valid email address.");
    if (!contact) return alert("Please enter your contact number.");
    if (!isValidPhone(contact)) return alert("Please enter a valid contact number.");
    if (!message) return alert("Please enter your message.");

    // ✅ Use Fetch API to send data to Django (without page reload)
    fetch(form.action, {
      method: "POST",
      headers: {
        "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
        "Content-Type": "application/x-www-form-urlencoded"
      },
      body: new URLSearchParams({
        name,
        email,
        phone: contact,
        message
      })
    })
    .then(response => {
      if (response.ok) {
        // hide form and show thank you
        form.style.display = "none";
        thankYouMessage.style.display = "block";
      } else {
        alert("Something went wrong. Please try again later.");
      }
    })
    .catch(error => {
      console.error("Error:", error);
      alert("Network error. Please check your connection.");
    });
  });

  // ✅ Cancel button
  cancelButton.addEventListener("click", function (e) {
    e.preventDefault();
    form.reset();
  });
});
