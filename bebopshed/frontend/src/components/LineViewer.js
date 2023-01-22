import React from "react";
import styled from "styled-components";
import parse from "html-react-parser";
import { Button } from "react-bootstrap";
import colors from "../style/ColorPalette";
import Spinner from "./Spinner";

const Panel = styled.div`
  background-color: ${colors.accent};
  border-radius: 10px;
  padding: 50px 40px;
  border: 2px solid ${colors.lightAccent};
  width: 100%;
  justify-content: center;
  align-items: center;
  text-align: center;
`;

const PanelHeading = styled.div`
  color: var(--txt-color);
  font-size: larger;
  font-weight: bold;
`;

const MainWrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 50px);
`;

const MainContent = styled.div`
  width: 100%;
  max-width: 1000px;
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
            <div id="line-graphic">{line}</div>
            <Button id="btn-generate" onClick={() => this.fetchLine()}>
              Give me another one!
            </Button>
          </Panel>
        </MainContent>
      </MainWrapper>
    );
  }
}
