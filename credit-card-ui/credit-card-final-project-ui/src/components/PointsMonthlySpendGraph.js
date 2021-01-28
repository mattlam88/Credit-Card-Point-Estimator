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
                    label: "Total Month Spend ($)",
                    data: [33, 53, 85, 41, 44, 65, 10, 10, 10, 10, 20, 20],
                    fill: false,
                    borderColor: "#9bb7d0"
                },
                {
                    label: "Credit Card Points",
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
          .get('/combinedSpendAndPoints')
          .then((response) => {
            console.log(response)
    
            this.setState({
                datasets: [
                    {
                        label: "Total Month Spend",
                        data: [
                            response.data.user_spend.January.monthly_spend,
                            response.data.user_spend.February.monthly_spend,
                            response.data.user_spend.March.monthly_spend,
                            response.data.user_spend.April.monthly_spend,
                            response.data.user_spend.May.monthly_spend,
                            response.data.user_spend.June.monthly_spend,
                            response.data.user_spend.July.monthly_spend,
                            response.data.user_spend.August.monthly_spend,
                            response.data.user_spend.September.monthly_spend,
                            response.data.user_spend.October.monthly_spend,
                            response.data.user_spend.November.monthly_spend,
                            response.data.user_spend.December.monthly_spend
                        ],
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