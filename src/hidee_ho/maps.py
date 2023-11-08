import plotly.graph_objects as go

STATE_ABBREVIATIONS = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "District of Columbia": "DC",
    "Florida": "FL",
    "Georgia": "GA",
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
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}


def valid_state(state: str) -> bool:
    """
    Check if a given state is valid.

    Args:
        state: A string representing a state.  Full name or abbreviation

    Returns:
        True if the state is valid, False otherwise.
    """
    state = state.strip()
    return (
        state.upper() in STATE_ABBREVIATIONS.values()
        or state.title() in STATE_ABBREVIATIONS
    )


def state_abbreviation(state: str) -> str:
    state = state.strip()

    if not valid_state(state):
        raise KeyError(f"{state} is not a State")

    if state.upper() in STATE_ABBREVIATIONS.values():
        return state.upper()
    else:
        state_name = state.title()
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
