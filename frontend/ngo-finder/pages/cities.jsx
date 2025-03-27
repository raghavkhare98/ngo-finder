import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import Head from "next/head"
import styles from "../styles/cities.module.css"

export async function getServerSideProps(){
    try{
        const reponse = await fetch("http://0.0.0.0:8000/api/cities/");
        const cities = await reponse.json();
        return{
            props: {
                cities: cities
            }
        };
    } catch(error){
        return{
            props:{
                cities: []
            }
        };
    }
}

export default function Cities({ cities }){
    
    function capitalizeLetter(word){
        let splitStr = word.toLowerCase().split(' ');
        for(let i=0; i < splitStr.length; i++){
            splitStr[i] = splitStr[i].charAt(0).toUpperCase() + splitStr[i].substring(1);
        }
        return splitStr.join(' ');
    }

    return(
        <div className={styles.container}>
            <Head>
                <title>Careconnect | Cities</title>
            </Head>
            <Navbar />
            <main className={styles.content}>
                <h1 className={styles.title}>Select your city</h1>
                <div className={styles.city_list}>
                    <ul>
                        {cities.map((city, index) => {
                            let cityName = capitalizeLetter(city.city_name);
                            return <li key={index}>{cityName}</li>;
                        })}
                    </ul>
                </div>
            </main>
            <Footer />
        </div>
    )
}