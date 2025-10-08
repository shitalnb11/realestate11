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
