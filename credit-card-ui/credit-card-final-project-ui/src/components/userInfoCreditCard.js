import { Button, Form, Card, Accordion } from 'react-bootstrap';
import React from 'react';

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
                <Form.Control as="select">
                  <option>Chase</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Credit Card Type:</Form.Label>
                <Form.Control as="select">
                  <option>Chase Sapphire Reserve</option>
                  <option>Chase Sapphire Preferred</option>
                  <option>Chase Freedom</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Credit Card Reward Points:</Form.Label>
                <Form.Control as="select">
                  <option>Chase Ultimate Rewards (UR)</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Restaurant Multiplier:</Form.Label>
                <Form.Control as="select">
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Grocery Multiplier:</Form.Label>
                <Form.Control as="select">
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Non-Category Multiplier:</Form.Label>
                <Form.Control as="select">
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Utility Multiplier:</Form.Label>
                <Form.Control as="select">
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Gas Multiplier:</Form.Label>
                <Form.Control as="select">
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