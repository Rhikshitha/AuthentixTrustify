import {useState} from "react"
import { useNavigate } from 'react-router-dom'

function Login(){
    const [email,setEmail] = useState("")
    const [password,setPassword] = useState("")
    const navigate = useNavigate();
    const URL = import.meta.env.VITE_API_URL
    async function callRegister(){
        try{
            const response = await fetch(URL+"user/login/",{
                method:"POST",
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ "email": email,"password":password })
            })
            const data  = await response.json()
            if(data.status){
                console.log(data)
                console.log(data.message)
                console.log("Navigating")
                navigate("/")

            }else{
                console.log(data.message)
            }
        }catch(err){
            console.log(err)
        }    
    }
    return <div>
        <h2>Login</h2>
        Email :
        <input  type="email"  onChange={(e)=>{setEmail(e.target.value)}}/><br/>
        Password : 
        <input type="password" onChange={(e)=>{setPassword(e.target.value)}}/><br/>
        <button onClick={callRegister}>Login</button>
    </div>
}

export default Login