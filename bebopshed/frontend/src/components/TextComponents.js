import styled from "styled-components";
import colors from "../style/ColorPalette";

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

const KeyText = styled.div`
  font-family: lilyjazz-chord;
  display: inline;
  font-size: small;
`;

export {
    TextDiv,
    ErrorDiv,
    KeyText,
}