import React, { useState, useEffect, useImperativeHandle, forwardRef } from 'react';

const IncidentList = forwardRef((props, ref) => {
  const [incidents, setIncidents] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    fetchIncidents();
  }, []);

  const fetchIncidents = async () => {
    try {
      const response = await fetch('http://localhost:5002/incidents');
      const data = await response.json();
      setIncidents(data.incidents || []);
      setIsLoading(false);
    } catch (error) {
      console.error('Error fetching incidents:', error);
      setIsLoading(false);
    }
  };

  useImperativeHandle(ref, () => ({
    refresh: fetchIncidents
  }));

  if (isLoading) {
    return <div>Loading incidents...</div>;
  }

  if (incidents.length === 0) {
    return <div>No theft incidents detected.</div>;
  }

  return (
    <div style={{ marginTop: '20px' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h3>Theft Detection Results</h3>
        <button 
          onClick={fetchIncidents}
          style={{ 
            padding: '8px 16px', 
            backgroundColor: '#28a745', 
            color: 'white', 
            border: 'none', 
            borderRadius: '5px',
            cursor: 'pointer'
          }}
        >
          Refresh Incidents
        </button>
      </div>
      {incidents.map((incident, index) => (
        <div key={index} style={{ 
          border: '1px solid #ddd', 
          padding: '15px', 
          margin: '10px 0', 
          borderRadius: '5px',
          backgroundColor: incident.theft_probability > 0.7 ? '#ffe6e6' : '#f9f9f9'
        }}>
          <h4>Incident #{index + 1}</h4>
          <p><strong>Type:</strong> {incident.incident_type}</p>
          <p><strong>Theft Probability:</strong> {(incident.theft_probability * 100).toFixed(1)}%</p>
          <p><strong>Items Discrepancy:</strong> {incident.discrepancy_count}</p>
          <p><strong>Detection Confidence:</strong> {(incident.detection_confidence * 100).toFixed(1)}%</p>
          <p><strong>Time:</strong> {incident.timestamp}</p>
          <p><strong>Recommendation:</strong> {incident.recommendation}</p>
        </div>
      ))}
    </div>
  );
});

export default IncidentList;