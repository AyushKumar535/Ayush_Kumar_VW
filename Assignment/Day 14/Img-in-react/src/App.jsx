import { useState } from "react";
import "./App.css";

function App() {
  const mountains = [
    {
      name: "Bengal Tiger",
      desc: "NATIONAL ANIMAL OF INDIA",
      img: "National Animal.jpg",
    },
    {
      name: "Lotus",
      desc: "NATIONAL FLOWER OF INDIA",
      img: "National Flower.jpg",
    },
    {
      name: "Peacock",
      desc: "NATIONAL BIRD OF INDIA",
      img: "National Bird.jpg",
    },
    {
      name: "Indian Flag",
      desc: "NATIONAL FLAG OF INDIA",
      img: "National Flag.jpg",
    },
  ];

  const [selected, setSelected] = useState(mountains[0]);

  return (
    <div className="container">
      <h1>National Symbols of India</h1>

      {/* Main Image */}
      <div className="main">
        <img src={selected.img} alt={selected.name} />
        <h2>{selected.name}</h2>
        <p>{selected.desc}</p>
      </div>

      {/* Thumbnails */}
      <div className="thumbnails">
        {mountains.map((mountain, index) => (
          <img
            key={index}
            src={mountain.img}
            alt={mountain.name}
            className={
              selected.name === mountain.name ? "thumb active" : "thumb"
            }
            onClick={() => setSelected(mountain)}
          />
        ))}
      </div>
    </div>
  );
}

export default App;