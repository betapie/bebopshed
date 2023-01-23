import React from "react";

import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import { Navbar as BootstrapNavbar } from "react-bootstrap";

import styled from "styled-components";

import { Link } from "react-router-dom";

import colors from "../style/ColorPalette";

const StyledNavbar = styled(BootstrapNavbar)`
  background-color: ${colors.accent};
  border-bottom: 2px solid ${colors.lightAccent};
  .navbar-brand {
    color: white;
  }
  .navbar-brand:hover {
    color: orange;
  }
  .nav-link {
    color: ${colors.text_deselected};
  }
  .nav-link:focus {
    color: white;
  }
  .nav-link:hover {
    color: orange;
  }
`;

function Navbar() {
  return (
    <StyledNavbar collapseOnSelect expand="lg">
      <Container>
        <BootstrapNavbar.Brand href="/">Bebopshed</BootstrapNavbar.Brand>
        <BootstrapNavbar.Toggle aria-controls="responsive-navbar-nav" />
        <BootstrapNavbar.Collapse id="responsive-navbar-nav">
          <Nav className="me-auto"></Nav>
          <Nav>
            <Nav.Link as={Link} to="/about">
              About
            </Nav.Link>
            <Nav.Link as={Link} to="/contribute">
              Contribute
            </Nav.Link>
          </Nav>
        </BootstrapNavbar.Collapse>
      </Container>
    </StyledNavbar>
  );
}

export default Navbar;
