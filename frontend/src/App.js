import React, { useRef } from 'react';
import VideoAnalyzer from './VideoAnalyzer';
import IncidentList from './IncidentList';
import './App.css';

function App() {
  const incidentListRef = useRef();

  const handleAnalysisComplete = () => {
    if (incidentListRef.current) {
      incidentListRef.current.refresh();
    }
  };

  return (
    <div className="App">
      <VideoAnalyzer onAnalysisComplete={handleAnalysisComplete} />
      <IncidentList ref={incidentListRef} />
    </div>
  );
}

export default App;