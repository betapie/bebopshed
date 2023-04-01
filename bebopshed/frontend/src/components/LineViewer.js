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
import ProcessingMenu from "./ProcessingMenu";
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

  executeLineFetch(endpoint, queryParams) {
    let url = endpoint;
    if (queryParams) {
      url += "?" + new URLSearchParams(queryParams).toString();
    }
    console.log("executing fetch line query at url \'" + url + "\'")
    this.setState((state) => DEFAULT_STATE);
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
          keyAccidental: data.key_accidental,
        });
      });
  }

  componentDidMount() {
    this.fetchLine();
  }

  fetchLine() {
    this.executeLineFetch("/api/generate")
  }

  chopsBuilder(startKeyBasePitch, startKeyAccidental, deltaKey) {
    let queryParams = {
      id: this.state.line.id,
      key_basepitch: startKeyBasePitch,
      key_accidental: startKeyAccidental,
      delta_key: deltaKey
    };
    this.executeLineFetch("/api/chops_builder", queryParams)
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
                <ProcessingMenu
                  lineId={this.state.line.id}
                  keyBasePitch={this.state.keyBasepitch}
                  keyAccidental={this.state.keyAccidental}
                  executeLineFetch={(endpoint, queryParams) =>
                    this.executeLineFetch(endpoint, queryParams)
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
