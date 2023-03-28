import React from "react";
import styled from "styled-components";
import parse from "html-react-parser";
import {
  MainWrapper,
  MainContent,
  Panel,
  PanelHeading,
} from "./MainComponents";
// import KeySelector from "./KeySelector";
import KeySelector2 from "./KeySelector2";
import Spinner from "./Spinner";
import { DefaultButton } from "./Buttons";

const LineGraphic = styled.div`
  svg {
    width: 100%;
    max-width: 100%;
    height: 100%;
    border: 2px solid var(--txt-color);
    border-radius: 5px;
    background-color: var(--txt-color);
    margin-top: 20px;
    margin-bottom: 20px;
  }
`;

const DEFAULT_STATE = {
  line: {
    id: null,
    lineRender: "",
    progSequence: "",
    progName: "",
  },
  keyBasepitch: null,
  keyAccidental: null,
};

export default class LineViewer extends React.Component {
  constructor(props) {
    super(props);
    this.state = DEFAULT_STATE;
  }

  componentDidMount() {
    this.fetchLine();
  }

  fetchLine() {
    console.log("fetching new line...");
    this.setState((state) => DEFAULT_STATE);
    fetch("/api/generate")
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          line: {
            id: data.id,
            lineRender: data.line,
            progSequence: data.prog_sequence,
            progName: data.prog_name,
          },
          keyBasepitch: data.key_basepitch,
          keyAccidental: data.key_accidental,
        });
      });
  }

  transpose(keyBasePitch, keyAccidental) {
    this.setState((state) => DEFAULT_STATE);

    let url =
      "/api/generate?" +
      new URLSearchParams({
        id: this.state.line.id,
        key_basepitch: keyBasePitch,
        key_accidental: keyAccidental
      }).toString();

    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          line: {
            id: data.id,
            lineRender: data.line,
            progSequence: data.prog_sequence,
            progName: data.prog_name,
          },
          keyBasepitch: data.key_basepitch,
          keyAccidental: data.key_accidental
        });
      });
  }

  render() {
    let heading = "Tuning Instruments...";
    if (this.state.line.lineRender) {
      heading = `#${this.state.line.id}: ${this.state.line.progName}`;
    }

    const line_view = this.state.line.lineRender ? (
      parse(this.state.line.lineRender)
    ) : (
      <Spinner />
    );

    return (
      <MainWrapper>
        <MainContent>
          <Panel>
            <PanelHeading>{heading}</PanelHeading>
            {this.state.keyBasepitch && (
                <KeySelector2
                  keyBasePitch={this.state.keyBasepitch}
                  keyAccidental={this.state.keyAccidental}
                  onClickedTranspose={(basePitch, accidental) =>
                    this.transpose(basePitch, accidental)
                  }
                />
              )}
            <LineGraphic id="line-graphic">{line_view}</LineGraphic>
            <DefaultButton id="btn-generate" onClick={() => this.fetchLine()}>
              Give me another one!
            </DefaultButton>
          </Panel>
        </MainContent>
      </MainWrapper>
    );
  }
}
