import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import styles from "../styles/custom404.module.css";

export default function Custom404(){
    return(
        <div className={styles.container}>
        <Navbar />
        <div className={styles.content}>
            <h1>Oops! This page was not found..</h1>
            <h2>Click on the 'Home' button to go back</h2>
        </div>
        <Footer />
        </div>
    )
}