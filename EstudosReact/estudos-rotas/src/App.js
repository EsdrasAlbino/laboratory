import './App.css';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import Home from './Pages/Home'
import Contato from './Pages/contato'
import Sobre from './Pages/sobre'
import Cronometro from './Pages/Cronometro/Index';
import Calculadora from './Pages/Calcu/index'
import Header from './Components/Header';
import Footer from './Components/Footer';

function App() {
  return (
    <div className='App'>
      <Router >
        <Header className='App-header'/>
          <Routes>
            <Route exact path="/" element={<Home/>}/>
            <Route path="/contato" element={<Contato/>}/>
            <Route path="/sobre" element={<Sobre/>}/>
            <Route path='/cronometro' element={<Cronometro/>}/>
            <Route path='/calculadora' element={<Calculadora/>}/>
          </Routes>
      </Router>
      <Footer />
    </div>
  );
}

export default App;
