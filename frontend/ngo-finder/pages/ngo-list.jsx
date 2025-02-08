import NgoList from "../components/NgoList";
import { useRouter } from "next/router";
import { useEffect } from "react";
import { useState } from "react";

export default function NgoListing(){
    const router = useRouter()
    const [city, setCity] = useState(""); 
    const [ngos, setNgos] = useState([]);
    useEffect(()=>{
        if(!router.isReady) return;
    
        setCity(router.query.city || ""); 
    
    }, [router.isReady, router.query.city]); 
    
    useEffect(() => {
        fetch('http://0.0.0.0:8000/api/ngos/')
        .then((response) => response.json())
        .then((data) => setNgos(data))
    }, [])

    return(
        <NgoList city={city} ngos={ngos}/>
    )
    
}