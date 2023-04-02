import React from "react";
import styled from "styled-components";
import parse from "html-react-parser";
import {
  MainWrapper,
  MainContent,
  Panel,
  PanelHeading,
  ErrorDiv,
} from "./MainComponents";
import colors from "../style/ColorPalette";
import ProcessingMenu from "./ProcessingMenu";
import Spinner from "./Spinner";
import { DefaultButton } from "./Buttons";

const LineGraphic = styled.div`
  svg {
    width: 100%;
    max-width: 100%;
    height: 100%;
    border: 2px solid ${colors.text};
    border-radius: 5px;
    background-color: ${colors.text};
    color: ${colors.accent};
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
  error: null,
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
    console.log("executing fetch line query at url '" + url + "'");
    this.setState((state) => DEFAULT_STATE);
    fetch(url)
      .then((response) => {
        if (!response.ok) {
          throw Error(response.statusText);
        }
        return response.json();
      })
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
      })
      .catch((error) => {
        console.log(error);
        this.setState({
          error: error,
        });
      });
  }

  componentDidMount() {
    this.executeLineFetch("/api/generate");
  }

  chopsBuilder(startKeyBasePitch, startKeyAccidental, deltaKey) {
    let queryParams = {
      id: this.state.line.id,
      key_basepitch: startKeyBasePitch,
      key_accidental: startKeyAccidental,
      delta_key: deltaKey,
    };
    this.executeLineFetch("/api/chops_builder", queryParams);
  }

  render() {
    let heading = "Tuning Instruments...";
    if (this.state.line.lineRender) {
      heading = `#${this.state.line.id}: ${this.state.line.progName}`;
    }

    const line_view = this.state.line.lineRender ? (
      parse(this.state.line.lineRender)
    ) : this.state.error ? (
      <ErrorDiv>
        Seems like an error occured! <br />
        Someone must have tripped over the drum set.
        <br />
        We are sorry for that.
        <br />
        Why don't you try another line?
      </ErrorDiv>
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
            <DefaultButton
              id="btn-generate"
              onClick={() => this.executeLineFetch("/api/generate")}
            >
              Give me another one!
            </DefaultButton>
          </Panel>
        </MainContent>
      </MainWrapper>
    );
  }
}
