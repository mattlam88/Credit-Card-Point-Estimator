import React from 'react';
import { VictoryLabel, VictoryPie } from 'victory';


export default class PieGraph extends React.Component {
    render() {
      return (
        <svg viewBox="0 0 1000 1000">
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
            style={{ fontSize: 10}}
            x={200} y={200}
            text="Yearly Category Spend"
          />
        </svg>
      );
    }
  }
