import { useState} from 'react'
import './App.css'
import axios from 'axios'

function App() {
  const [count, setCount] = useState([])
  const handleLoad=() => {
    axios.get('http://127.0.0.1:8001/patientget/')
    .then(res=>setCount(res.data))
    .then(console.log(count))
    .catch(err=>console.error(err))
  }

  return (
    <>
      {count.map((patient) => {
        return (
          <table>
            <tbody>
            <tr>
            <th>Name</th>
            <th>Age</th>
            </tr>
              <tr>
                <td key={patient.id}>{patient.name}</td>
                <td>{patient.age}</td>
              </tr>
            </tbody>
          </table>
        )
      })}
      <button onClick={handleLoad}>Get Report</button>
    </>
  )
}

export default App
