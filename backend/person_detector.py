"""
Person detection and classification functions for theft prevention system.
Handles identification of cashiers and customers based on position analysis.
"""

def detect_people_in_frame(frame):
    """
    Placeholder function for person detection in video frame.
    Will integrate with YOLOv5 for actual person detection.
    """
    # Mock detection data for testing - replace with actual YOLO implementation
    mock_people_data = [
        {"x": 100, "y": 200, "width": 50, "height": 150, "confidence": 0.9},
        {"x": 300, "y": 180, "width": 60, "height": 160, "confidence": 0.8}
    ]
    return mock_people_data

def classify_cashier_customer(people_data):
    """
    Classify detected people as cashier or customer based on position.
    Cashiers typically positioned on left side (x < 200), customers on right.
    """
    classified_people = []
    
    for person in people_data:
        person_x_position = person.get("x", 0)
        
        if person_x_position < 200:
            person_role = "cashier"
        else:
            person_role = "customer"
            
        person_with_role = person.copy()
        person_with_role["role"] = person_role
        classified_people.append(person_with_role)
    
    return classified_people