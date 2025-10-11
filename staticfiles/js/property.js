const property = JSON.parse(localStorage.getItem("selectedProperty"));
 
  if (property) {
      document.getElementById("propertyName").innerText = property.name;
      document.getElementById("propertyLocation").innerText = property.location;
      document.getElementById("propertyBuilder").innerText = property.builder;
      document.getElementById("propertyBuilderContact").innerText = property.buildContactNumber;
      document.getElementById("propertyArea").innerText = property.area;
      document.getElementById("propertyDesc").innerText = property.description;
      document.getElementById("propertyRate").innerText = property.rate;
 
      const photosContainer = document.getElementById("propertyPhotos");
      property.photos.forEach(photo => {
          const img = document.createElement("img");
          img.src = photo;
          photosContainer.appendChild(img);
      });
 
      document.getElementById("propertyMap").src = property.map;
  } else {
      document.querySelector(".property-container").innerHTML = "<p>No property data found.</p>";
  }
 
 
  // Load Google Maps API
  function initMap() {
    const propertyLocation = { lat: parseFloat(property.latitude), lng: parseFloat(property.longitude) };
 
    const map = new google.maps.Map(document.getElementById("propertyMap"), {
      zoom: 15,
      center: propertyLocation,
      mapTypeId: 'roadmap',
      disableDefaultUI: true, // Removes map UI controls
    });
 
    // Add a custom marker
    const marker = new google.maps.Marker({
      position: propertyLocation,
      map: map,
      title: property.name,
      icon: "static/img/marker.png" // Custom marker icon
    });
 
    // Optional: Add InfoWindow
    const infoWindow = new google.maps.InfoWindow({
      content: `<strong>${property.name}</strong><br>${property.location}`
    });
 
    marker.addListener("click", function () {
      infoWindow.open(map, marker);
    });
  }
 
  // Initialize map on page load
  if (property && property.latitude && property.longitude) {
    initMap();
  }
 