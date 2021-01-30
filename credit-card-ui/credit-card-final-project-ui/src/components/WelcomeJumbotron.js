import { Jumbotron } from 'react-bootstrap';

export default function Welcome(props) {
    return (
        <Jumbotron>
            <h1>Hello, {props.name}!</h1>
            <p>
                Let's begin estimating how many credit points you will accumulate in a year!
            </p>
        </Jumbotron>
    )
}