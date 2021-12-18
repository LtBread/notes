import React from "react";


const ToDoItem = ({todo}) => {
    return(
        <tr>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.user}
            </td>
            <td>
                {todo.is_active}
            </td>
             <td>
                {todo.is_completed}
            </td>
        </tr>
    )
}

const ToDoList = ({todos}) => {
    return(
        <table>
            <th>
                TEXT
            </th>
            <th>
                PROJECT
            </th>
            <th>
                USER
            </th>
            <th>
                ACTIVE
            </th>
            <th>
                COMPLETED
            </th>
            {todos.map((todo) => <ToDoItem todo={todo} />)}
        </table>
    )
}

export default ToDoList;