import React from "react";
import parse from "html-react-parser";
import Spinner from "./Spinner";

const DEFAULT_STATE = {
  line: "",
  artist: "",
  song: "",
  year: "",
};

export default class App extends React.Component {
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
      <div className="panel">
        <div className="line-info">{info}</div>
        <div id="line-graphic">{line}</div>
        <button id="btn-generate" onClick={() => this.fetchLine()}>
          Give me another one!
        </button>
      </div>
    );
  }
}
