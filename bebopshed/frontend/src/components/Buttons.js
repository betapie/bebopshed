import React from "react";
import styled from "styled-components";
import { Button as BootstrapButton } from "react-bootstrap";
import { ToggleButton as BootstrapToggleButton } from "react-bootstrap";
import colors from "../style/ColorPalette";

const DefaultButton = styled(BootstrapButton)`
  --bs-btn-color: ${colors.text};
  --bs-btn-bg: ${colors.accent};
  --bs-btn-border-color: ${colors.lightAccent};
  --bs-btn-hover-color: ${colors.highlight};
  --bs-btn-hover-bg: ${colors.accent};
  --bs-btn-hover-border-color: ${colors.highlight};
  --bs-btn-focus-shadow-rgb: 49, 132, 253;
  --bs-btn-active-color: #fff;
  --bs-btn-active-bg: ${colors.highlight};
  --bs-btn-active-border-color: ${colors.highlight};
  --bs-btn-active-shadow: inset 0 3px 5pxrgba (0, 0, 0, 0.125);
  --bs-btn-disabled-color: #fff;
  --bs-btn-disabled-bg: #0d6efd;
  --bs-btn-disabled-border-color: #0d6efd;
`;

const ToggleButton = styled(BootstrapToggleButton)`
  --bs-btn-color: ${colors.text};
  --bs-btn-border-color: ${colors.lightAccent};
  --bs-btn-hover-color: ${colors.highlight};
  --bs-btn-hover-bg: ${colors.accent};
  --bs-btn-hover-border-color: ${colors.lightAccent};
  --bs-btn-focus-shadow-rgb: 13, 110, 253;
  --bs-btn-active-color: #fff;
  --bs-btn-active-bg: ${colors.highlight};
  --bs-btn-active-border-color: ${colors.highlight};
  --bs-btn-active-shadow: inset 0 3px 5pxrgba (0, 0, 0, 0.125);
  --bs-btn-disabled-color: #0d6efd;
  --bs-btn-disabled-bg: transparent;
  --bs-btn-disabled-border-color: #0d6efd;
`;

export { DefaultButton, ToggleButton };
