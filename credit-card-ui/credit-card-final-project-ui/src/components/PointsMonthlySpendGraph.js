import React from 'react';
import { Card, Accordion, Button } from 'react-bootstrap'
import { VictoryChart, VictoryBar, VictoryGroup, VictoryStack } from 'victory';

export default class BarGraph extends React.Component {
    render() {

        const getBarData = () => {
            return [1, 2, 3, 4, 5].map(() => {
                return [
                    { x: 1, y: Math.random() },
                    { x: 2, y: Math.random() },
                    { x: 3, y: Math.random() }
                ];
            });
        };

        return (
            <Accordion defaultActiveKey="0">
                <Card>
                    <Card.Header>
                        <Accordion.Toggle as={Button} variant="link" eventKey="4">
                            Step 5. View Estimated Points Accumulated
                        </Accordion.Toggle>
                    </Card.Header>
                    <Accordion.Collapse eventKey="4">
                        <Card.Body>
                            <div>
                                <VictoryChart domainPadding={{ x: 50 }} width={400} height={400}>
                                    <VictoryGroup offset={20} style={{ data: { width: 15 } }}>
                                        <VictoryStack colorScale={"red"}>
                                            {getBarData().map((data, index) => {
                                                return <VictoryBar key={index} data={data} />;
                                            })}
                                        </VictoryStack>
                                        <VictoryStack colorScale={"green"}>
                                            {getBarData().map((data, index) => {
                                                return <VictoryBar key={index} data={data} />;
                                            })}
                                        </VictoryStack>
                                        <VictoryStack colorScale={"blue"}>
                                            {getBarData().map((data, index) => {
                                                return <VictoryBar key={index} data={data} />;
                                            })}
                                        </VictoryStack>
                                    </VictoryGroup>
                                </VictoryChart>
                            </div>
                        </Card.Body>
                    </Accordion.Collapse>
                </Card>
            </Accordion>
        );
    }
}
