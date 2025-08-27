import json
import os
from datetime import datetime

def fetch_pos_data_for_timeframe(timestamp):
    """
    Fetch POS transaction data for a specific timeframe.
    Returns transaction data if found, None otherwise.
    """
    data_file_path = os.path.join('..', 'data', 'mock_pos_transactions.json')
    
    try:
        with open(data_file_path, 'r') as file:
            transactions = json.load(file)
        
        # If timestamp contains date only, return all transactions for that day
        if len(timestamp) == 10:  # Format: 2024-01-15
            matching_transactions = []
            for transaction in transactions:
                if transaction['timestamp'].startswith(timestamp):
                    matching_transactions.append(transaction)
            return matching_transactions
        
        # If full timestamp, find exact or closest match
        for transaction in transactions:
            if transaction['timestamp'] == timestamp:
                return transaction
        
        return None
        
    except FileNotFoundError:
        return None

def extract_video_timestamp():
    """
    Placeholder function to extract timestamp from video metadata.
    Will be implemented with actual video processing logic.
    """
    # Placeholder implementation
    return "2024-01-15 14:15:00"

def correlate_video_with_pos(video_analysis, pos_data):
    """
    Correlate video analysis results with POS transaction data.
    Identifies discrepancies between items scanned and items detected in video.
    """
    if not video_analysis or not pos_data:
        return {"error": "Missing video analysis or POS data"}
    
    items_scanned_in_pos = pos_data.get('items_scanned', 0)
    scanning_motions_detected = video_analysis.get('scanning_motions_detected', 0)
    
    discrepancy = scanning_motions_detected - items_scanned_in_pos
    confidence_score = video_analysis.get('confidence_score', 0.0)
    
    correlation_data = {
        "pos_items_scanned": items_scanned_in_pos,
        "video_scanning_motions": scanning_motions_detected,
        "discrepancy": discrepancy,
        "confidence": confidence_score,
        "timestamp": video_analysis.get('timestamp', 'unknown')
    }
    
    return correlation_data

def generate_incident_report(correlation_data):
    """
    Generate incident report based on correlation analysis.
    Returns theft probability and incident details.
    """
    discrepancy = correlation_data.get('discrepancy', 0)
    confidence = correlation_data.get('confidence', 0.0)
    
    # Calculate theft probability based on discrepancy and confidence
    if discrepancy > 0:
        theft_probability = min(0.9, discrepancy * 0.3 + confidence * 0.5)
        incident_type = "potential_theft"
    else:
        theft_probability = 0.1
        incident_type = "normal_transaction"
    
    incident_report = {
        "incident_type": incident_type,
        "theft_probability": round(theft_probability, 2),
        "discrepancy_count": discrepancy,
        "detection_confidence": confidence,
        "timestamp": correlation_data.get('timestamp', 'unknown'),
        "recommendation": "Review video footage" if theft_probability > 0.5 else "No action needed"
    }
    
    return incident_report