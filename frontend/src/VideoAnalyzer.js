import React, { useState } from 'react';

function VideoAnalyzer({ onAnalysisComplete }) {
  const [selectedVideo, setSelectedVideo] = useState(null);
  const [uploadStatus, setUploadStatus] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);

  const handleVideoSelect = (event) => {
    const video_file = event.target.files[0];
    setSelectedVideo(video_file);
    setUploadStatus(video_file ? `Selected: ${video_file.name}` : '');
  };

  const handleAnalyzeVideo = async () => {
    if (!selectedVideo) {
      setUploadStatus('Please select a video file first');
      return;
    }

    setIsProcessing(true);
    setUploadStatus('Analyzing video...');

    try {
      const formData = new FormData();
      formData.append('video', selectedVideo);

      const response = await fetch('http://localhost:5002/analyze-video', {
        method: 'POST',
        body: formData,
      });

      const result = await response.json();
      
      if (response.ok) {
        setUploadStatus(`Analysis complete! Discrepancy: ${result.analysis.discrepancy} items`);
        if (onAnalysisComplete) {
          onAnalysisComplete();
        }
      } else {
        setUploadStatus(`Error: ${result.error || 'Analysis failed'}`);
      }
    } catch (error) {
      setUploadStatus(`Error: ${error.message}`);
    } finally {
      setIsProcessing(false);
    }
  };

  return (
    <div style={{ padding: '20px', maxWidth: '600px', margin: '0 auto' }}>
      <h2>AI-Powered Theft Prevention - Video Analysis</h2>
      <div style={{ border: '2px dashed #ccc', padding: '40px', textAlign: 'center' }}>
        <input type="file" accept="video/*" onChange={handleVideoSelect} />
        <p>{uploadStatus || 'Select a video file to analyze'}</p>
        <button 
          onClick={handleAnalyzeVideo} 
          disabled={!selectedVideo || isProcessing}
          style={{ 
            marginTop: '10px', 
            padding: '10px 20px', 
            backgroundColor: isProcessing ? '#ccc' : '#007bff', 
            color: 'white', 
            border: 'none', 
            borderRadius: '5px',
            cursor: isProcessing ? 'not-allowed' : 'pointer'
          }}
        >
          {isProcessing ? 'Processing...' : 'Analyze Video'}
        </button>
      </div>
    </div>
  );
}

export default VideoAnalyzer;