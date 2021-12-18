import React from "react";


const ProjectItem = ({project}) => {
    return(
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.repository_link}
            </td>
            <td>
                {project.users}
            </td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return(
        <table>
            <th>
                PROJECT NAME
            </th>
            <th>
                REPOSITORY LINK
            </th>
            <th>
                USERNAME
            </th>
            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectList;