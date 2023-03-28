import React from "react";
import Collapse from "react-bootstrap/Collapse";
import styled from "styled-components";
import colors from "../style/ColorPalette";
import { ToggleButton, DefaultButton } from "./Buttons";
import { ButtonGroup } from "react-bootstrap";

const basePitches = ["c", "d", "e", "f", "g", "a", "b"];
const accidentals = ["flat", "natural", "sharp"];
const accidentalSymbols = [">", "\u266e", "<"];

const KeyText = styled.div`
  font-family: lilyjazz-chord;
  display: inline;
`;

const SelectionDiv = styled.div`
  border: 2px solid ${colors.lightAccent};
  border-radius: 5px;
  width: 240px;
  padding: 2px;
`;

const SelectionElement = styled.div`
  padding: 5px;
`;

export default class KeySelector2 extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      open: false,
      basePitch: props.keyBasePitch,
      accidental: props.keyAccidental,
    };
    this.onClickedTranspose = props.onClickedTranspose;
    this.setBasePitch = this.setBasePitch.bind(this);
    this.setAccidental = this.setAccidental.bind(this);
  }

  toggleOpen() {
    this.setState((prev_state) => ({
      open: !prev_state.open,
    }));
  }

  setBasePitch(basePitch) {
    this.setState(() => ({
      basePitch: basePitch,
    }));
  }

  setAccidental(accidental) {
    this.setState(() => ({
      accidental: accidental,
    }));
  }

  render() {
    return (
      <div style={{ textAlign: "left" }}>
        <ToggleButton
          variant="outline-primary"
          size="sm"
          onClick={() => {
            this.toggleOpen();
          }}
          aria-controls="selection-group"
          aria-expanded={this.state.open}
          type="checkbox"
          checked={this.state.open}
        >
          Transpose
        </ToggleButton>
        <Collapse in={this.state.open}>
          <SelectionDiv id="selection-group">
            <SelectionElement>
              <ButtonGroup>
                {basePitches.map((basePitch, idx) => (
                  <ToggleButton
                    key={idx}
                    id={`basePitchRadio-${idx}`}
                    type="radio"
                    variant="outline-primary"
                    name="basePitchRadio"
                    value={basePitch}
                    checked={this.state.basePitch === basePitch}
                    onChange={(e) => this.setBasePitch(e.currentTarget.value)}
                  >
                    {basePitch}
                  </ToggleButton>
                ))}
              </ButtonGroup>
            </SelectionElement>
            <SelectionElement>
              <ButtonGroup>
                {accidentals.map((accidental, idx) => (
                  <ToggleButton
                    key={idx}
                    id={`accidentalRadio-${idx}`}
                    type="radio"
                    variant="outline-primary"
                    name="accidentalRadio"
                    value={accidental}
                    checked={this.state.accidental === accidental}
                    onChange={(e) => this.setAccidental(e.currentTarget.value)}
                  >
                    <KeyText>{accidentalSymbols[idx]}</KeyText>
                  </ToggleButton>
                ))}
              </ButtonGroup>
            </SelectionElement>
            <SelectionElement>
              <DefaultButton
                onClick={() =>
                  this.onClickedTranspose(
                    this.state.basePitch,
                    this.state.accidental
                  )
                }
              >
                Do it!
              </DefaultButton>
            </SelectionElement>
          </SelectionDiv>
        </Collapse>
      </div>
    );
  }
}
