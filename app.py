from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Sample data
meals = [
    {"name": "Gourmet Burger", "price": 15, "img": "/static/meals/burger.jpg"},
    {"name": "Vegan Salad", "price": 12, "img": "/static/meals/salad.jpg"},
    {"name": "Grilled Salmon", "price": 25, "img": "/static/meals/salmon.jpg"}
]

celebrities = [
    {"name": "Famous DJ Max", "img": "/static/celebrities/dj_max.jpg"},
    {"name": "Pop Star Anna", "img": "/static/celebrities/anna.jpg"},
    {"name": "Comedian Joe", "img": "/static/celebrities/joe.jpg"}
]

guests = [
    {"name": "VIP Lounge", "description": "Exclusive VIP access with special amenities."},
    {"name": "Open Guest Area", "description": "Spacious and comfortable guest area."}
]

events = [
    {"id": "1", "title": "Sydney Tech Meetup", "date": "2025-06-25", "link": "https://example.com/event1"},
    {"id": "2", "title": "Art Exhibition: Vivid Sydney", "date": "2025-06-27", "link": "https://example.com/event2"}
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/meals")
def meals_page():
    return render_template("meals.html", meals=meals)

@app.route("/celebrities")
def celebrities_page():
    return render_template("celebrities.html", celebrities=celebrities)

@app.route("/guests")
def guests_page():
    return render_template("guests.html", guests=guests)

@app.route("/tickets")
def tickets_page():
    return render_template("tickets.html", events=events)

@app.route("/tickets/<event_id>", methods=["GET", "POST"])
def tickets_detail(event_id):
    event = next((e for e in events if e["id"] == event_id), None)
    if not event:
        return "Event not found", 404

    if request.method == "POST":
        email = request.form.get("email")
        seat_type = request.form.get("seat_type")
        print(f"Email: {email}, Seat: {seat_type} for event {event['title']}")
        return redirect(event["link"])

    # Hardcoded ticket prices for demo
    tickets = {
        "Standard": 50,
        "VIP": 100,
        "Balcony": 70
    }
    return render_template("tickets_detail.html", event=event, tickets=tickets)

if __name__ == "__main__":
    app.run(debug=True)
