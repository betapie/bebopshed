import React from "react";
import { MainWrapper, MainContent, Panel, TextDiv } from "./MainComponents";
import { ExternalLink } from "./Links";
//import SubmitLineForm from "./SubmitLineForm";

const Contribute = () => {
  return (
    <MainWrapper>
      <MainContent>
        <Panel>
          <TextDiv>
            <h3>Interested in contributing? That's awesome!</h3>
            <p>
              Do you have cool bebop licks or lines you want to add? Do you have
              ideas for features? Do you want to contribute to development? In
              any case I'd love to hear from you.
            </p>
            <p>
              The whole thing is public on &nbsp;
              <ExternalLink href="https://github.com/betapie/bebopshed">
                Github
              </ExternalLink>
              . Check it out. Please get in touch there for the time being.
            </p>
            <p>
              Happy sheddin',
              <br /> Manu
            </p>
          </TextDiv>
        </Panel>
      </MainContent>
    </MainWrapper>
  );
};

export default Contribute;
