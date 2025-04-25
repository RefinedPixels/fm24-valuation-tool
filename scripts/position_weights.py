# Attribute weights by position
# You can expand this with more detailed role-based logic

POSITION_WEIGHTS = {
    "ST": {
        "Finishing": 1.5,
        "Composure": 1.3,
        "Off the Ball": 1.2,
        "Acceleration": 1.2,
        "Pace": 1.0,
    },
    "CB": {
        "Tackling": 1.5,
        "Marking": 1.3,
        "Positioning": 1.3,
        "Jumping Reach": 1.2,
        "Strength": 1.0,
    },
    "CM": {
        "Passing": 1.4,
        "Vision": 1.3,
        "Work Rate": 1.2,
        "First Touch": 1.2,
        "Stamina": 1.0,
    },
    "GK": {
        "Reflexes": 1.5,
        "Handling": 1.4,
        "Positioning": 1.2,
        "One on Ones": 1.3,
        "Aerial Reach": 1.0,
    }
}
