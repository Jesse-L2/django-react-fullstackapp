import { useState, useEffect } from "react";
import api from "../../api";

const Home = () => {
  const [notes, setNotes] = useState([]);
  const [content, setContent] = useState("");
  const [title, setTitle] = useState("");

  return <div>Home</div>;
};

export default Home;
