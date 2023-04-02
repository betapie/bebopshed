import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Navbar from "./Navbar";
import LineViewer from "./LineViewer";
import About from "./About";
import Contribute from "./Contribute";
import LegalNotice from "./LegalNotice";
import Footer from "./Footer"

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<LineViewer />} />
        {/* <Route path="/about" element={<About />} /> */}
        <Route path="/contribute" element={<Contribute />} />
        <Route path="/legal_notice" element={<LegalNotice />} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
