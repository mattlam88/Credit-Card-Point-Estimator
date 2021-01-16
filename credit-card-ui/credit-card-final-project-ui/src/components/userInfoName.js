import { Button, Form, Card, Accordion } from 'react-bootstrap';
import React from 'react';
import axios from 'axios';

class UserInfoName extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      firstName: '',
      lastName: '',
    };
  }

  onChangeUsername = (e) => {
    this.setState({ username: e.target.value });
  }

  onChangeFirstName = (e) => {
    this.setState({ firstName: e.target.value });
  }

  onChangeLastName = (e) => {
    this.setState({ lastName: e.target.value })
  }
  onSubmitUserInfoName = () => {
    console.log(this.state.username)
    console.log(this.state.firstName)
    console.log(this.state.lastName)

    axios.post('http://localhost:5000/', {
      username: this.state.username,
      firstName: this.state.firstName,
      lastName: this.state.lastName
    }).then((result) => {
      console.log(result)
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
              <Form>
                <Form.Group controlId="userInfoUsername">
                  <Form.Label>Choose Username:</Form.Label>
                  <Form.Control type="username" placeholder="Username" value={this.state.username} onChange={this.onChangeUsername.bind(this)} />
                </Form.Group>
                <Form.Group controlId="userInfoFirstName">
                  <Form.Label>Input First Name:</Form.Label>
                  <Form.Control type="firstName" placeholder="First Name" value={this.state.firstName} onChange={this.onChangeFirstName.bind(this)} />
                </Form.Group>
                <Form.Group controlId="userInfoLastName">
                  <Form.Label>Input Last Name:</Form.Label>
                  <Form.Control type="lastName" placeholder="Last Name" value={this.state.lastName} onChange={this.onChangeLastName.bind(this)} />
                </Form.Group>
              </Form>

              <Button as="input" type="submit" value="Submit" onClick={this.onSubmitUserInfoName} />{' '}

            </Card.Body>
          </Accordion.Collapse>
        </Card>
      </Accordion>
    )
  }
}
export default UserInfoName;