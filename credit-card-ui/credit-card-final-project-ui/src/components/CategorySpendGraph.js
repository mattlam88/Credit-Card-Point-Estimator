import React from 'react';
import axios from 'axios';
import { Card, Accordion, Button } from 'react-bootstrap'
import { VictoryLabel, VictoryPie } from 'victory';


export default class PieGraph extends React.Component {
  render() {
    return (
      <Accordion defaultActiveKey="0">
        <Card>
          <Card.Header>
            <Accordion.Toggle as={Button} variant="link" eventKey="3">
              Step 4. View Yearly Category Spend
          </Accordion.Toggle>
          </Card.Header>
          <Accordion.Collapse eventKey="3">
            <Card.Body>
              <svg viewBox="0 0 400 400">
                <VictoryPie
                  standalone={false}
                  width={400} height={400}
                  data={[
                    { x: 1, y: 120 }, { x: 2, y: 150 }, { x: 3, y: 75 }
                  ]}
                  innerRadius={68} labelRadius={100}
                  style={{ labels: { fontSize: 20, fill: "white" } }}
                />
                <VictoryLabel
                  textAnchor="middle"
                  style={{ fontSize: 10 }}
                  x={200} y={200}
                  text="Yearly Category Spend"
                />
              </svg>
            </Card.Body>
          </Accordion.Collapse>
        </Card>
      </Accordion>
    );
  }
}
