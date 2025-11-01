
const puneProperties = [
  {
    id: 1,
    name: "Hadapsar Heights",
    type: "Flat",
    image: "/static/img/hp.jpg",
    location: "Hadapsar, Pune",
    price: "₹ 85 Lakh",
    rate: "4.9",
    description: "Modern 2BHK flat with premium interiors and garden view."
  },
  {
    id: 2,
    name: "Baner Bliss Villa",
    type: "Villa",
    image: "/static/img/Goa.png",
    location: "Baner, Pune",
    price: "₹ 3.1 Crore",
    rate: "4.8",
    description: "Luxurious villa in Baner with private pool and parking."
  },
  {
    id: 3,
    name: "Kothrud Row House",
    type: "Row House",
    image: "/static/img/flat2.png",
    location: "Kothrud, Pune",
    price: "₹ 1.5 Crore",
    rate: "4.7",
    description: "Spacious 3BHK row house with beautiful terrace and balcony."
  },
  {
    id: 4,
    name: "Hinjewadi Elite Homes",
    type: "Flat",
    image: "/static/img/Mumbai.png",
    location: "Hinjewadi, Pune",
    price: "₹ 95 Lakh",
    rate: "4.6",
    description: "Premium flats near IT park with modern amenities."
  }
];

let scrollPosition = 0;

function renderCarousel() {
  const carousel = document.getElementById('carousel');
  carousel.innerHTML = '';

  puneProperties.forEach(property => {
    const card = document.createElement('div');
    card.classList.add('card');

    card.innerHTML = `
      <img src="${property.image}" alt="${property.name}">
      <div class="card-description">
        <span class="property-type">${property.type}</span>
        <h4>${property.name}</h4>
        <p><i class="fas fa-map-marker-alt"></i> ${property.location}</p>
        <p class="price">${property.price}</p>
        <div class="rating">⭐ ${property.rate}</div>
        <p>${property.description}</p>
        <a href="/property/" class="view-btn">View Details</a>
      </div>
    `;
    carousel.appendChild(card);
  });
}

function moveCarousel(direction) {
  const carousel = document.getElementById('carousel');
  const cardWidth = 320;
  const visibleWidth = carousel.parentElement.offsetWidth;
  const totalWidth = carousel.scrollWidth;

  if (direction === 'left') {
    scrollPosition = Math.max(scrollPosition - cardWidth, 0);
  } else {
    scrollPosition = Math.min(scrollPosition + cardWidth, totalWidth - visibleWidth);
  }

  carousel.style.transform = `translateX(-${scrollPosition}px)`;
}

document.addEventListener("DOMContentLoaded", renderCarousel);

