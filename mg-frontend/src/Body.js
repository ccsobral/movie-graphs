import React, { useState, useEffect} from 'react'
import Plot from 'react-plotly.js'

function Body({title}) {

    const [data, setData] = useState()
    const [layout, setLayout] = useState()

    useEffect(() => {
        (async () => {
            const response = await fetch('/api/title/'+title)
            const json = await response.json()
            setData(json.data)
            setLayout(json.layout)
        }
        )()
    }, [title]
    )

    let foo = <h1>Search for a title!</h1>
    if (title) {
        foo = <div>
                <h1>{title}</h1>
                <Plot data={data} layout={layout}/>
            </div>
    }

    return (
        <div className='Body'>
            {foo}
        </div>
    )
}

export default Body