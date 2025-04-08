import { useState} from "react";
import axios from "axios";

function DoctorDetails() {
    const [doctors, setDoctors] = useState([]);

  const getDoctors = () => {
    axios.get('http://127.0.0.1:8004/doctorget/')
    .then(res=>setDoctors(res.data))
    .then(console.log(doctors))
    .catch(err=>console.error(err))
}
return (
    <>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Specialization</th>
                </tr>
            </thead>
            <tbody>
                {doctors.map((doctor) => (
                    <tr key={doctor.id}>
                        <td>{doctor.name}</td>
                        <td>{doctor.department}</td>
                    </tr>
                ))}
            </tbody>
        </table>
        <button onClick={getDoctors}>Get Doctor Details</button>
    </>
);
}
export default DoctorDetails;