import React from "react"
import {Link} from 'react-router-dom'

const Navebar = (props) =>{
    return(
        <>
                <li>
                    <Link to={props.link}>{props.name}</Link>
                </li>
        </>
    )
}

export default Navebar