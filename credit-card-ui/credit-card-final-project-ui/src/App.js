import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, Nav } from 'react-bootstrap';
import Welcome from './components/WelcomeJumbotron';
import UserInfo from './components/userInfo';
import PieGraph from './components/CategorySpendGraph';
import BarGraph from './components/PointsMonthlySpendGraph';
import React, { useState, useEffect } from 'react';
// import NavbarUI from '.components/NavbarUI';




function App() {

  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

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
      <p>The current time is {currentTime}.</p>
      <div className='jumbotron-container'>
        <Welcome name='Matt'  /> 
      </div>

      <div className="userinput">
        <UserInfo  />
      </div>

      <div class="graph_1">
        <PieGraph  />
      </div>
      <div class="graph_2">

        <BarGraph  />

      </div>
    </div >
  );
}

export default App;
