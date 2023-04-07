import React from "react";
import styled from "styled-components";
import colors from "../style/ColorPalette";
import { ToggleButton, DefaultButton } from "./Buttons";
import { ButtonGroup } from "react-bootstrap";
import { TextDiv } from "./TextComponents";

const basePitches = ["c", "d", "e", "f", "g", "a", "b"];
const accidentals = ["flat", "natural", "sharp"];
const accidentalSymbols = [">", "\u266e", "<"];
const intervals = ["1", "2", "3", "4", "5", "6"];
const directions = ["descending", "ascending"]

const KeyText = styled.div`
  font-family: lilyjazz-chord;
  display: inline;
`;

const SelectionDiv = styled.div`
  border: 2px solid ${colors.lightAccent};
  border-radius: 5px;
  width: 250px;
  padding: 2px;
`;

const SelectionElement = styled.div`
  padding: 5px;
`;

export default class ChopsBuilderMenu extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      interval: "2",
      direction: "descending",
      basePitch: props.basePitch,
      accidental: props.accidental,
    };
    this.executeLineFetch = props.executeLineFetch;
    this.setInterval = this.setInterval.bind(this);
    this.setBasePitch = this.setBasePitch.bind(this);
    this.setAccidental = this.setAccidental.bind(this);
  }

  setInterval(interval) {
    this.setState(() => ({
        interval: interval,
    }))
  }

  setDirection(direction) {
    this.setState(() => ({
        direction: direction,
    }))
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
    let delta_key = Number(this.state.interval)
    if (this.state.direction == "descending") {
        delta_key = -delta_key
    }
    let queryParams = {
      id: this.props.lineId,
      key_basepitch: this.state.basePitch,
      key_accidental: this.state.accidental,
      delta_key: delta_key.toString()
    };
    this.executeLineFetch("/api/chops_builder", queryParams);
  }

  render() {
    return (
      <div>
        <SelectionDiv id="selection-group">
          <TextDiv>
            Number of Semitones
          </TextDiv>
          <SelectionElement>
            <ButtonGroup>
              {intervals.map((interval) => (
                <ToggleButton
                  key={interval}
                  id={`intervalRadio-${interval}`}
                  type="radio"
                  variant="outline-primary"
                  name="intervalRadio"
                  value={interval}
                  checked={this.state.interval === interval}
                  onChange={(e) => this.setInterval(e.currentTarget.value)}
                >
                  {interval}
                </ToggleButton>
              ))}
            </ButtonGroup>
          </SelectionElement>
          <SelectionElement>
            <ButtonGroup>
              {directions.map((direction) => (
                <ToggleButton
                  key={direction}
                  id={`directionRadio-${direction}`}
                  type="radio"
                  variant="outline-primary"
                  name="directionRadio"
                  value={direction}
                  checked={this.state.direction === direction}
                  onChange={(e) => this.setDirection(e.currentTarget.value)}
                >
                  {direction}
                </ToggleButton>
              ))}
            </ButtonGroup>
          </SelectionElement>
          <TextDiv>
            Starting from Key
          </TextDiv>
          <SelectionElement>
            <ButtonGroup>
              {basePitches.map((basePitch, idx) => (
                <ToggleButton
                  key={idx}
                  id={`startBasePitchRadio-${idx}`}
                  type="radio"
                  variant="outline-primary"
                  name="startBasePitchRadio"
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
                  id={`startAccidentalRadio-${idx}`}
                  type="radio"
                  variant="outline-primary"
                  name="startAccidentalRadio"
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
