import React from 'react';
import ReactDOM from 'react-dom';
import { VictoryBar, VictoryChart, VictoryAxis } from 'victory';

class Main extends React.Component {
  render() {
    return (
      <div>
        <h1>Victory Tutorial</h1>
      </div>
    );
  }
}
const data = [
  {quarter: 1, earnings: 13000},
  {quarter: 2, earnings: 16500},
  {quarter: 3, earnings: 14250},
  {quarter: 4, earnings: 19000}
];


class App extends React.Component {
  render() {
    return (
      <VictoryChart
        // domainPadding will add space to each side of VictoryBar to
        // prevent it from overlapping the axis
        domainPadding={20}
      >
        <VictoryAxis
          // tickValues specifies both the number of ticks and where
          // they are placed on the axis
          tickValues={[1, 2, 3, 4]}
          tickFormat={["Quarter 1", "Quarter 2", "Quarter 3", "Quarter 4"]}
        />
        <VictoryAxis
          dependentAxis
          // tickFormat specifies how ticks should be displayed
          tickFormat={(x) => (`$${x / 1000}k`)}
        />
        <VictoryBar
          data={data}
          x="quarter"
          y="earnings"
        />
      </VictoryChart>
    )
  }
}

// ReactDOM.render(<App/>, mountNode);

const app = document.getElementById('chartdisp');
ReactDOM.render(<App />, app);
