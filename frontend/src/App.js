import React from "react";
import {HashRouter, BrowserRouter, Route, Routes, Link, Navigate} from 'react-router-dom'
import axios from "axios";
import logo from './logo.svg';
import './App.css';

import UserList from "./components/Users";
import ProjectList from "./components/Projects";
import ToDoList from "./components/ToDo";
import Menu from "./components/Menu";
import Footer from "./components/Footer";

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
        }
    }

    componentDidMount() {
        axios
            .get('http://127.0.0.1:8000/api/users')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => console.log(error))

        axios
            .get('http://127.0.0.1:8000/api/projects')
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects
                    }
                )
            })
            .catch(error => console.log(error))

        axios
            .get('http://127.0.0.1:8000/api/todos')
            .then(response => {
                const todos = response.data
                this.setState(
                    {
                        'todos': todos
                    }
                )
            })
            .catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                {/*<Menu/>*/}
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li><Link to='/'>Users</Link></li>
                            <li><Link to='/projects'>Projects</Link></li>
                            <li><Link to='/todos'>To Do</Link></li>
                        </ul>
                    </nav>
                    <Routes>
                        <Route exact path='/' element={<UserList users={this.state.users} /> } />
                        <Route exact path='/projects' element={<ProjectList projects={this.state.projects} /> } />
                        <Route exact path='/todos' element={<ToDoList todos={this.state.todos} /> } />
                    </Routes>
                </BrowserRouter>
                {/*<Footer/>*/}
            </div>
        )
    }
}

export default App;