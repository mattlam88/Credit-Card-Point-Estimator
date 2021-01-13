import { Button, Form, FormControl, InputGroup, Card, Accordion } from 'react-bootstrap';
import React from 'react';
import axios from 'axios';

class UserInfoBudget extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      month: null,
      year: null,
      restaurantSpend: null,
      grocerySpend: null,
      nonCategorySpend: null,
      utilitySpend: null,
      gasSpend: null,
    };
  }

  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  }

  onSubmit = (e) => {
    e.preventDefault();
    const { month, year, restaurantSpend, grocerySpend, nonCategorySpend, utilitySpend, gasSpend } = this.state;

    axios.post('/', {
      month, year, restaurantSpend, grocerySpend, nonCategorySpend, utilitySpend, gasSpend
    }).then((result) => {
      // access the result right here
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
                  <Form.Control as="select" value={this.state.month} onChange={this.onChange}>
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
                  <Form.Control as="select" value={this.state.year} onChange={this.onChange}>
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
                  <FormControl aria-label="Amount (to the nearest dollar)" value={this.state.restaurantSpend} onChange={this.onChange}/>
                  <InputGroup.Append>
                    <InputGroup.Text>.00</InputGroup.Text>
                  </InputGroup.Append>
                </InputGroup>

                <label htmlFor="basic-url">Grocery Spend:</label>
                <InputGroup className="mb-3">
                  <InputGroup.Prepend>
                    <InputGroup.Text>$</InputGroup.Text>
                  </InputGroup.Prepend>
                  <FormControl aria-label="Amount (to the nearest dollar)" value={this.state.grocerySpend} onChange={this.onChange}/>
                  <InputGroup.Append>
                    <InputGroup.Text>.00</InputGroup.Text>
                  </InputGroup.Append>
                </InputGroup>

                <label htmlFor="basic-url">Non-Category Spend:</label>
                <InputGroup className="mb-3">
                  <InputGroup.Prepend>
                    <InputGroup.Text>$</InputGroup.Text>
                  </InputGroup.Prepend>
                  <FormControl aria-label="Amount (to the nearest dollar)" value={this.state.nonCategorySpend} onChange={this.onChange}/>
                  <InputGroup.Append>
                    <InputGroup.Text>.00</InputGroup.Text>
                  </InputGroup.Append>
                </InputGroup>

                <label htmlFor="basic-url">Utility Spend:</label>
                <InputGroup className="mb-3">
                  <InputGroup.Prepend>
                    <InputGroup.Text>$</InputGroup.Text>
                  </InputGroup.Prepend>
                  <FormControl aria-label="Amount (to the nearest dollar)" value={this.state.utilitySpend} onChange={this.onChange}/>
                  <InputGroup.Append>
                    <InputGroup.Text>.00</InputGroup.Text>
                  </InputGroup.Append>
                </InputGroup>

                <label htmlFor="basic-url">Gas Spend:</label>
                <InputGroup className="mb-3">
                  <InputGroup.Prepend>
                    <InputGroup.Text>$</InputGroup.Text>
                  </InputGroup.Prepend>
                  <FormControl aria-label="Amount (to the nearest dollar)" value={this.state.gasSpend} onChange={this.onChange}/>
                  <InputGroup.Append>
                    <InputGroup.Text>.00</InputGroup.Text>
                  </InputGroup.Append>
                </InputGroup>
              </Form>

              <Button as="input" type="submit" value="Submit" />{' '}

            </Card.Body>
          </Accordion.Collapse>
        </Card>
      </Accordion>
    )
  }
}

export default UserInfoBudget;