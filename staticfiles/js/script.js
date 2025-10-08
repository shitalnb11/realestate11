const cities = [
  {
    id: 1,
          name: "Hadapsar",
          image: "/static/img/hp.jpg",
          location: "Hadapsar, Pune",
          rate: "4.9",
          description: "Bustling area with IT hubs...",
          builder: "ABC Constructions",
          buildContactNumber: "+91 1234567890",
          area: "1200 sq ft",
          photos: [
            "/static/img/flat1.png",
            "/static/img/flat2.png",
            "/static/img/flat3.png"
    ],
    map: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3783.238082880655!2d73.934155!3d18.501763!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2c1766e5b3c3b%3A0x76b19b5a7f5f2a6b!2sHadapsar%2C%20Pune%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1639559879837!5m2!1sen!2sin"
  },
  {
    id: 2,
          name: "Kothrud",
          image: "/static/img/bengluru.png",
          location: "Kothrud, Pune",
          rate: "4.6",
          description: "One of the oldest residential areas...",
    builder: "XYZ Developers",
    buildContactNumber: "+91 1234567890",
    area: "950 sq ft",
    photos: [
      "/static/img/flat1.png",
            "/static/img/flat2.png",
            "/static/img/flat3.png"
    ],
    map: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3783.845378226033!2d73.807697!3d18.507397!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2bfa5b1e18b2f%3A0xb7cd5d057d2b953f!2sKothrud%2C%20Pune%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1639559879837!5m2!1sen!2sin"
  },
  {
    id: 3,
    name: "Hinjewadi",
    image: "/static/img/hyd.png",
    location: "Hinjewadi, Pune",
    rate: "4.8",
    description: "Pune's largest IT hub, with several phases and huge residential demand.",
    builder: "LMN Properties",
    buildContactNumber: "+91 1234567890",
    area: "1400 sq ft",
    photos: [
    "/static/img/flat1.png",
            "/static/img/flat2.png",
            "/static/img/flat3.png"
    ],
    map: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3782.9146232521995!2d73.729278!3d18.591231!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2bbfcf0e6e0c5%3A0xcebcc7584c2e2a33!2sHinjewadi%2C%20Pimpri-Chinchwad%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1639559879837!5m2!1sen!2sin"
  },
  {
    id: 4,
    name: "Baner",
    image: "/static/img/Goa.png",
    location: "Baner, Pune",
    rate: "4.7",
    description: "Fast-growing suburb with IT parks, premium cafes, and upscale apartments.",
    builder: "Sunshine Realty",
    buildContactNumber: "+91 1234567890",
    area: "1100 sq ft",
    photos: [
      "/static/img/flat1.png",
            "/static/img/flat2.png",
            "/static/img/flat3.png"
    ],
    map: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3782.8873982245147!2d73.774597!3d18.559168!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2bfc4bda917ef%3A0xd9d4c6e3c097db7d!2sBaner%2C%20Pune%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1639559879837!5m2!1sen!2sin"
  },
  {
    id: 5,
    name: "Wakad",
    image: "/static/img/jaipur.png",
    location: "Wakad, Pune",
    rate: "4.5",
    description: "Prime residential hub near Hinjewadi, popular with IT professionals.",
    builder: "Elite Homes",
    area: "1000 sq ft",
    photos: [
      "/static/img/flat1.png",
            "/static/img/flat2.png",
            "/static/img/flat3.png"
    ],
    map: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3782.9573368677286!2d73.761254!3d18.597089!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2b90f3a48f27b%3A0x2c884aabf8a4dc6e!2sWakad%2C%20Pimpri-Chinchwad%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1639559879837!5m2!1sen!2sin"
  },
  {
    id: 6,
    name: "Viman Nagar",
    image: "/static/img/Mumbai.png",
    location: "Wakad, Pune",
    rate: "4.5",
    description: "Prime residential hub near Hinjewadi, popular with IT professionals.",
    builder: "Elite Homes",
    area: "1000 sq ft",
    photos: [
      "/static/img/flat1.png",
            "/static/img/flat2.png",
            "/static/img/flat3.png"
    ],
    map: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3782.9573368677286!2d73.761254!3d18.597089!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2b90f3a48f27b%3A0x2c884aabf8a4dc6e!2sWakad%2C%20Pimpri-Chinchwad%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1639559879837!5m2!1sen!2sin"
  }

];

let scrollPosition = 0;

function renderCarousel(cityList) {
    const carousel = document.getElementById('carousel');
    carousel.innerHTML = '';
    scrollPosition = 0;
    carousel.style.transform = 'translateX(0px)';

    cityList.forEach(city => {
        const card = document.createElement('div');
        card.classList.add('card');

        // ✅ Redirect to Django property page
        card.onclick = () => {
            localStorage.setItem("selectedProperty", JSON.stringify(city));
            window.location.href = "/property/";
        };

        const image = document.createElement('img');
        image.src = city.image;  // ✅ Must start with /static/
        image.alt = city.name;

        const description = document.createElement('div');
        description.classList.add('card-description');
        description.innerHTML = `
            <h4>${city.name}</h4>
            <p>${city.location}</p>
            <p>Rating: ${city.rate}</p>
            <p>${city.description}</p>
        `;

        card.appendChild(image);
        card.appendChild(description);
        carousel.appendChild(card);
    });
}

function moveCarousel(direction) {
    const carousel = document.getElementById('carousel');
    const card = carousel.querySelector('.card');
    if (!card) return;

    const cardWidth = card.offsetWidth + 20;
    const visibleWidth = carousel.parentElement.offsetWidth;
    const totalWidth = carousel.scrollWidth;

    if (direction === 'left') {
        scrollPosition = Math.max(scrollPosition - cardWidth, 0);
    } else {
        scrollPosition = Math.min(scrollPosition + cardWidth, totalWidth - visibleWidth);
    }

    carousel.style.transform = `translateX(-${scrollPosition}px)`;
}

// ✅ Load carousel on page load
renderCarousel(cities);
