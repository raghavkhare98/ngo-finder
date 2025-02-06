import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import Head from "next/head";
import { useRouter } from "next/router";
import { useEffect } from "react";
import { useState } from "react";
import styles from "../styles/ngolist.module.css"

export default function NgoList(){
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
        
        <div className={styles.container}>
            <Head>
                <title>Connect | {city}</title>
            </Head>
            <Navbar />
            <main className={styles.list_content}>
                <ul>
                    {ngos
                    .filter((ngo) => ngo.city_name === city)
                    .map((ngo) => (
                        <li key={ngo.id}>
                            <h5>{ngo.ngo_name}</h5>
                        </li>
                    ))}
                </ul>
            </main>
            <Footer />
        </div>
    )
}