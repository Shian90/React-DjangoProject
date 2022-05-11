import React, { Component } from "react";
import "./App.css";

import { Calculation } from "./Components/Calculation";
import { History } from "./Components/History";

export class Home extends Component {
  render() {
    return (
      <div class="overflow-auto overflow-padding">
        <Calculation />
        <History />
      </div>
    );
  }
}
