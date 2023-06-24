import React from "react"
import Navebar from '../Menu/navebar.jsx'
import "./style.css"

const Header = (props) =>{
    return(
        <div className="header">
            <ul>
                <Navebar link="/" name="Home"></Navebar>
                <Navebar link="/contato" name="Contato"></Navebar>
                <Navebar link="/sobre" name="Sobre"></Navebar>
                <Navebar link="/cronometro" name="Cronometro"></Navebar>
                <Navebar link="/calculadora" name="Calculadora"></Navebar>
            </ul>
        </div>
    )
}

export default Header