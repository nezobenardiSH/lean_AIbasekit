from flask import Flask, jsonify, request
from flask_cors import CORS
from behavior_detector import track_scanning_motions
from pos_integrator import fetch_pos_data_for_timeframe, correlate_video_with_pos, generate_incident_report

app = Flask(__name__)
CORS(app)

# Store incidents in memory (in production, use a database)
incidents_store = []

@app.route('/health')
def health_check():
    return jsonify({"status": "running"})

@app.route('/analyze-video', methods=['POST', 'OPTIONS'])
def analyze_video():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        if 'video' not in request.files:
            return jsonify({"error": "No video file provided"}), 400
        
        video_file = request.files['video']
        print(f"Received file: {video_file.filename}")  # Debug log
        
        video_analysis_result = track_scanning_motions("uploaded_video.mp4")
        pos_data_list = fetch_pos_data_for_timeframe("2024-01-15")
        
        if pos_data_list and len(pos_data_list) > 0:
            pos_data = pos_data_list[0]  # Use first transaction for demonstration
            correlation_result = correlate_video_with_pos(video_analysis_result, pos_data)
            
            # Generate and store incident if there's a discrepancy
            if correlation_result.get('discrepancy', 0) > 0:
                incident = generate_incident_report({
                    "discrepancy": correlation_result['discrepancy'],
                    "confidence": correlation_result['confidence']
                })
                incident['timestamp'] = pos_data.get('timestamp', 'unknown')
                incident['video_file'] = video_file.filename
                incidents_store.append(incident)
                print(f"Incident stored: {incident}")  # Debug log
        else:
            correlation_result = {"error": "No POS data found"}
        
        return jsonify({"status": "analyzed", "analysis": correlation_result})
    except Exception as e:
        print(f"Error in analyze_video: {str(e)}")  # Debug log
        return jsonify({"error": str(e)}), 500

@app.route('/incidents')
def get_incidents():
    # Return actual stored incidents or a default if none exist
    if incidents_store:
        return jsonify({"incidents": incidents_store})
    else:
        # Return empty list if no incidents yet
        return jsonify({"incidents": []})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)