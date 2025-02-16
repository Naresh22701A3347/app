// App.js
import React from "react";
import Upload from "./Upload"; // Import the Upload component
import "./App.css"; // Import CSS for better styling

function App() {
  return (
    <div className="app-container">
      <h1 className="title">Handwriting Recognition</h1>
      <Upload />
    </div>
  );
}

export default App;