import styles from "../styles/home.module.css"

export default function Navbar(){
    return(
        <header className={styles.navbar}>
            <span className={styles.gradient_text}><a href="/">Careconnect</a></span>
            <nav>
                <ul className={styles.nav_links}>
                    <li><a href="/">Home</a></li>
                    <li><a href="/cities">Cities</a></li>
                    
                </ul>
            </nav>
        </header>
    )
}