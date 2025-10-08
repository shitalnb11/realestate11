function filterProperties() {
  const searchText = document.getElementById("searchInput").value.toLowerCase();
  const price = document.getElementById("priceFilter").value;
  const type = document.getElementById("typeFilter").value.toLowerCase();

  // Select the Bootstrap columns (not just the cards)
  const cards = document.querySelectorAll(".col-lg-4");

  // 🎯 Define price ranges (easy to expand later)
  const priceRanges = {
    "5000000": { min: 0, max: 4999999 },        // Below 50L
    "10000000": { min: 5000000, max: 10000000 }, // 50L – 1Cr
    "20000000": { min: 10000000, max: 20000000 }, // 1Cr – 2Cr
    "30000000": { min: 20000001, max: Infinity } // Above 2Cr
  };

  cards.forEach(col => {
    const card = col.querySelector(".property-card");
    const title = card.querySelector("h2").innerText.toLowerCase();
    const loc = card.querySelector(".location").innerText.toLowerCase();
    const details = card.querySelector(".details").innerText.toLowerCase();
    const priceText = card.querySelector(".price").innerText.replace(/[₹,]/g, "");
    const priceValue = parseInt(priceText) || 0;

    let isMatch = true;

    // 🔍 Search filter (title, location, details)
    if (
      searchText &&
      !title.includes(searchText) &&
      !loc.includes(searchText) &&
      !details.includes(searchText)
    ) {
      isMatch = false;
    }

    // 💰 Price filter
    if (price && priceRanges[price]) {
      const { min, max } = priceRanges[price];
      if (priceValue < min || priceValue > max) {
        isMatch = false;
      }
    }

    // 🏠 Type filter (checks title & details for match)
    if (type && !title.includes(type) && !details.includes(type)) {
      isMatch = false;
    }

    // ✅ Show/hide the whole column (keeps Bootstrap grid intact)
    col.style.display = isMatch ? "block" : "none";
  });
}
