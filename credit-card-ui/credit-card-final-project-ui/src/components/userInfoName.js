import { Button, Form, Card, Accordion } from 'react-bootstrap';
import React from 'react';
import axios from 'axios';

class UserInfoName extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: null,
      firstName: null,
      lastName: null,
    };
  }
  
  onChange = (e) => {
    this.setState({[e.target.name]: e.target.value});
  }

  onSubmit = (e) => {
    e.preventDefault();
    const {username, firstName, lastName} = this.state;

    axios.post('/', {username, firstName, lastName}).then((result) => {
      // access the result right here
    });
  }

  

  render() {
    return (
      <Accordion>
        <Card>
          <Card.Header>
            <Accordion.Toggle as={Button} variant="link" eventKey="0">
              Step 1. Add Personal Details
              </Accordion.Toggle>
          </Card.Header>
          <Accordion.Collapse eventKey="0">
            <Card.Body>
              <Form onSubmit={this.onSubmit}>
                <Form.Group controlId="exampleForm.ControlInput1">
                  <Form.Label>Choose Username:</Form.Label>
                  <Form.Control type="email" placeholder="Username" value={this.state.username} onChange={this.onChange} />
                </Form.Group>
                <Form.Group controlId="exampleForm.ControlInput1">
                  <Form.Label>Input First Name:</Form.Label>
                  <Form.Control type="firstName" placeholder="First Name" value={this.state.firstName} onChange={this.onChange} />
                </Form.Group>
                <Form.Group controlId="exampleForm.ControlInput1">
                  <Form.Label>Input Last Name:</Form.Label>
                  <Form.Control type="lastName" placeholder="Last Name" value={this.state.lastName} onChange={this.onChange} />
                </Form.Group>
              </Form>

              <Button as="input" type="submit" value="Submit" />{' '}

            </Card.Body>
          </Accordion.Collapse>
        </Card>
      </Accordion>
    )
  }
}
export default UserInfoName;