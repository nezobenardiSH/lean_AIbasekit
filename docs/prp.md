# Project Requirements Plan (PRP)

## 1. Core Identity
A web-based AI theft detection system that analyzes uploaded security videos using person detection and movement tracking to identify customers vs cashiers, detect suspicious behaviors like fake scanning, and automatically correlates with POS transaction data to generate incident reports.

## 2. Single Success Scenario  
- User uploads: checkout security video from 2:15 PM showing cashier fake-scanning for customer
- System responds: detects 2 people, identifies 5 items placed, 2 scanning motions, automatically pulls POS data showing only 2 items scanned at 2:15 PM
- User verifies: sees dashboard showing "Theft Detected: 3 items missing from transaction" with video clips and POS receipt comparison

## 3. User Flows
**PRIMARY FLOW:**
1. User starts at dashboard with upload area
2. User uploads video file → system shows "Detecting people and analyzing..."
3. System automatically retrieves POS data matching video timestamp
4. System processes → displays person tracking, behavior analysis, and POS correlation
5. Result: Dashboard shows theft incidents with automatic POS data matching and discrepancy alerts

**ERROR HANDLING:** 
- No POS data for video timeframe → show "No transactions found for this time"
- Multiple transactions in timeframe → show "Multiple transactions detected, reviewing each"
- No people detected → show "Unable to identify cashier/customer in video"

## 4. Technical Stack & Architecture
**STACK:**
- Frontend: React.js with video player and person tracking overlay
- Backend: Python Flask with YOLOv5 for person detection and OpenCV for movement analysis
- Data Storage: Local JSON files simulating POS database with timestamps
- Deployment: Local development server

**FILE STRUCTURE:**
- `/frontend/src/VideoAnalyzer.js` - Video player with detection overlays
- `/backend/app.py` - Flask server and API endpoints  
- `/backend/person_detector.py` - YOLOv5 person detection logic
- `/backend/pos_integrator.py` - Mock POS data retrieval and matching
- `/backend/behavior_detector.py` - Identify scanning vs stealing actions
- `/data/mock_pos_transactions.json` - Fake daily transaction data with timestamps

## 5. API Design & Data Models
**DATA MODELS:**
```
Transaction: {
  id, timestamp, items_scanned, total_amount, 
  cashier_id, item_details
}
Person: {
  id, role (cashier/customer), bounding_box, 
  movements, confidence_score
}
Incident: {
  id, video_timestamp, transaction_id, people_detected, 
  items_detected_video, items_in_pos, discrepancy, theft_probability
}
```

**ENDPOINTS:**
- POST `/analyze-video` - Process video and auto-fetch POS data
- GET `/pos-data/:timestamp` - Retrieve transactions for video timeframe
- GET `/incidents` - Retrieve theft detection results with POS correlation

**STORAGE:** Mock POS JSON database, person tracking results, incident reports with transaction matching

## 6. Core Functions & Data Flow
**FUNCTIONS:**
- `detect_people_in_frame()` - YOLOv5 person detection
- `extract_video_timestamp()` - Get video recording time
- `fetch_pos_data_for_timeframe()` - Auto-retrieve matching transactions
- `track_scanning_motions()` - Identify cashier hand movements
- `count_items_on_counter()` - Detect objects being processed
- `correlate_video_with_pos()` - Match video analysis with transaction data

**FLOW:** Video upload → Extract timestamp → Auto-fetch POS data → Person detection → Behavior analysis → POS correlation → Incident flagging
**INTEGRATION:** Flask processes video, auto-queries mock POS database by timestamp, correlates detection results with transaction records

## 7. Dependencies & Constraints  
**ALLOWED:** 
- YOLOv5 (person detection)
- OpenCV-Python (movement tracking)
- Flask (web framework)

**FORBIDDEN FOR SKELETON:** 
- Real POS system integration (use mock data)
- Complex behavioral AI models (use basic motion detection)
- Real-time processing (uploaded video only)

**LIMITS:** 
- Mock POS data for POC (JSON file with realistic transaction structure)
- Single checkout lane analysis
- Basic timestamp-based POS matching

## 8. Code Quality Requirements
- Verbose, readable code over compact solutions
- Maximum 15 lines per function
- Descriptive variable names (pos_transaction_data, video_timestamp)
- Comments explaining POS correlation logic and WHY
- No nested ternary operators
- No method chaining beyond 2 levels
- Separate files for POS, detection, and correlation concerns
- Explicit error handling for missing POS data
- One responsibility per function

## 9. Definition of Done
**SKELETON COMPLETE WHEN:**
- Can detect and track people in uploaded checkout videos
- Can automatically extract video timestamps and fetch matching POS data
- Can distinguish between cashier and customer positions
- Can identify basic scanning movements and correlate with POS item counts
- Dashboard shows video analysis alongside matching POS transaction details
- Can flag discrepancies between video detection and POS records
- Mock POS database contains realistic daily transaction data with timestamps
- Foundation ready for real POS integration and advanced behavioral detection