import React from "react";
import Collapse from "react-bootstrap/Collapse";
import styled from "styled-components";
import colors from "../style/ColorPalette";
import { ToggleButton } from "./Buttons";

const KeysList = [
  "c",
  "cis",
  "des",
  "d",
  "dis",
  "es",
  "e",
  "f",
  "fis",
  "ges",
  "g",
  "gis",
  "as",
  "a",
  "bes",
  "b",
];

const KeyText = styled.div`
  font-family: lilyjazz-chord;
  display: inline;
`;

const SelectionDiv = styled.div`
  border: 2px solid ${colors.lightAccent};
  border-radius: 5px;
  @media (max-width: 768px) {
    display: grid;
    grid-template-columns: repeat(auto-fill, 30px);
  }
  padding: 2px;
`;

const SelectionBtn = styled(ToggleButton)`
  --bs-btn-border-color: transparent;
  //flex-grow: 1;
`;

export default class KeySelector extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      open: false,
      selected_key: props.selected_key,
    };
    this.onSelect = props.onSelect;
  }

  toggle_open() {
    this.setState((prev_state) => ({
      open: !prev_state.open,
    }));
  }

  to_display_key(key_txt) {
    let display_key = key_txt.charAt(0).toUpperCase();
    if (key_txt.length > 1) {
      if (key_txt.charAt(1) == "i") {
        display_key += "<";
      } else {
        display_key += ">";
      }
    }
    return display_key;
  }

  render() {
    let display_key = this.to_display_key(this.state.selected_key);

    return (
      <div style={{ textAlign: "left" }}>
        <ToggleButton
          variant="outline-primary"
          size="sm"
          onClick={() => {
            this.toggle_open();
          }}
          aria-controls="selection-group"
          aria-expanded={this.state.open}
          type="checkbox"
          checked={this.state.open}
        >
          Key of <KeyText>{display_key}</KeyText>
        </ToggleButton>
        <Collapse in={this.state.open}>
          <SelectionDiv id="selection-group">
            {KeysList.map((key_txt, idx) => (
              <SelectionBtn
                key={idx}
                onClick={() => this.onSelect(key_txt)}
                variant="outline-primary"
                size="sm"
                type="checkbox"
                checked={this.state.selected_key === key_txt}
              >
                <KeyText>{this.to_display_key(key_txt)}</KeyText>
              </SelectionBtn>
            ))}
          </SelectionDiv>
        </Collapse>
      </div>
    );
  }
}
