import plotly.graph_objects as go

STATE_ABBREVIATIONS = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Canal Zone": "CZ",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "District of Columbia": "DC",
    "Florida": "FL",
    "Georgia": "GA",
    "Guam": "GU",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Puerto Rico": "PR",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virgin Islands": "VI",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}


def state_abbreviation(state: str) -> str:
    state = state.strip()
    
    state_name = state.capitalize()

    if state.upper() in STATE_ABBREVIATIONS.values():
        return state.upper()
    elif state_name not in STATE_ABBREVIATIONS:
        raise KeyError(f"{state_name} is not a State")
    else:
        return STATE_ABBREVIATIONS[state_name]


def list_abbreviations(states: list[str]) -> list[str]:
    _states = []

    if isinstance(states, str):
        _states = [state_abbreviation(states)]
    else:
        _states = [state_abbreviation(state) for state in states]
    return _states


def mapper(states: list[str]) -> go.Figure:
    _states = list_abbreviations(states)
    color = [1 for s in _states]

    fig = go.Figure(
        data=go.Choropleth(
            locations=_states,  # Spatial coordinates
            z=color,  # Data to be color-coded
            locationmode="USA-states",  # set of locations match entries in `locations`
            colorscale="Reds",
        )
    )

    fig.update_layout(
        title_text="Operation hidee-ho is a go!",
        geo_scope="usa",  # limite map scope to USA
    )
    return fig
