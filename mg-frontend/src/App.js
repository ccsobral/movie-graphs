 import React, {useState} from 'react'
// import Header from './Header'
import Autocomplete from './Autocomplete'
 import Body from './Body'
 import Footer from './Footer'

function App() {

    const [itemTitle, setItemTitle] = useState('')

    return (
        <div className="App">
            <header>
                <div className='Title'>
                    <h1 className='Title1'>Movie</h1>
                    <h1 className='Title2'>Graphs</h1>
                </div>
                <div className='SearchBar'>
                    <Autocomplete setTitle={setItemTitle}/>
                </div>
            </header>
            <Body title={itemTitle}/>
            <Footer />
        </div>
    )
}

export default App