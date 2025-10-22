def scrape_events():
    # Mock events with IDs and ticket prices
    return [
        {
            "id": "1",
            "title": "Sydney Tech Meetup",
            "date": "2025-06-25",
            "link": "https://example.com/event1",
            "tickets": {
                "Standard": 50,
                "VIP": 100,
                "Balcony": 70
            }
        },
        {
            "id": "2",
            "title": "Art Exhibition: Vivid Sydney",
            "date": "2025-06-27",
            "link": "https://example.com/event2",
            "tickets": {
                "General Admission": 30,
                "Premium": 60
            }
        },
        {
            "id": "3",
            "title": "Sydney Food Festival",
            "date": "2025-06-30",
            "link": "https://example.com/event3",
            "tickets": {
                "Entry Only": 20,
                "All Access": 80
            }
        }
    ]
