import { Button, Form, Card, Accordion } from 'react-bootstrap';
import React from 'react';
import axios from 'axios'

class UserInfoCreditCard extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      creditCardIssuer: 'Chase',
      creditCardType: 'Chase Sapphire Reserve',
      creditCardRewardPoints: 'Chase Ultimate Rewards (UR)',
      restaurantMultiplier: 1,
      groceryMultiplier: 1,
      nonCategoryMultiplier: 1,
      utilityMultiplier: 1,
      gasMultiplier: 1,
    };
  }

  onChangeCreditCardIssuer = (e) => {
    this.setState({ creditCardIssuer: e.target.value });
  }
  onChangeCreditCardType = (e) => {
    this.setState({ creditCardType: e.target.value });
  }
  onChangeCreditCardRewardPoints = (e) => {
    this.setState({ creditCardRewardPoints: e.target.value });
  }
  onChangeRestaurantMultiplier = (e) => {
    this.setState({ restaurantMultiplier: e.target.value });
  }
  onChangeGroceryMultiplier = (e) => {
    this.setState({ groceryMultiplier: e.target.value });
  }
  onChangeNonCategoryMultiplier = (e) => {
    this.setState({ nonCategoryMultiplier: e.target.value });
  }
  onChangeUtilityMultiplier = (e) => {
    this.setState({ utilityMultiplier: e.target.value });
  }
  onChangeGasMultiplier = (e) => {
    this.setState({ gasMultiplier: e.target.value });
  }
 
  onSubmitUserInfoCreditCard = () => {
    console.log(this.state.creditCardIssuer)
    console.log(this.state.creditCardType)
    console.log(this.state.creditCardRewardPoints)
    console.log(this.state.restaurantMultiplier)
    console.log(this.state.groceryMultiplier)
    console.log(this.state.nonCategoryMultiplier)
    console.log(this.state.utilityMultiplier)
    console.log(this.state.gasMultiplier)

    axios.post('http://localhost:5000/', {
      creditCardIssuer: this.state.creditCardIssuer,
      creditCardType: this.state.creditCardType,
      creditCardRewardPoints: this.state.creditCardRewardPoints,
      restaurantMultiplier: this.state.restaurantMultiplier,
      groceryMultiplier: this.state.groceryMultiplier,
      nonCategoryMultiplier: this.state.nonCategoryMultiplier,
      utilityMultiplier: this.state.utilityMultiplier,
      gasMultiplier: this.state.gasMultiplier
    }).then((result) => {
      console.log(result)
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
                <Form.Control as="select" value={this.state.creditCardIssuer} onChange={this.onChangeCreditCardIssuer.bind(this)}>
                  <option>Chase</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Credit Card Type:</Form.Label>
                <Form.Control as="select"value={this.state.creditCardType} onChange={this.onChangeCreditCardType.bind(this)} >
                  <option>Chase Sapphire Reserve</option>
                  <option>Chase Sapphire Preferred</option>
                  <option>Chase Freedom</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Credit Card Reward Points:</Form.Label>
                <Form.Control as="select" value={this.state.creditCardRewardPoints} onChange={this.onChangeCreditCardRewardPoints.bind(this)}>
                  <option>Chase Ultimate Rewards (UR)</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Restaurant Multiplier:</Form.Label>
                <Form.Control as="select" value={this.state.restaurantMultiplier} onChange={this.onChangeRestaurantMultiplier.bind(this)}>
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Grocery Multiplier:</Form.Label>
                <Form.Control as="select" value={this.state.groceryMultiplier} onChange={this.onChangeGroceryMultiplier.bind(this)}>
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Non-Category Multiplier:</Form.Label>
                <Form.Control as="select" value={this.state.nonCategoryMultiplier} onChange={this.onChangeNonCategoryMultiplier.bind(this)}>
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Utility Multiplier:</Form.Label>
                <Form.Control as="select" value={this.state.utilityMultiplier} onChange={this.onChangeUtilityMultiplier.bind(this)}>
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                </Form.Control>
              </Form.Group>
              <Form.Group controlId="exampleForm.ControlSelect1">
                <Form.Label>Select Gas Multiplier:</Form.Label>
                <Form.Control as="select" value={this.state.gasMultiplier} onChange={this.onChangeGasMultiplier.bind(this)}>
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                </Form.Control>
              </Form.Group>

              <Button as="input" type="submit" value="Submit" onClick={this.onSubmitUserInfoCreditCard} />{' '}

            </Card.Body>
          </Accordion.Collapse>
        </Card>
      </Accordion>
    )
  }
}

export default UserInfoCreditCard;