import React from 'react';
import { VictoryLabel, VictoryBar, VictoryLine, VictoryChart } from 'victory';


export default class LineBarGraph extends React.Component {
    render() {
    return (
        <svg>
        <VictoryChart domain={{ x: [0, 4] }}>
            <VictoryBar
                style={{ data: { fill: "red" } }}
                data={[{ x: 1, y: 2 }, { x: 2, y: 4 }, { x: 3, y: 6 }]}
            />
            <VictoryLine
                style={{ data: { stroke: "blue", strokeWidth: 5 } }}
                y={(d) => d.x}
            />
        </VictoryChart>
        </svg>
      )
    }
}
