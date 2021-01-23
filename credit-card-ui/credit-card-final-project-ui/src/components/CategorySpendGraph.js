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
          data: [65, 59, 80, 81, 56]
        }
      ]
    };
  }

  onClickUpdatePieChart = (e) => {
    console.log('hi');

    axios
      .get('/yearlyCategorySpend', this.state.datasets.data)
      .then((result) => {
        console.log(result)
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
