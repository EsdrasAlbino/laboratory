import React,{useEffect, useState} from "react";
import "./style.css"

export default function Body(){
    const [segundos, setSegundos] = useState(0);
    const [minutos, setMinutos] = useState(0);
    const [horas, setHoras] = useState(0);

    useEffect(() =>{
        if(segundos >= 59){
            setMinutos(minutos+1)
            setSegundos(0);
        }
        if(minutos >= 60){
            setMinutos(0)
            setHoras(horas+1)
        }
    }, [segundos])

    const adicionarHora = () =>{
        setHoras(horas+1)
    }
    const adicionarMinuto = () =>{
        setMinutos(minutos+1)
    }
    const adicionarSegundos = () =>{
        setSegundos(segundos+1)
    }

    setTimeout(()=>{
        setSegundos(segundos + 1)
        
    }, 1000)
    return(
        <div className="body">
        <h1 className="h1_size"><span class="horas">{horas <= 9 ? "0" + horas : horas}</span>:
            <span className="minutos">{minutos <= 9 ? "0" + minutos : minutos}</span>:
            <span className="segundos">{segundos <= 9 ? "0" + segundos : segundos}</span></h1>
            <button onClick={adicionarHora}>Add Horas</button>
            <button onClick={adicionarMinuto}>Add Minutos</button>
            <button onClick={adicionarSegundos}>Add Segundos</button>
        </div>
        
    )
}