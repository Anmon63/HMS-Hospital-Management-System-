import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Doctor from "./components/doctor"; // Import Doctor.jsx
import DoctorDetails from "./components/doctordet"; // Import DoctorDetails.jsx
import Nurse from "./components/nurse"; // Import Nurse.jsx
import NurseDetails from "./components/nursedet";

function App() {
  return (
    <Router>
      <nav> 
        <Link to="/doctor">Doctor</Link>|
        <Link to="/doctordet">Doctor Details</Link>|
        <Link to="/nurse">Nurse</Link>|
        <Link to="/nursedet">Nurse Details</Link>|
        <a href="http://127.0.0.1:8004/patientdet/">Patient Details</a>|
        <a href="http://127.0.0.1:8004/home/">Home</a>
      </nav>

      <Routes>
        <Route path="/doctor" element={<Doctor />} />
        <Route path="/doctordet" element={<DoctorDetails />} />
        <Route path="/nurse" element={<Nurse />} />
        <Route path="/nursedet" element={<NurseDetails />} />
        {/* Add more routes as needed */}
      </Routes>
    </Router>
  );
}
export default App
