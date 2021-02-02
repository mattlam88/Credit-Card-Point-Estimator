import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, Nav } from 'react-bootstrap';
import Welcome from './components/WelcomeJumbotron';
import UserInfoName from './components/userInfoName';
import UserInfoCreditCard from './components/userInfoCreditCard';
import UserInfoBudget from './components/userInfoBudget';
import PieGraph from './components/CategorySpendGraph';
import LineGraph from './components/PointsMonthlySpendGraph';

function App() {

  // use state hook create hook to create username state and then pass it down.

  return (
    <div>
      <Navbar bg="dark" expand="lg" variant='dark'>
      <Navbar.Brand href="#home">Credit Card Tracker</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <Nav.Link href="#home">Home</Nav.Link>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
      <div className='jumbotron-container'>
        <Welcome name='Matt'  /> 
      </div>

      <div className="userinput">
        <UserInfoName  />
        <UserInfoCreditCard  usern={this.state.username}/>
        <UserInfoBudget  />
      </div>

      <div class="graph_1">
        <PieGraph  usern={this.state.username}/>
      </div>
      <div class="graph_2">

        <LineGraph  />

      </div>
    </div >
  );
}

export default App;
