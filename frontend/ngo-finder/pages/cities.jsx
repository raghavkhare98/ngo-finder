import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import Head from "next/head"
import styles from "../styles/cities.module.css"
import Link from "next/link";

const cities = ["Waterloo", "Kitchener", "Cambridge", "Guelph"]

export default function Cities({repo}){

    /*
    WILL WORK ON THIS WHEN WE ADD MORE CITIES
    
    async function getCityName(){
        const response = await fetch("http://0.0.0.0:8000/api/cities/");
        const data = await response.json();
        console.log(data);
    }
    const cityNames = getCityName().then()*/
    return(
        
        <div className={styles.container}>
            <Head>
                <title>Careconnect | Cities</title>
            </Head>
            <Navbar />
            <main className={styles.content}>
                <h1 className={styles.title}>Select your city</h1>
                <div className={styles.city_list}>
                    {cities.map((city => (
                        <button><Link key={city} href={`/ngo-list?city=${city}`}>  
                            {city}
                        </Link></button>
                    )))}
                </div>
            </main>
            <Footer />
        </div>
    )
}