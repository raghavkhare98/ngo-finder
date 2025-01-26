import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import Head from "next/head"
import styles from "../styles/cities.module.css"
import Link from "next/link";

const cities = ["Waterloo", "Kitchener", "Cambridge", "Guelph"]

export default function Cities({repo}){

    return(
        <div className={styles.container}>
            <Head>
                <title>Connect | Cities</title>
            </Head>
            <Navbar />
            <main className={styles.content}>
                <h1 className={styles.title}>Select your city</h1>
                <div className={styles.city_list}>
                    {cities.map((city => (
                        //we used / instead of \ because we would need to write \\ as a single \ would cause the escape character error
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