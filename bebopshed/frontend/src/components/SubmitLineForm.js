import React from "react";

export default class SubmitLineForm extends React.Component {
  constructor(props) {
    super(props);
  }

  submitLine() {}

  renderLine() {}

  render() {
    return (
      <div>
        <p>Some Text Here</p>
        <p>Choose a progression</p>
        <p>Choose a key</p>
        <p>This is where the rendered line will be shown</p>
        <form>
          <input></input>
        </form>
      </div>
    );
  }
}
