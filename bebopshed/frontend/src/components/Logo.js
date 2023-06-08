import React from 'react';
import { ReactComponent as LogoSvg } from '@static/bebopshed_logo_stylable.svg';

import styled from "styled-components";

import colors from "../style/ColorPalette";

const StyledLogoSvg = styled(LogoSvg)`
  height: 30px;
  path:nth-child(1) {
    fill: ${colors.highlight} !important;
  }
`;

function Logo() {
    return (
        <StyledLogoSvg className="logo" />
    );
}

export default Logo;