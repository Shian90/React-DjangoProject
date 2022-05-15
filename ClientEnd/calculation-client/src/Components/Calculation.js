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
      <div className="container">
        <form>
          <div className="form-group overflow-padding">
            <p className="h3">Functionalities</p>

            <input
              type="text"
              className="form-control"
              id="input-number"
              placeholder="Enter a number"
              onChange={this.handleInputChange}
            />

            {this.state.error ? (
              <p className="text-danger d-flex justify-content-center text-justify text-wrap">
                {this.state.errorMessage}
              </p>
            ) : this.state.result ? (
              <p className="text-success text-justify text-wrap">
                The answer is : {this.state.result}
              </p>
            ) : (
              <></>
            )}

            <div className="container d-flex justify-content-center">
              <button
                disabled={this.state.loading}
                type="submit"
                className="btn btn-outline-info button"
                id="sq"
                onClick={this.handleClick}
              >
                Square
              </button>
              <button
                disabled={this.state.loading}
                type="submit"
                className="btn btn-outline-info button"
                id="sqrt"
                onClick={this.handleClick}
              >
                SquareRoot
              </button>
              <button
                disabled={this.state.loading}
                type="submit"
                className="btn btn-outline-info button"
                id="fact"
                onClick={this.handleClick}
              >
                Factorial
              </button>
              <button
                disabled={this.state.loading}
                type="submit"
                className="btn btn-outline-info button"
                id="fib"
                onClick={this.handleClick}
              >
                Fibonacci
              </button>
            </div>
          </div>
        </form>
      </div>
    );
  }
}
