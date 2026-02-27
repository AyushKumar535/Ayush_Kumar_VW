import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

function Home() {
  const navigate = useNavigate();
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    const storedData = sessionStorage.getItem("userData");

    if (!storedData) {
      navigate("/");
    } else {
      setUserData(JSON.parse(storedData));
    }
  }, [navigate]);

  const handleLogout = () => {
    sessionStorage.removeItem("userData");
    navigate("/");
  };

  if (!userData) return null;

  return (
    <div>
      <div className="navbar">
        <div className="welcome-text">
          Welcome {userData.name}
        </div>
        <button className="logout-btn" onClick={handleLogout}>
          Logout
        </button>
      </div>

      <div className="details-container">
        <h2>User Details</h2>
        <p><strong>Name:</strong> {userData.name}</p>
        <p><strong>Email:</strong> {userData.email}</p>
        <p><strong>Phone:</strong> {userData.phone}</p>
        <p><strong>Address:</strong> {userData.address}</p>
      </div>
    </div>
  );
}

export default Home;