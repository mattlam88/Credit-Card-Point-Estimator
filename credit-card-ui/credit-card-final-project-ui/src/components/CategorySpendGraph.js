import React from 'react';
import axios from 'axios';
import { Card, Accordion, Button } from 'react-bootstrap'
import { Doughnut } from 'react-chartjs-2';

// Will need to add components logic here where the setState is updated, google online for this



export default class PieGraph extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
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
    console.log('hi');

    axios
      .get('/yearlyCategorySpend')
      .then((year_spend_data) => {
        this.setState({
          data: [
            year_spend_data.restaurant_spend,
            year_spend_data.grocery_spend,
            year_spend_data.non_category_spend,
            year_spend_data.utility_spend,
            year_spend_data.gas_spend
          ]
        })
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
            <Accordion.Toggle as={Button} variant="link" eventKey="3" onClick={this.onClickUpdatePieChart}>
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
