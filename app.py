from flask import Flask, render_template, request
from datasets import load_dataset
import pandas as pd

app = Flask(__name__)

# Load the dataset (only done once at startup)
df = load_dataset("jniimi/tripadvisor-review-rating")
reviews_df = df['train'].to_pandas()

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    message = ""
    if request.method == "POST":
        hotel_name = request.form.get("hotelName")
        
        # Debugging: Print the hotel name to verify form data
        print("Hotel Name from Form:", hotel_name)

        # Check if the hotel name is provided
        if hotel_name:
            # Filter the dataset based on the hotel name
            filtered_reviews = reviews_df[reviews_df['hotel_name'].str.contains(hotel_name, case=False, na=False)]
            
            # Debugging: Print the filtered results count
            print("Number of matching reviews:", len(filtered_reviews))

            # Check if results are empty and set message accordingly
            if filtered_reviews.empty:
                message = "Hotel not found."
            else:
                # Extract relevant information from filtered reviews
                results = filtered_reviews[['hotel_name', 'review', 'overall']].to_dict(orient='records')
    
    # Render the template with the results and message
    return render_template("index.html", results=results, message=message)

if __name__ == "__main__":
    app.run(debug=True)
