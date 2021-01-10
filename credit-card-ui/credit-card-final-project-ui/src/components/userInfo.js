import { Button, Form, FormControl, InputGroup, Card, Accordion } from 'react-bootstrap';

export default function UserInfo (props) {

    const submitForm = (form) =>{
      fetch('/time', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(form.data)})
    }

    return(
        <Accordion defaultActiveKey="0">
          <Card>
            <Card.Header>
              <Accordion.Toggle as={Button} variant="link" eventKey="0">
                Step 1. Add Personal Details
              </Accordion.Toggle>
            </Card.Header>
            <Accordion.Collapse eventKey="0">
              <Card.Body>
                <InputGroup className="mb-3">
                  <InputGroup.Prepend>
                    <InputGroup.Text id="basic-addon1">@</InputGroup.Text>
                  </InputGroup.Prepend>
                  <FormControl
                    placeholder="Username"
                    aria-label="Username"
                    aria-describedby="basic-addon1"
                  />
                </InputGroup>
                <InputGroup className="mb-3">
                  <InputGroup.Prepend>
                    <InputGroup.Text id="basic-addon1">@</InputGroup.Text>
                  </InputGroup.Prepend>
                  <FormControl
                    placeholder="First name"
                    aria-label="First name"
                    aria-describedby="basic-addon1"
                  />
                </InputGroup>
                <InputGroup className="mb-3">
                  <InputGroup.Prepend>
                    <InputGroup.Text id="basic-addon1">@</InputGroup.Text>
                  </InputGroup.Prepend>
                  <FormControl
                    placeholder="Last name"
                    aria-label="Last name"
                    aria-describedby="basic-addon1"
                  />
                </InputGroup>

                <Button as="input" type="submit" value="Submit" />{' '}

              </Card.Body>
            </Accordion.Collapse>
          </Card>

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

                <Button as="input" type="submit" value="Submit" />{' '}

              </Card.Body>
            </Accordion.Collapse>
          </Card>

          <Card>
            <Card.Header>
              <Accordion.Toggle as={Button} variant="link" eventKey="2">
                Step 3. Add Monthly Spend
              </Accordion.Toggle>
            </Card.Header>
            <Accordion.Collapse eventKey="2">
              <Card.Body>
                <Form onSubmit={submitForm}>
                  <Form.Group controlId="exampleForm.ControlSelect1">
                    <Form.Label>Select Monthly Budget:</Form.Label>
                    <Form.Control as="select">
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
                    <Form.Control as="select">
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

                  <label htmlFor="basic-url">Restaurant Spend</label>
                  <InputGroup className="mb-3">
                    <InputGroup.Prepend>
                      <InputGroup.Text>$</InputGroup.Text>
                    </InputGroup.Prepend>
                    <FormControl aria-label="Amount (to the nearest dollar)" />
                    <InputGroup.Append>
                      <InputGroup.Text>.00</InputGroup.Text>
                    </InputGroup.Append>
                  </InputGroup>

                  <label htmlFor="basic-url">Restaurant Spend:</label>
                  <InputGroup className="mb-3">
                    <InputGroup.Prepend>
                      <InputGroup.Text>$</InputGroup.Text>
                    </InputGroup.Prepend>
                    <FormControl aria-label="Amount (to the nearest dollar)" />
                    <InputGroup.Append>
                      <InputGroup.Text>.00</InputGroup.Text>
                    </InputGroup.Append>
                  </InputGroup>

                  <label htmlFor="basic-url">Grocery Spend:</label>
                  <InputGroup className="mb-3">
                    <InputGroup.Prepend>
                      <InputGroup.Text>$</InputGroup.Text>
                    </InputGroup.Prepend>
                    <FormControl aria-label="Amount (to the nearest dollar)" />
                    <InputGroup.Append>
                      <InputGroup.Text>.00</InputGroup.Text>
                    </InputGroup.Append>
                  </InputGroup>

                  <label htmlFor="basic-url">Non-Category Spend:</label>
                  <InputGroup className="mb-3">
                    <InputGroup.Prepend>
                      <InputGroup.Text>$</InputGroup.Text>
                    </InputGroup.Prepend>
                    <FormControl aria-label="Amount (to the nearest dollar)" />
                    <InputGroup.Append>
                      <InputGroup.Text>.00</InputGroup.Text>
                    </InputGroup.Append>
                  </InputGroup>

                  <label htmlFor="basic-url">Utility Spend:</label>
                  <InputGroup className="mb-3">
                    <InputGroup.Prepend>
                      <InputGroup.Text>$</InputGroup.Text>
                    </InputGroup.Prepend>
                    <FormControl aria-label="Amount (to the nearest dollar)" />
                    <InputGroup.Append>
                      <InputGroup.Text>.00</InputGroup.Text>
                    </InputGroup.Append>
                  </InputGroup>

                  <label htmlFor="basic-url">Gas Spend:</label>
                  <InputGroup className="mb-3">
                    <InputGroup.Prepend>
                      <InputGroup.Text>$</InputGroup.Text>
                    </InputGroup.Prepend>
                    <FormControl aria-label="Amount (to the nearest dollar)" />
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

