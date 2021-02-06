import React from 'react';
import axios from 'axios';
import { Card, Accordion, Button } from 'react-bootstrap'
import { Doughnut } from 'react-chartjs-2';

export default class PieGraph extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      username: this.props.usern,
      labels: ['Restaurant', 'Grocery', 'Non-Category', 'Utility', 'Gas'],
      datasets: [
        {
          label: 'Category Spend',
          backgroundColor: [
            '#2e4a62',
            '#456f93',
            '#6993b8',
            '#9bb7d0',
            '#cddbe7'
          ],
          hoverBackgroundColor: [
            '#2e4a62',
            '#456f93',
            '#6993b8',
            '#9bb7d0',
            '#cddbe7'
          ],
          data: [1, 1, 1, 1, 1]
        }
      ]
    };
  }

  onClickUpdatePieChart = (e) => {
    console.log(this.state);

    axios
      .get(`/yearlyCategorySpend/${this.props.username}`)
      .then((response) => {
        console.log(response)

        this.setState({
          datasets: [
            {
              label: 'Category Spend',
              backgroundColor: [
                '#2e4a62',
                '#456f93',
                '#6993b8',
                '#9bb7d0',
                '#cddbe7'
              ],
              hoverBackgroundColor: [
                '#2e4a62',
                '#456f93',
                '#6993b8',
                '#9bb7d0',
                '#cddbe7'
              ],
              data: [
                response.data.restaurant_spend,
                response.data.grocery_spend,
                response.data.non_category_spend,
                response.data.utility_spend,
                response.data.gas_spend
              ]
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
            <Accordion.Toggle as={Button} variant="link" eventKey="3" onClick={this.onClickUpdatePieChart.bind(this)}>
              Step 4. View Yearly Category Spend
          </Accordion.Toggle>
          </Card.Header>
          <Accordion.Collapse eventKey="3">
            <Card.Body>
              <Doughnut
                data={this.state}
                options={{
                  title: {
                    display: true,
                    text: 'Yearly Category Spend',
                    fontSize: 20
                  },
                  legend: {
                    display: true,
                    position: 'right'
                  }
                }}
              />
            </Card.Body>
          </Accordion.Collapse>
        </Card>
      </Accordion>
    );
  }
}
