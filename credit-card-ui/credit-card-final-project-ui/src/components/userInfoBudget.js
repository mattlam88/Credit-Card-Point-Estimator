import { Button, Form, FormControl, InputGroup, Card, Accordion } from 'react-bootstrap';
import React from 'react';
import axios from 'axios';

class UserInfoBudget extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      month: 'January',
      year: 2020,
      restaurantSpend: 0,
      grocerySpend: 0,
      nonCategorySpend: 0,
      utilitySpend: 0,
      gasSpend: 0,
    };
  }

  onChangeMonth = (e) => {
    this.setState({ month: e.target.value });
  }

  onChangeYear = (e) => {
    this.setState({ year: e.target.value });
  }

  onChangeRestaurantSpend = (e) => {
    this.setState({ restaurantSpend: e.target.value });
  }
  
  onChangeGrocerySpend = (e) => {
    this.setState({ grocerySpend: e.target.value });
  }

  onChangeNonCateogrySpend = (e) => {
    this.setState({ nonCategorySpend: e.target.value });
  }

  onChangeUtilitySpend = (e) => {
    this.setState({ utilitySpend: e.target.value });
  }

  onChangeGasSpend = (e) => {
    this.setState({ gasSpend: e.target.value });
  }

  onSubmitUserInfoBudget = () => {
    // console.log(this.state.month)
    // console.log(this.state.year)
    // console.log(this.state.restaurantSpend)
    // console.log(this.state.grocerySpend)
    // console.log(this.state.nonCategorySpend)
    // console.log(this.state.utilitySpend)
    // console.log(this.state.gasSpend)

    axios.post('http://localhost:5000/', {
      month: this.state.month,
      year: this.state.year,
      restaurantSpend: this.state.restaurantSpend,
      grocerySpend: this.state.grocerySpend,
      nonCategorySpend: this.state.nonCategorySpend,
      utilitySpend: this.state.utilitySpend,
      gasSpend: this.state.gasSpend
    }).then((result) => {
      console.log(result)
    });
  }

  render() {
    return (
      <Accordion>
        <Card>
          <Card.Header>
            <Accordion.Toggle as={Button} variant="link" eventKey="2">
              Step 3. Add Monthly Spend
              </Accordion.Toggle>
          </Card.Header>
          <Accordion.Collapse eventKey="2">
            <Card.Body>
              <Form>
                <Form.Group controlId="exampleForm.ControlSelect1">
                  <Form.Label>Select Monthly Budget:</Form.Label>
                  <Form.Control as="select" value={this.state.month} onChange={this.onChangeMonth.bind(this)}>
                    <option>January</option>
                    <option>February</option>
                    <option>March</option>
                    <option>April</option>
                    <option>May</option>
                    <option>June</option>
                    <option>July</option>
                    <option>August</option>
                    <option>September</option>
                    <option>November</option>
                    <option>December</option>
                  </Form.Control>
                </Form.Group>

                <Form.Group controlId="exampleForm.ControlSelect1">
                  <Form.Label>Select Year:</Form.Label>
                  <Form.Control as="select" value={this.state.year} onChange={this.onChangeYear.bind(this)}>
                    <option>2020</option>
                    <option>2021</option>
                    <option>2022</option>
                    <option>2023</option>
                    <option>2024</option>
                    <option>2025</option>
                    <option>2026</option>
                    <option>2027</option>
                    <option>2028</option>
                    <option>2029</option>
                  </Form.Control>
                </Form.Group>

                <label htmlFor="basic-url">Restaurant Spend:</label>
                <InputGroup className="mb-3">
                  <InputGroup.Prepend>
                    <InputGroup.Text>$</InputGroup.Text>
                  </InputGroup.Prepend>
                  <FormControl aria-label="Amount (to the nearest dollar)" value={this.state.restaurantSpend} onChange={this.onChangeRestaurantSpend.bind(this)}/>
                  <InputGroup.Append>
                    <InputGroup.Text>.00</InputGroup.Text>
                  </InputGroup.Append>
                </InputGroup>

                <label htmlFor="basic-url">Grocery Spend:</label>
                <InputGroup className="mb-3">
                  <InputGroup.Prepend>
                    <InputGroup.Text>$</InputGroup.Text>
                  </InputGroup.Prepend>
                  <FormControl aria-label="Amount (to the nearest dollar)" value={this.state.grocerySpend} onChange={this.onChangeGrocerySpend.bind(this)}/>
                  <InputGroup.Append>
                    <InputGroup.Text>.00</InputGroup.Text>
                  </InputGroup.Append>
                </InputGroup>

                <label htmlFor="basic-url">Non-Category Spend:</label>
                <InputGroup className="mb-3">
                  <InputGroup.Prepend>
                    <InputGroup.Text>$</InputGroup.Text>
                  </InputGroup.Prepend>
                  <FormControl aria-label="Amount (to the nearest dollar)" value={this.state.nonCategorySpend} onChange={this.onChangeNonCateogrySpend.bind(this)}/>
                  <InputGroup.Append>
                    <InputGroup.Text>.00</InputGroup.Text>
                  </InputGroup.Append>
                </InputGroup>

                <label htmlFor="basic-url">Utility Spend:</label>
                <InputGroup className="mb-3">
                  <InputGroup.Prepend>
                    <InputGroup.Text>$</InputGroup.Text>
                  </InputGroup.Prepend>
                  <FormControl aria-label="Amount (to the nearest dollar)" value={this.state.utilitySpend} onChange={this.onChangeUtilitySpend.bind(this)}/>
                  <InputGroup.Append>
                    <InputGroup.Text>.00</InputGroup.Text>
                  </InputGroup.Append>
                </InputGroup>

                <label htmlFor="basic-url">Gas Spend:</label>
                <InputGroup className="mb-3">
                  <InputGroup.Prepend>
                    <InputGroup.Text>$</InputGroup.Text>
                  </InputGroup.Prepend>
                  <FormControl aria-label="Amount (to the nearest dollar)" value={this.state.gasSpend} onChange={this.onChangeGasSpend.bind(this)}/>
                  <InputGroup.Append>
                    <InputGroup.Text>.00</InputGroup.Text>
                  </InputGroup.Append>
                </InputGroup>
              </Form>

              <Button as="input" type="submit" value="Submit" onClick={this.onSubmitUserInfoBudget} />{' '}

            </Card.Body>
          </Accordion.Collapse>
        </Card>
      </Accordion>
    )
  }
}

export default UserInfoBudget;