import {useState,useEffect} from "react"
import {getCSRFToken,getSessionId } from "../utils/GetAuth"

function Home(){
    const URL = import.meta.env.VITE_API_URL
    async function getHomePageData(){
        try{
            const response = await fetch(URL+"",{
                method : "GET",
                headers : {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken(),  
                    'Authorization': `Bearer ${getSessionId()}`, 
                },
            })
            const data = await response.json()
            console.log(data)
        }catch(e){
            console.log(e)
        }
    }
    useEffect(()=>{
        getHomePageData()
    },[])
    return <div>
        <h2>Home</h2>
    </div>
}

export default Home