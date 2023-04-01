import React from "react";
import Collapse from "react-bootstrap/Collapse";
import { ToggleButton } from "./Buttons";
import ChopsBuilderMenu from "./ChopsBuilderMenu";
import TransposeMenu from "./TransposeMenu";

const toggleButtons = [
  {
    id: "transpose",
    caption: "Transpose",
  },
  {
    id: "chopsBuilder",
    caption: "Chops Builder",
  },
];

export default class ProcessingMenu extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      open: null,
      basePitch: props.keyBasePitch,
      accidental: props.keyAccidental,
    };
    this.executeLineFetch = props.executeLineFetch;
    this.setBasePitch = this.setBasePitch.bind(this);
    this.setAccidental = this.setAccidental.bind(this);
  }

  toggleOpen(element) {
    this.setState((prev_state) => ({
      open: prev_state.open == element ? null : element,
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
      <div style={{ textAlign: "left" }}>
        {toggleButtons.map((btn) => (
          <ToggleButton
            variant="outline-primary"
            size="sm"
            onClick={() => {
              this.toggleOpen(btn.id);
            }}
            key={btn.id}
            aria-controls="selection-group"
            aria-expanded={this.state.open == btn.id}
            type="checkbox"
            checked={this.state.open == btn.id}
          >
            {btn.caption}
          </ToggleButton>
        ))}
        <Collapse in={this.state.open == "transpose"}>
          <div>
            <TransposeMenu
              id="selection-group"
              lineId={this.props.lineId}
              basePitch={this.state.basePitch}
              accidental={this.state.accidental}
              executeLineFetch={this.props.executeLineFetch}
            ></TransposeMenu>
          </div>
        </Collapse>
        <Collapse in={this.state.open == "chopsBuilder"}>
          <div>
            <ChopsBuilderMenu
              id="selection-group"
              lineId={this.props.lineId}
              basePitch={this.state.basePitch}
              accidental={this.state.accidental}
              executeLineFetch={this.props.executeLineFetch}
            ></ChopsBuilderMenu>
          </div>
        </Collapse>
      </div>
    );
  }
}
