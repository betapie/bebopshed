import styled, { keyframes } from "styled-components";
import colors from "../style/ColorPalette";

const rotate360 = keyframes`
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
`;

const Spinner = styled.div`
  animation: ${rotate360} 1s linear infinite;
  transform: translateZ(0);
  
  border-top: 3px solid ${colors.lightAccent};
  border-right: 3px solid ${colors.lightAccent};
  border-bottom: 3px solid ${colors.lightAccent};
  border-left: 6px solid ${colors.highlight};
  background: transparent;
  width: 72px;
  height: 72px;
  border-radius: 50%;
  margin: auto;
  margin-bottom: 30px;
`;

export default Spinner;
