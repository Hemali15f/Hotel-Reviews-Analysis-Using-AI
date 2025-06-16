document.getElementById("search-form").addEventListener("submit", function(event) {
    event.preventDefault();

    let hotelName = document.getElementById("hotel-name").value;
    fetch('/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ hotel_name: hotelName })
    })
    .then(response => response.json())
    .then(data => {
        let reviewsDiv = document.getElementById("reviews");
        reviewsDiv.innerHTML = "";
        if (data.reviews.length > 0) {
            data.reviews.forEach(review => {
                let reviewElement = document.createElement("div");
                reviewElement.classList.add("review");
                reviewElement.innerHTML = `
                    <h3>${review.title}</h3>
                    <p>${review.review}</p>
                    <p><strong>Rating:</strong> ${review.overall}</p>
                `;
                reviewsDiv.appendChild(reviewElement);
            });
        } else {
            reviewsDiv.innerHTML = "<p>No reviews found for the specified hotel.</p>";
        }
    });
});
