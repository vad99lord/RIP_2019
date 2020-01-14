import React from 'react';
import './App.css';
import Home from "./Home/Home";
import axios from 'axios';


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            repos: [],
        }
    }

    componentDidMount() {
        axios.get('https://api.github.com/users/OlegElizarov/repos')
            .then(response => {
                this.setState({repos: response.data});
            })
            .catch(error => {
                console.log(error);
            });
    }

    render() {
        return (
            <div class="maindiv">
                <h1>OlegElizarov repositories</h1>
                <ul>
                    <Home list={this.state.repos}/>
                </ul>
            </div>
        );
    }
}

export default App;
