//IGNORE THE COMMENTS AS I AM WRITING THEM FOR LEARNING PURPOSES

//we are using _app.jsx to keep styling persistent. Hence it is useful for common components like the navbar, footer, header, etc.
//this is also where we can add global css styling. Global css is styling for every page
//_app.jsx is like the parent component which will always be there and will provide any "global" styling to the current component
import "../styles/globals.css";

export default function MyApp({Component, pageProps}){ //here the component prop is the active page and pageProps are props for the active page
    return(
        <>
            <Component {...pageProps} />
        </>
    );
}