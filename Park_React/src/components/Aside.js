import "./Aside.css";

function Aside(){
    return (<div class="sidebar">
    
    <img class="logo" src={require("./logo.png")}/><br/><br/><br/><br/><br/><br/>
    <ul id="">
        <a href="#"><li class="sidebar-item">
        
        <h2>About our services</h2>
      </li></a>
      <hr/>
      <a href="#">
      <li class="sidebar-item">
        <h2>Parking infos</h2>
      </li></a>
      <hr/>
      <a href="">
      <li class="sidebar-item">
        <h2>Parking design</h2>
      </li></a>
      <hr/>
      <a href="">
      <li class="sidebar-item">
        <h2>Book a place</h2>
      </li></a>
      <hr/>
    </ul>
  </div>);
}
export default Aside;