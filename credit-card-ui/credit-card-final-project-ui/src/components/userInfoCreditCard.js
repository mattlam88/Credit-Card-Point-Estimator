import { Button, Form, Card, Accordion } from 'react-bootstrap';
import React from 'react';
import axios from 'axios'

class UserInfoCreditCard extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      creditCardIssuer: null,
      creditCardType: null,
      creditCardRewardPoints: null,
      restaurantMultiplier: null,
      groceryMultiplier: null,
      nonCategoryMultiplier: null,
      utilityMultiplier: null,
      gasMultiplier: null,
    };
  }

  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  }

  onSubmit = (e) => {
    e.preventDefault();
    const { creditCardIssuer, creditCardType, creditCardRewardPoints,
      restaurantMultiplier, groceryMultiplier, nonCategoryMultiplier,
      utilityMultiplier, gasMultiplier } = this.state;

    axios.post('/', {
      creditCardIssuer, creditCardType, creditCardRewardPoints,
      restaurantMultiplier, groceryMultiplier, nonCategoryMultiplier,
      utilityMultiplier, gasMultiplier
    }).then((result) => {
      // access the result right here
    });
  }

  render() {
    return (
      <Accordion>
        <Card>
          <Card.Header>
            <Accordion.Toggle as={Button} variant="link" eventKey="1">
              Step 2. Add Credit Cards
              </Accordion.Toggle>
          </Card.Header>
          <Accordion.Collapse eventKey="1">
            <Card.Body>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Credit Card Issuer:</Form.Label>
                <Form.Control as="select" value={this.state.creditCardIssuer} onChange={this.onChange}>
                  <option>Chase</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Credit Card Type:</Form.Label>
                <Form.Control as="select"value={this.state.creditCardType} onChange={this.onChange} >
                  <option>Chase Sapphire Reserve</option>
                  <option>Chase Sapphire Preferred</option>
                  <option>Chase Freedom</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Credit Card Reward Points:</Form.Label>
                <Form.Control as="select" value={this.state.creditCardRewardPoints} onChange={this.onChange}>
                  <option>Chase Ultimate Rewards (UR)</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Restaurant Multiplier:</Form.Label>
                <Form.Control as="select" value={this.state.restaurantMultiplier} onChange={this.onChange}>
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Grocery Multiplier:</Form.Label>
                <Form.Control as="select" value={this.state.groceryMultiplier} onChange={this.onChange}>
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Non-Category Multiplier:</Form.Label>
                <Form.Control as="select" value={this.state.nonCategoryMultiplier} onChange={this.onChange}>
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Utility Multiplier:</Form.Label>
                <Form.Control as="select" value={this.state.utilityMultiplier} onChange={this.onChange}>
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Gas Multiplier:</Form.Label>
                <Form.Control as="select" value={this.state.gasMultiplier} onChange={this.onChange}>
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                </Form.Control>
              </Form.Group>

              <Button as="input" type="submit" value="Submit" />{' '}

            </Card.Body>
          </Accordion.Collapse>
        </Card>
      </Accordion>
    )
  }
}

export default UserInfoCreditCard;