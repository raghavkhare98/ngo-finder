import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import Head from "next/head";
import { useRouter } from "next/router";
import { useEffect } from "react";
import { useState } from "react";
import styles from "../styles/ngolist.module.css"

const ngos = {
    "Waterloo": ["ngo1", "ngo2", "ngo3"],
    "Kitchener": ["ngo1", "ngo2", "ngo3"],
    "Cambridge": ["ngo1", "ngo2", "ngo3"],
    "Guelph": ["ngo1", "ngo2", "ngo3"]
}


export default function NgoList(){
    const router = useRouter()
    const [city, setCity] = useState(""); //used a state because we want to manage the state of city across re-renders
    //useEffect is used whenever we receive a query response and want to render the page on the basis of that
    //useEffect sort of delays the execution of the code until after the rendering has been done
    useEffect(()=>{
        if(!router.isReady) return;
    
        setCity(router.query.city || ""); 
    
    }, [router.isReady, router.query.city]); //this array defines when the useEffect should run. So whenever these values change, useEffect should execute
    
    return(
        
        <div className={styles.container}>
            <Head>
                <title>Connect | {city}</title>
            </Head>
            <Navbar />
            <main className={styles.list_content}>
                <ul>
                    {
                    city && ngos[city] ? ngos[city].map((ngo) => (
                        <li key={ngo}>
                            {ngo}
                        </li>
                    )) : <li>Loading NGOs...</li>}
                </ul>
            </main>
            <Footer />
        </div>
    )
}