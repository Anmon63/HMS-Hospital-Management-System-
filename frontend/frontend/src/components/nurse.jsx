import { useState } from "react";
import AxiosInstance from "./axios";
import { useNavigate } from "react-router-dom"; // To navigate between pages

    
    const Nurse = () => {
        const navigate = useNavigate(); // Hook for navigation
        const [name, setName] = useState('');
        const [department, setDepartment] = useState('');

        const handleSubmit =async (e) => {
            e.preventDefault();
            console.log(name, department);
            try {
                const response = await AxiosInstance.post('nursecreate/', {
                    name:name.trim(),
                    department:department.trim()
                });
                console.log("Success:", response.data);
                alert("Nurse created successfully!");
                navigate("/nurse"); // Redirect to home after submission
                setName('');
                setDepartment('');
            } catch (error) {
                console.error("Error:", error);
                alert("Error creating nurse!");
            }
        };
return(
    <>
               <div>
                    <form onSubmit={handleSubmit}>
                        <h1>Nurse Registration</h1>
                        <h2>Enter Nurse Details</h2>
                        <label htmlFor="name">Name:</label>
                        <input type="text" placeholder="Enter the Name" value={name} onChange={(e) => setName(e.target.value)}/>
                        <label htmlFor="department">Department:</label>
                        <input type="text" placeholder="Enter the Department" value={department} onChange={(e) => setDepartment(e.target.value)} />
                        <button type="submit">Submit</button>
                    </form>
               </div>
    </>
)}
export default Nurse;