import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Navbar from "./Navbar";
import LineViewer from "./LineViewer";
import About from "./About";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<LineViewer />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  );
}

export default App;