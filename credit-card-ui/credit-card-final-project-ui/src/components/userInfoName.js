import { Button, Form, Card, Accordion } from 'react-bootstrap';
import React from 'react';

class UserInfoName extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: null,
      firstName: null,
      lastName: null,
    };
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
              <Form>
                <Form.Group controlId="exampleForm.ControlInput1">
                  <Form.Label>Choose Username:</Form.Label>
                  <Form.Control type="email" placeholder="Username" />
                </Form.Group>
                <Form.Group controlId="exampleForm.ControlInput1">
                  <Form.Label>Input First Name:</Form.Label>
                  <Form.Control type="firstName" placeholder="First Name" />
                </Form.Group>
                <Form.Group controlId="exampleForm.ControlInput1">
                  <Form.Label>Input Last Name:</Form.Label>
                  <Form.Control type="lastName" placeholder="Last Name" />
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