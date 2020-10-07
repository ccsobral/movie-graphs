import React from 'react'
import Autocomplete from './Autocomplete'

function Header() {
    return (
        <header>
            <div className='Title'>
                <h1 className='Title1'>Movie</h1>
                <h1 className='Title2'>Graphs</h1>
            </div>
            <div className='SearchBar'>
                <Autocomplete />
            </div>
        </header>
    )
}

export default Header