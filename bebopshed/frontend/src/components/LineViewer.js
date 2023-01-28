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
import Spinner from "./Spinner";

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
  line: "",
  artist: "",
  song: "",
  year: "",
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
          line: data.line,
          artist: data.artist,
          song: data.song,
          year: data.year,
        });
      });
  }

  render() {
    let info = this.state.artist;
    if (this.state.song) {
      info += " on " + this.state.song;
    }
    if (this.state.year) {
      info += " (" + this.state.year + ")";
    }

    const line = this.state.line ? parse(this.state.line) : <Spinner />;

    return (
      <MainWrapper>
        <MainContent>
          <Panel>
            <PanelHeading>{info}</PanelHeading>
            <LineGraphic id="line-graphic">{line}</LineGraphic>
            <Button id="btn-generate" onClick={() => this.fetchLine()}>
              Give me another one!
            </Button>
          </Panel>
        </MainContent>
      </MainWrapper>
    );
  }
}
