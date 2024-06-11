import React, { useState, useEffect, useRef } from 'react';
import './App.scss';
import 'chart.js/auto';
import { Chart } from 'react-chartjs-2';
import HeadsetMicIcon from '@mui/icons-material/HeadsetMic';
import PersonIcon from '@mui/icons-material/Person';
import RestartAltIcon from '@mui/icons-material/RestartAlt';
import SendIcon from '@mui/icons-material/Send';

function App() {
  const [query, setQuestion] = useState<string>('');
  const [messages, setMessages] = useState<any>([{ text: 'Hello! How can I assist you today?', sender: 'bot', chart: {}}]);
  const [loading, setLoading] = useState<boolean>(false);

  const messagesContainerRef = useRef<any>(null);
  const scrollToBottom = () => {
    if (messagesContainerRef.current) {
      messagesContainerRef.current.scrollTop = messagesContainerRef.current.scrollHeight;
    }
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const submitQuestion = async () => {
    setQuestion('');
    setLoading(true);

    const userMessage = { text: query, sender: 'user' };
    setMessages([...messages, userMessage]);

    try {
      const response = await fetch(`generate_chart?query=${query}`);
      const data = await response.json();

      const botMessage = { text: data.response, sender: 'bot', chart: {} };

      if (data.chartjs_code !== '') {
        const newChart = data.chartjs_code;
        botMessage.chart = newChart;
      }

      setMessages([...messages, userMessage, botMessage]);
    } catch (error: any) {
        console.error('Error:', error.message);
        setMessages([...messages, userMessage, { text: 'Error occurred during the API call.', sender: 'bot' }]);
    } finally {
        setLoading(false);
    }
  };

  const handleReset = () => {
    setQuestion('');
    setMessages([{ text: 'Hello! How can I assist you today?', sender: 'bot' }]);
    setLoading(false);
  };

  return (
    <div className="chatbot-interface">
      <div className="messages-container" ref={messagesContainerRef}>
      {messages.map((message: any, index: number) => (
        <div key={index}>
          <div className='message-wrapper'>
            {message.sender === 'bot' && (
              <div className="icon-container">
                <HeadsetMicIcon />
              </div>
            )}
            <div className={`${message.sender}-container`}>
              <div className={`message ${message.sender}`}>
                <p>{message.text}</p>
                {message.chart && Object.keys(message.chart).length > 0 && (
                  <div className='chatbot-chart-style' key={index}>
                    <Chart type={message.chart.type} data={message.chart.data} options={message.chart.options}/>
                  </div>
                )}
              </div>
            </div>
            {message.sender === 'user' && (
              <div className="icon-container-user">
                <PersonIcon />
              </div>
            )}
          </div>
        </div>
      ))}

      {loading && (
        <div className='bot-loading'>
          <div className='message-wrapper'>
            <div className="icon-container">
              <HeadsetMicIcon />
            </div>
            <div className='loading-message bot'>
              <div className='padding-snippet'>
                <div className="snippet" data-title="dot-elastic">
                  <div className="stage">
                    <div className="dot-elastic"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      </div>
      <div className="input-area">
        <input
          type="text"
          placeholder="Ask AI to create a chart"
          value={query}
          onChange={(e) => setQuestion(e.target.value)}
          className="input-field"
          onKeyPress={(e) => e.key === 'Enter' && submitQuestion()}
        />
        <button onClick={handleReset} disabled={loading} className={`send-button chat-reset-button ${loading ? 'disabled' : ''}`}>
          <RestartAltIcon/>
        </button>

        <button onClick={submitQuestion} disabled={loading || !query} className={`send-button ${loading || !query ? 'disabled' : ''}`}>
          <SendIcon/>
        </button>
      </div>
    </div>
  );
}

export default App;
