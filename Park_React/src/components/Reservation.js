import Ligne from "./Ligne";
import "./Reservation.css";
import myJson from '../example.json'

function Reservation(){
  const fff = ()=>{
    
  }
   
    return(
        <table>
                <tr class="thead">
                  <th>Place vide </th>
                  <th>Réserver</th>
                  <th>temps restant (min:sec)</th>
                </tr>
                
                {
                  myJson[2].amount.map( item => (
                    <Ligne placeNumber={item}/>
                  ))
                }
                  
              </table>
    )
}
export default Reservation;