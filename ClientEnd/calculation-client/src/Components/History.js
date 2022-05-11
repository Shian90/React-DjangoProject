import React, { Component } from "react";
import "../App.css";

import { getHistory } from "../Controllers/controllers";

export class History extends Component {
  constructor(props) {
    super(props);

    this.state = {
      inputNumber: "",
      history: [],
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

    this.setState({ loading: true });
    const requestBody = {
      n: this.state.inputNumber.toString(),
    };

    const res = await getHistory(requestBody);
    this.setState({ loading: false });

    if (res.success) {
      this.setState({ history: res.result, error: false });
    } else {
      this.setState({ errorMessage: res.message, error: true });
    }
  };
  render() {
    return (
      <>
        <form class="form-inline">
          <div class="form-group mx-sm-3 mb-2">
            <p class="h2">History</p>

            <input
              type="text"
              class="form-control"
              placeholder="Enter number or leave blank"
              onChange={this.handleInputChange}
            />
          </div>

          <div className="resultContainer">
            {this.state.error ? (
              <p class="text-danger">{this.state.errorMessage}</p>
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
                onClick={this.handleClick}
              >
                Show History
              </button>
            </div>
          </div>
        </form>

        {this.state.history.length > 0 && !this.state.error ? (
          <table class="table">
            <thead>
              <tr>
                <th scope="col">Serial</th>
                <th scope="col">Value</th>
                <th scope="col">Answer</th>
                <th scope="col">Operation</th>
              </tr>
            </thead>
            <tbody>
              {this.state.history.map((history, i) => (
                <tr>
                  <td>{i + 1}</td>
                  <td>{history.value}</td>
                  <td>{history.output}</td>
                  <td>{history.type}</td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <></>
        )}
      </>
    );
  }
}
