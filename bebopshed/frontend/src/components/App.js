import React from "react";
import parse from "html-react-parser";

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      line: "<p>missing</p>",
    };
  }

  componentDidMount() {
    fetch("/api/generate")
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          line: data.line,
          artist: data.artist,
          song: data.song,
          year: data.year
        });
      });
  }

  render() {
    let info = this.state.artist;
    if (this.state.song) {
      info += " on " + this.state.song;
    }
    if (this.state.year) {
      info += " (" + this.state.year + ")"
    }

    return (
      <div className="panel">
        <div className="line-info">{info}</div>
        <div id="line-graphic">{parse(this.state.line)}</div>
        <div id="btn-generate">Give me another one!</div>
      </div>
    );
  }
}
