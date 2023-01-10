import "./section.css";

function Section(props) {
  return (
    
        <div class="section">
          <h2 class="title"> {props.title}</h2>
          <p class="nbr">{props.amount}</p>
        </div>
      
  );
}
export default Section;
