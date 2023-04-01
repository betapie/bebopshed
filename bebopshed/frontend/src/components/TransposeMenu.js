import React from "react";
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

export default class TransposeMenu extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      basePitch: props.basePitch,
      accidental: props.accidental,
    };
    this.executeLineFetch = props.executeLineFetch;
    this.setBasePitch = this.setBasePitch.bind(this);
    this.setAccidental = this.setAccidental.bind(this);
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

  onBtnClicked() {
    let queryParams = {
      id: this.props.lineId,
      key_basepitch: this.state.basePitch,
      key_accidental: this.state.accidental,
    };
    this.executeLineFetch("/api/generate", queryParams);
  }

  render() {
    return (
      <div>
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
            <DefaultButton onClick={() => this.onBtnClicked()}>
              Do it!
            </DefaultButton>
          </SelectionElement>
        </SelectionDiv>
      </div>
    );
  }
}
