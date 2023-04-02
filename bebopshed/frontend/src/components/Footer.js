import React from "react";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import { Navbar as BootstrapNavbar } from "react-bootstrap";
import styled from "styled-components";
import { Link } from "react-router-dom";
import colors from "../style/ColorPalette";

const StyledNavbar = styled(BootstrapNavbar)`
  background-color: ${colors.accent};
  border-top: 2px solid ${colors.lightAccent};
  height: 40px;
  .navbar-brand {
    color: white;
  }
  .nav-link {
    color: ${colors.text_deselected};
    max-height: 30px;
    padding: 0px;
    font-size: small;
  }
  .nav-link:focus {
    color: white;
  }
  .nav-link:hover {
    color: orange;
    text-decoration: solid underline orange 3px;
  }
`;

function Footer() {
  return (
    <StyledNavbar variant="dark" expand="sm">
      <Container style={{ maxHeight: "30px" }}>
        <Nav>
          <Nav.Link as={Link} to="/legal_notice">
            Legal Notice
          </Nav.Link>
        </Nav>
      </Container>
    </StyledNavbar>
  );
}

export default Footer;
