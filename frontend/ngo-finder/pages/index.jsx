import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import styles from "../styles/home.module.css";
import Head from "next/head";

export default function Home(){
    
    function onExploreButtonClick(){
        const location="/cities"
        window.open(location, "_self")   
    }

    return(
        <div className={styles.container}>
            <Head>
                <title>Connect | Home</title>
            </Head>
            <Navbar />
            <main className={styles.hero}>
                <h1>Welcome to CareConnect</h1>
                <p>Find non-governemnts and their events near you in Ontario</p>
                <button className={styles.btn_primary} onClick={onExploreButtonClick}>Explore cities</button>
            </main>
            <Footer />
        </div>
    )
}