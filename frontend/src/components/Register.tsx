import {useState} from "react"

function Register(){
    const [email,setEmail] = useState("")
    const [password,setPassword] = useState("")
    const URL = import.meta.env.VITE_API_URL
    async function callRegister(){
        try{
            const response = await fetch(URL+"user/register/",{
                method:"POST",
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ "email": email,"password":password })
            })
            const data  = await response.json()
            if(data.status=="success"){
                console.log(data.message)
            }else{
                console.log(data.message)
            }
        }catch(err){
            console.log(err)
        }    
    }
    return <div>
        <h2>Register</h2>
        <label htmlFor="email">Email : </label>
        <input id="email" type="tel" onChange={(e)=>{setEmail(e.target.value)}} /><br/><br />
        <label htmlFor="password">Password : </label>
        <input id="password" type="password" onChange={(e)=>{setPassword(e.target.value)}} /><br/><br />
        <button onClick={callRegister}>Register</button>
    </div>
}

export default Register