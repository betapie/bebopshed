import styled from "styled-components";
import colors from "../style/ColorPalette";

const ExternalLink = styled.a`
  color: ${colors.text};
  &:hover {
    color: ${colors.highlight};
  }
`

export {
    ExternalLink
}