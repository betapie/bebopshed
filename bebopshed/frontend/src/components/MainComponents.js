import React from "react";
import styled from "styled-components";

import colors from "../style/ColorPalette";

const MainWrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 58px - 40px);
`;

const MainContent = styled.div`
  width: 100%;
  max-width: 1100px;
  padding: 5px;
`;

const Panel = styled.div`
  background-color: ${colors.accent};
  border-radius: 10px;
  // padding: 50px 40px;
  padding: 5%;
  border: 2px solid ${colors.lightAccent};
  width: 100%;
  min-width: 300px;
  justify-content: center;
  align-items: center;
  text-align: center;
  color: ${colors.text};
`;

const PanelHeading = styled.div`
  font-size: larger;
`;

const TextDiv = styled.div`
  padding: 5px;
`;

const ErrorDiv = styled.div`
  border: 2px solid ${colors.highlight};
  border-radius: 10px;
  color: ${colors.highlight};
  padding: 5px;
  margin: 5px;
`;

export { 
  MainWrapper, MainContent, Panel, PanelHeading, TextDiv, ErrorDiv 
};
