import React, {useState} from 'react'
import Autosuggest from 'react-autosuggest'

import './autocomplete.css'

const getSuggestionValue = suggestion => suggestion.title

const renderSuggestion = suggestion => (
    <div>
        {suggestion.title}
    </div>
)

export default function Autocomplete() {
    const [value, setValue] = useState('')
    const [suggestions, setSuggestions] = useState([])

    const onSuggestionsFetchRequested = ({value}) => {
        const inputValue = value.trim().toLowerCase();

        (async () => {
            const response = await fetch(
                '/api/search', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({input: inputValue})
                }
            )
            const json = await response.json()
            setSuggestions(json.data)
        }) ()
    }

    const onSuggestionsClearRequested = () => {
        setSuggestions([])
    }

    const inputProps = {
        placeholder: 'Search dataset',
        value,
        onChange: (e, {newValue}) => setValue(newValue)
    }

    return (
        <Autosuggest
            suggestions={suggestions}
            onSuggestionsFetchRequested={onSuggestionsFetchRequested}
            onSuggestionsClearRequested={onSuggestionsClearRequested}
            getSuggestionValue={getSuggestionValue}
            renderSuggestion={renderSuggestion}
            inputProps={inputProps}
        />
    )
}