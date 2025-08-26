# Implementation & Testing Plan: AI-Powered Theft Prevention Suite

## Quick Reference
**PRP Status:** ✅ Approved  
**Total Tasks:** 10 tasks across 3 conversation batches
**Estimated Timeline:** 3 conversations over 2-3 sessions

## Conversation Batching Strategy
**CRITICAL: Keep batches small to manage context window**
Based on the PRP complexity, create 3 conversation batches:
- **Batch 1:** Foundation (3 micro-tasks: Project setup, mock data, basic Flask)
- **Batch 2:** Core AI Logic (3 micro-tasks: Person detection, POS integration, video processing)
- **Batch 3:** Dashboard & Integration (4 micro-tasks: React frontend, correlation logic, incident display, end-to-end flow)

**Each batch = One conversation session**

---

## BATCH 1: Foundation & Setup
**Status:** ⬜ Not Started  
**Goal:** Setup project structure, create mock POS data, and basic Flask server
**Context Window Strategy:** Fresh conversation, 3 tasks maximum

### Task 1: Project Structure & Mock POS Data
**Status:** ⬜
**Implementation Checklist:**
- [ ] Create backend folder structure: `/backend`, `/frontend/src`, `/data`
- [ ] Create file: `data/mock_pos_transactions.json`
- [ ] Add realistic transaction data with timestamps (10-15 entries for test day)

**Manual Test Commands:**
```bash
# Test command 1
ls -la backend/ frontend/src/ data/
# Expected output: Folders exist with correct structure

# Test command 2  
cat data/mock_pos_transactions.json | head -20
# Expected output: Valid JSON with transaction records including timestamps
```

**Visual Verification:**
- [ ] Open `data/mock_pos_transactions.json` and verify realistic transaction structure
- [ ] Confirm timestamps span a full day (e.g., 9 AM to 8 PM)
- [ ] Check transaction includes: id, timestamp, items_scanned, cashier_id

**Success Criteria:** Project folders created with mock POS database containing timestamped transactions

---

### Task 2: Basic Flask Server Setup
**Status:** ⬜
**Implementation Checklist:**
- [ ] Create file: `backend/app.py`
- [ ] Add Flask server with basic route structure (10 lines max)
- [ ] Add requirements.txt with Flask, opencv-python

**Manual Test Commands:**
```bash
# Test command 1
cd backend && python app.py
# Expected output: Flask server starts on localhost:5000

# Test command 2  
curl http://localhost:5000/health
# Expected output: {"status": "running"}
```

**Visual Verification:**
- [ ] Open browser to http://localhost:5000/health and see JSON response
- [ ] Confirm server runs without errors
- [ ] Verify requirements.txt contains necessary dependencies

**Success Criteria:** Flask server runs successfully with basic health check endpoint

---

### Task 3: POS Data Access Function
**Status:** ⬜
**Implementation Checklist:**
- [ ] Create file: `backend/pos_integrator.py`
- [ ] Add function: `fetch_pos_data_for_timeframe(timestamp)` (10-12 lines max)
- [ ] Add function: `extract_video_timestamp()` placeholder (5 lines)

**Manual Test Commands:**
```bash
# Test command 1
cd backend && python -c "from pos_integrator import fetch_pos_data_for_timeframe; print(fetch_pos_data_for_timeframe('2024-01-15 14:15:00'))"
# Expected output: Transaction data or None if no match

# Test command 2  
python -c "from pos_integrator import fetch_pos_data_for_timeframe; print(len(fetch_pos_data_for_timeframe('2024-01-15')))"
# Expected output: Number of transactions for that day
```

**Visual Verification:**
- [ ] Function returns correct transaction data for valid timestamps
- [ ] Function returns None or empty list for invalid timestamps
- [ ] Code is verbose with clear variable names

**Success Criteria:** POS integration functions work with mock data and return correct transaction records

---

**Batch 1 Completion Checklist:**
- [ ] All tasks marked as ✅ Complete
- [ ] Manual tests passed for each task
- [ ] Integration test: Flask server can fetch POS data via API endpoint
- [ ] Ready for Batch 2: Foundation exists for AI processing and frontend

**Update After Completion:**
When this batch is done, update this section with:
- Actual files created
- Any deviations from plan
- Issues encountered
- Batch completion timestamp

---

## BATCH 2: Core AI Logic
**Status:** ⬜ Not Started
**Goal:** Implement person detection, behavior analysis, and video processing core functions
**Conversation Management:** Fresh start with Batch 1 context

### Task 4: Basic Person Detection Setup
**Status:** ⬜
**Implementation Checklist:**
- [ ] Create file: `backend/person_detector.py`
- [ ] Add function: `detect_people_in_frame(frame)` placeholder (8-10 lines)
- [ ] Add function: `classify_cashier_customer(people_data)` (10-12 lines)

**Manual Test Commands:**
```bash
# Test command 1
cd backend && python -c "from person_detector import detect_people_in_frame; print('Function loaded successfully')"
# Expected output: Function loaded successfully

# Test command 2  
python -c "from person_detector import classify_cashier_customer; print(classify_cashier_customer([{'x': 100}, {'x': 300}]))"
# Expected output: Role classification based on position
```

**Visual Verification:**
- [ ] Functions exist and can be imported without errors
- [ ] Cashier/customer classification logic uses position-based rules
- [ ] Code includes comments explaining detection approach

**Success Criteria:** Person detection foundation ready for video processing

---

### Task 5: Video Processing & Analysis
**Status:** ⬜
**Implementation Checklist:**
- [ ] Create file: `backend/behavior_detector.py`
- [ ] Add function: `track_scanning_motions(video_path)` (12-15 lines)
- [ ] Add function: `count_items_on_counter(frame)` placeholder (8 lines)

**Manual Test Commands:**
```bash
# Test command 1
cd backend && python -c "from behavior_detector import track_scanning_motions; print('Behavior functions loaded')"
# Expected output: Behavior functions loaded

# Test command 2  
python -c "from behavior_detector import count_items_on_counter; print('Item counting ready')"
# Expected output: Item counting ready
```

**Visual Verification:**
- [ ] Functions can process basic video input parameters
- [ ] Scanning motion detection has placeholder logic
- [ ] Item counting function structure exists

**Success Criteria:** Video analysis functions ready to process uploaded files

---

### Task 6: Video-POS Correlation Logic  
**Status:** ⬜
**Implementation Checklist:**
- [ ] Add function to `pos_integrator.py`: `correlate_video_with_pos(video_analysis, pos_data)` (12-15 lines)
- [ ] Add basic incident detection logic comparing counts
- [ ] Add function: `generate_incident_report(correlation_data)` (10 lines)

**Manual Test Commands:**
```bash
# Test command 1
cd backend && python -c "from pos_integrator import correlate_video_with_pos; print('Correlation function ready')"
# Expected output: Correlation function ready

# Test command 2
python -c "from pos_integrator import generate_incident_report; print(generate_incident_report({'discrepancy': 3, 'confidence': 0.8}))"
# Expected output: Incident report with theft probability
```

**Visual Verification:**
- [ ] Correlation logic compares video detection counts with POS transaction data
- [ ] Incident report includes discrepancy details and confidence scoring
- [ ] Functions handle missing data gracefully

**Success Criteria:** Core correlation between video analysis and POS data works with test data

---

**Batch 2 Completion Checklist:**
- [ ] All AI processing functions implemented
- [ ] Video-POS correlation logic working
- [ ] Manual tests confirm function integration
- [ ] Ready for Batch 3: Frontend dashboard and complete user flow

---

## BATCH 3: Dashboard & Integration
**Status:** ⬜ Not Started
**Goal:** Create React frontend, complete API endpoints, and end-to-end theft detection flow
**Conversation Management:** Fresh start with previous batch context

### Task 7: Basic React Dashboard Setup
**Status:** ⬜
**Implementation Checklist:**
- [ ] Create file: `frontend/src/VideoAnalyzer.js`
- [ ] Add basic video upload component (12-15 lines)
- [ ] Create basic project structure with package.json

**Manual Test Commands:**
```bash
# Test command 1
cd frontend && npm install && npm start
# Expected output: React dev server starts on localhost:3000

# Test command 2  
ls -la src/VideoAnalyzer.js
# Expected output: Component file exists
```

**Visual Verification:**
- [ ] Open browser to http://localhost:3000 and see basic upload interface
- [ ] Video upload area is visible and functional
- [ ] React app runs without console errors

**Success Criteria:** Basic React dashboard with video upload capability

---

### Task 8: Flask API Endpoints
**Status:** ⬜
**Implementation Checklist:**
- [ ] Add to `backend/app.py`: POST `/analyze-video` endpoint (10-12 lines)
- [ ] Add GET `/incidents` endpoint (8-10 lines)
- [ ] Connect endpoints to processing functions

**Manual Test Commands:**
```bash
# Test command 1
cd backend && python app.py &
curl -X POST http://localhost:5000/analyze-video -F "video=@test.mp4"
# Expected output: JSON response with analysis status

# Test command 2  
curl http://localhost:5000/incidents
# Expected output: JSON list of incident reports
```

**Visual Verification:**
- [ ] API endpoints respond correctly to requests
- [ ] File upload handling works for video files
- [ ] Endpoints return proper JSON responses

**Success Criteria:** Flask API can receive video uploads and return incident data

---

### Task 9: Incident Display Component
**Status:** ⬜
**Implementation Checklist:**
- [ ] Create file: `frontend/src/IncidentList.js`
- [ ] Add component to display theft incidents (12-15 lines)
- [ ] Show incident details: timestamp, discrepancy, confidence

**Manual Test Commands:**
```bash
# Test command 1
cd frontend && npm test IncidentList
# Expected output: Component renders without errors

# Test command 2  
# Upload a test video through the interface and verify incident display
```

**Visual Verification:**
- [ ] Incident list shows detected theft cases with clear formatting
- [ ] Each incident displays relevant details (time, items detected vs scanned)
- [ ] Component handles empty state (no incidents found)

**Success Criteria:** Dashboard displays theft detection results in readable format

---

### Task 10: End-to-End Integration
**Status:** ⬜
**Implementation Checklist:**
- [ ] Connect React frontend to Flask backend APIs
- [ ] Add error handling for upload and processing failures
- [ ] Complete the full user journey from upload to incident display

**Manual Test Commands:**
```bash
# Test command 1 - Full workflow test
# Start both servers, upload video, verify processing pipeline
cd backend && python app.py &
cd ../frontend && npm start &
# Upload test video through UI and confirm incident appears

# Test command 2 - Error handling
# Upload invalid file and confirm proper error message
```

**Visual Verification:**
- [ ] Complete user flow: upload video → see processing status → view theft incidents
- [ ] Error messages appear for invalid uploads or processing failures
- [ ] Data flows correctly from video analysis through POS correlation to display

**Success Criteria:** Complete working system that detects theft from uploaded videos and displays results

---

**Batch 3 Completion Checklist:**
- [ ] Full end-to-end user journey working
- [ ] React dashboard displays incident reports
- [ ] Flask backend processes videos and correlates with POS data
- [ ] Ready for demo: Upload video, see theft detection results

---

## Conversation Briefing Templates

### Starting Fresh Conversation:
```
I'm implementing AI-Powered Theft Prevention Suite from the PRP document. 

**Completed So Far:**
- [List completed batches/tasks]

**Current Focus - Batch [X]: [Batch Name]**
Tasks for this conversation:
1. [Task name and brief description]
2. [Task name and brief description]

**Key PRP Requirements:**
- Person detection with YOLOv5 for cashier/customer identification
- POS data correlation using timestamp matching
- Video analysis for sweethearting theft detection
- React dashboard with incident reporting

Please help me implement these tasks following the PRP specifications.
```

### Debugging/Reset Template:
```
I need to debug/fix AI-Powered Theft Prevention Suite implementation.

**Issue:**
[Describe what's broken]

**Current State:**
- [What's been built]
- [What's working]
- [What's failing]

**PRP Reference:**
Person detection, POS integration, and video correlation for theft detection

Please help me fix this issue and get back on track.
```

---

## Progress Tracking System

### Status Indicators:
- ⬜ Not Started
- 🟦 In Progress  
- ✅ Complete
- ❌ Blocked
- 🔄 Needs Revision

### Regression Testing Checklist:
After each batch, verify:
- [ ] Mock POS data still accessible
- [ ] Flask server runs without errors
- [ ] Video processing functions work
- [ ] Frontend components render correctly
- [ ] End-to-end data flow remains intact

---

**Generated from:** `docs/prp.md`  
**Date:** August 26, 2025  
**Ready to implement:** Start with Batch 1, Task 1