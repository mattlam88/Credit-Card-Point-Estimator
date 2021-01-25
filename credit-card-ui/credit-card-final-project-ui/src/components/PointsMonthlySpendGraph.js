import React, { Component } from 'react';
import axios from 'axios';
import { Accordion, Card, Button } from 'react-bootstrap'

import { Line } from "react-chartjs-2";

export default class LineGraph extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
            datasets: [
                {
                    label: "Total Month Spend",
                    data: [33, 53, 85, 41, 44, 65, 10, 10, 10, 10, 20, 20],
                    fill: false,
                    borderColor: "#9bb7d0"
                },
                {
                    label: "Second dataset",
                    data: [33, 25, 35, 51, 54, 76, 10, 10, 10, 10, 20, 20],
                    fill: false,
                    borderColor: "#456f93"
                }
            ]
        };
    }

    onClickUpdateLineChart = (e) => {
        console.log(this.state);
    
        axios
          .get('/yearlySpendAndPoints')
          .then((response) => {
            console.log(response)
    
            this.setState({
                datasets: [
                    {
                        label: "Total Month Spend",
                        data: [33, 53, 85, 41, 44, 65, 10, 10, 10, 10, 20, 20],
                        fill: false,
                        borderColor: "#9bb7d0"
                    },
                    {
                        label: "Second dataset",
                        data: [33, 25, 35, 51, 54, 76, 10, 10, 10, 10, 20, 20],
                        fill: false,
                        borderColor: "#456f93"
                    }
                ]});
            console.log(this.state)
          })
          .catch(error => {
            console.log(error)
          });
      }

    render() {
        return (
            <Accordion defaultActiveKey="0">
                <Card>
                    <Card.Header>
                        <Accordion.Toggle as={Button} variant="link" eventKey="3" onClick={this.onClickUpdateLineChart.bind(this)}>
                            Step 5. View Yearly Spend & Point Accumulation
                        </Accordion.Toggle>
                    </Card.Header>
                    <Accordion.Collapse eventKey="3">
                        <Card.Body>
                            <Line data={this.state} />
                        </Card.Body>
                    </Accordion.Collapse>
                </Card>
            </Accordion>
        )
    }
}