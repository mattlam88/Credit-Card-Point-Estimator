import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, Nav } from 'react-bootstrap';
import Welcome from './components/WelcomeJumbotron';
import UserInfoName from './components/userInfoName';
import UserInfoCreditCard from './components/userInfoCreditCard';
import UserInfoBudget from './components/userInfoBudget';
import PieGraph from './components/CategorySpendGraph';
import LineGraph from './components/PointsMonthlySpendGraph';
import React, { useState } from "react";

function App()  {
  const [usern, setUsern] = useState("")
  const updateUsern = (userInfo) => {
    console.log(userInfo);
    setUsern(userInfo);
  }
  
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
        <Welcome name={usern}/> 
      </div>

      <div className="userinput">
        <UserInfoName  onChange={updateUsern}/>
        <UserInfoCreditCard  />
        <UserInfoBudget  />
      </div>

      <div class="graph_1">
        <PieGraph username={usern}/>
      </div>
      <div class="graph_2">

        <LineGraph username={usern}/>

      </div>
    </div >
  );
}


export default App;
