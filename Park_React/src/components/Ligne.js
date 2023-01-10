function Ligne(props) {
  const startTimer1 = (e) => {
    e.preventDefault();
    const departMinutes = 2;
    let temps = departMinutes * 60;

    const timerElement = document.getElementById("timer");
    document.querySelector("button").disabled = true;

    setInterval(() => {
      let minutes = parseInt(temps / 60, 10);
      let secondes = parseInt(temps % 60, 10);

      minutes = minutes < 10 ? "0" + minutes : minutes;
      secondes = secondes < 10 ? "0" + secondes : secondes;

      timerElement.innerText = `${minutes}:${secondes}`;
      temps = temps <= 0 ? 0 : temps - 1;
    }, 1000);
  };
  return (
    <tr>
      <td>{props.placeNumber}</td>
      <td>
        <button onClick={startTimer1}>Book a place</button>
      </td>
      <td>
        <p id="timer"></p>
      </td>
    </tr>
  );
}

export default Ligne;
