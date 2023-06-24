import './style.css';
import React,{useEffect, useState} from "react";
import Header from '../../Components/Header';

function Calculadora() {

  const [numero1, setNumero1] = useState(0);
  const [numero2, setNumero2] = useState(0);
  const [operacao, setOperacao] = useState(0);
  const [resultado, setResultado] = useState(0);

  const digitarNumero = (e)=>{

    if (operacao==0){
      setNumero1(state => {
        return parseInt(state + e.target.id)
      })
    }else{
      setNumero2(state => {
        return parseInt(state + e.target.id)
      })
    }
  }

  const DigitarOperacao = (e) =>{
    setOperacao(e.target.id)
  }

  const Resultado = (e) => {
    if(operacao == "+"){
        setResultado(numero1 + numero2);
    } else if (operacao == "."){
        setResultado(numero1 * numero2);
    } else if (operacao == "-"){
        setResultado(numero1 - numero2);
    } else if (operacao == "/"){
        setResultado(numero1 / numero2);
    }
}

  const LimparTudo = (e) => {
    setNumero1(0);
    setNumero2(0);
    setOperacao(0);
    setResultado(0);
  }

  return (
    <div className="Calc">
      <div className='numeros'>
        <h4>{numero1}</h4>
        <h4>{operacao}</h4>
        <h4>{numero2}</h4>
        <h4>{resultado}</h4>
      </div>
      <div className='Size-button'>
        <button id='1' onClick={digitarNumero}>1</button>
        <button id='2' onClick={digitarNumero}>2</button>
        <button id='3' onClick={digitarNumero}>3</button>
      </div>
      <div className='Size-button'>
        <button id='4' onClick={digitarNumero}>4</button>
        <button id='5' onClick={digitarNumero}>5</button>
        <button id='6' onClick={digitarNumero}>6</button>
      </div>
      <div className='Size-button'>
        <button id='7' onClick={digitarNumero}>7</button>
        <button id='8' onClick={digitarNumero}>8</button>
        <button id='9' onClick={digitarNumero}>9</button>
        <button id='-' onClick={DigitarOperacao}>-</button>
      </div>
      <div className='Size-button'>
        <button id='0' onClick={digitarNumero}>0</button>
        <button id='.' onClick={DigitarOperacao}>.</button>
        <button id='/' onClick={DigitarOperacao}>/</button>
        <button id='+' onClick={DigitarOperacao}>+</button>
      </div>
      <div className='Size-button'>
        <button id='=' onClick={Resultado}>=</button>
        <button id='Limpar' onClick={LimparTudo}>Limpar</button>
      </div>
      
    </div>
  );
}

export default Calculadora;