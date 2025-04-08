import { useState} from "react";
import axios from "axios";

function NurseDetails() {
    const [nurse, setNurse] = useState([]);

  const getNurse = () => {
    axios.get('http://127.0.0.1:8004/nurseget/')
    .then(res=>setNurse(res.data))
    .then(console.log(nurse))
    .catch(err=>console.error(err))
}
return (
    <>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Department</th>
                </tr>
            </thead>
            <tbody>
                {nurse.map((nurse) => (
                    <tr key={nurse.id}>
                        <td>{nurse.name}</td>
                        <td>{nurse.department}</td>
                    </tr>
                ))}
            </tbody>
        </table>
        <button onClick={getNurse}>Get Nurse Details</button>
    </>
);
}
export default NurseDetails;