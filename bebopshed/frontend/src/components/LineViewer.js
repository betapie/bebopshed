import React from "react";
import styled from "styled-components";
import parse from "html-react-parser";
import { Button } from "react-bootstrap";
import {
  MainWrapper,
  MainContent,
  Panel,
  PanelHeading,
} from "./MainComponents";
import KeySelector from "./KeySelector";
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
    line_id: null,
    line_render: "",
    prog_sequence: "",
    prog_name: ""
  },
  selected_key: null,
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
            line_render: data.line,
            prog_sequence: data.prog_sequence,
            prog_name: data.prog_name
          },
          selected_key: data.key,
        });
      });
  }

  key_selected(key_str) {
    this.setState((state) => DEFAULT_STATE);

    let url =
      "/api/generate?" +
      new URLSearchParams({
        id: this.state.line.id,
        key: key_str,
      }).toString();

    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          line: {
            id: data.id,
            line_render: data.line,
            prog_sequence: data.prog_sequence,
            prog_name: data.prog_name
          },
          selected_key: data.key,
        });
      });
  }

  render() {
    let heading = "Tuning Instruments..."
    if (this.state.line.line_render) {
      heading = `#${this.state.line.id}: ${this.state.line.prog_name}`;
    }

    const line_view = this.state.line.line_render ? (
      parse(this.state.line.line_render)
    ) : (
      <Spinner />
    );

    return (
      <MainWrapper>
        <MainContent>
          <Panel>
            <PanelHeading>{heading}</PanelHeading>
            {this.state.selected_key && (
              <KeySelector
                selected_key={this.state.selected_key}
                onSelect={(key) => this.key_selected(key)}
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
