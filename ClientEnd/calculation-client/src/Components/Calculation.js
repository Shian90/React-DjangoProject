import React, { Component } from "react";
import "../App.css";

import { calculate } from "../Controllers/controllers";

export class Calculation extends Component {
  constructor(props) {
    super(props);

    this.state = {
      inputNumber: "",
      result: "",
      errorMessage: "",
      error: false,
      loading: false,
    };
  }
  handleInputChange = (e) => {
    this.setState({ inputNumber: e.target.value });
  };

  handleClick = async (e) => {
    e.preventDefault();

    const type = e.target.id;
    this.setState({ loading: true });

    const requestBody = {
      type: type,
      value: this.state.inputNumber.toString(),
    };

    const res = await calculate(requestBody);
    this.setState({ loading: false });

    if (res.success) {
      this.setState({ result: res.result, error: false });
    } else {
      this.setState({ errorMessage: res.message, error: true });
    }
  };
  render() {
    return (
      <form>
        <div class="form-group overflow-padding">
          <p class="h2">Functionalities</p>

          <input
            type="text"
            class="form-control"
            id="input-number"
            placeholder="Enter a number"
            onChange={this.handleInputChange}
          />

          <div className="resultContainer">
            {this.state.error ? (
              <p class="text-danger">{this.state.errorMessage}</p>
            ) : this.state.result ? (
              <p class="text-success">The answer is : {this.state.result}</p>
            ) : (
              <></>
            )}
          </div>

          <div className="buttonsContainer">
            <div className="button">
              <button
                disabled={this.state.loading}
                type="submit"
                class="btn btn-outline-info"
                id="sq"
                onClick={this.handleClick}
              >
                Square
              </button>
            </div>
            <div className="button">
              <button
                disabled={this.state.loading}
                type="submit"
                class="btn btn-outline-info"
                id="sqrt"
                onClick={this.handleClick}
              >
                SquareRoot
              </button>
            </div>
            <div className="button">
              <button
                disabled={this.state.loading}
                type="submit"
                class="btn btn-outline-info"
                id="fact"
                onClick={this.handleClick}
              >
                Factorial
              </button>
            </div>
            <div className="button">
              <button
                disabled={this.state.loading}
                type="submit"
                class="btn btn-outline-info"
                id="fib"
                onClick={this.handleClick}
              >
                Fibonacci
              </button>
            </div>
          </div>
        </div>
      </form>
    );
  }
}
