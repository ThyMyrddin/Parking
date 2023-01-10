
import './App.css';

import Section from "./components/Section"
import Aside from "./components/Aside"
import ParkingPlan from"./components/ParkingPlan";
import Reservation from './components/Reservation';
import myJson from './example.json'

function App() {
    
  console.log(myJson)

    return (
      <div>
        
      <Aside></Aside>
      <div className='flex'>
      <div class="body">
      <div class="infos-display">
      <Section title={myJson[0]['title']} amount={myJson[0].amount}/>
      <Section title={myJson[1].title} amount={myJson[1].amount}/>
      </div>
      </div></div>
      <ParkingPlan/>
      <Reservation className="res" /></div>
    
    
  );
}

export default App;
