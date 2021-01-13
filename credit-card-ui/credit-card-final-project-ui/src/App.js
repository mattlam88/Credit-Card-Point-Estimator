import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, Nav } from 'react-bootstrap';
import Welcome from './components/WelcomeJumbotron';
import UserInfoName from './components/userInfoName';
import UserInfoCreditCard from './components/userInfoCreditCard';
import UserInfoBudget from './components/userInfoBudget';
import PieGraph from './components/CategorySpendGraph';
import BarGraph from './components/PointsMonthlySpendGraph';
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {

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
        <UserInfoCreditCard  />
        <UserInfoBudget  />
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
