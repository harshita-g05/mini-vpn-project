import './App.css'
import { useState } from 'react';


function App() {
  {/* isConnected tracks vpn connection and starts as false
    setIsConnected  updates value and useState sets starting 
    val to false */}
  const [isConnected, setIsConnected] = useState(false);

  return (
    <div className="dashboard">
      <h1>VPN Dashboard</h1>
      <p>Status: {isConnected ? "Connected" : "Disconnected"}</p>
      <button onClick={() => setIsConnected(!isConnected)}>
        Connect to VPN
      </button>

    </div>
  );
}

export default App;
