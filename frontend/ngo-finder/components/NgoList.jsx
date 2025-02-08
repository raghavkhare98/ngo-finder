import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import Head from "next/head";
import styles from "../styles/ngolist.module.css";

export default function NgoList({city, ngos}){
return(
        
    <div className={styles.container}>
        <Head>
            <title>Careconnect | {city || ""}</title>
        </Head>
        <Navbar />
        <main className={styles.list_content}>
            {city ? <h2>NGOs in {city}</h2> : <h2>All NGOs</h2>}
            <ul>
                {city ? 
                ngos
                .filter((ngo) => ngo.city_name === city)
                .map((ngo) => (
                    <li key={ngo.id}>
                        <h4>{ngo.ngo_name}</h4>
                    </li>
                )) : 
                ngos.map((ngo) => (
                    <li key={ngo.id}>
                        <h4>{ngo.ngo_name}</h4>
                    </li>
                ))}
            </ul>
        </main>
        <Footer />
    </div>
)}