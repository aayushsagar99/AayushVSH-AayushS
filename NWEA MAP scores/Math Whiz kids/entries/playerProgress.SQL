{
  "name": "PlayerProgress",
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "Name of the player"
    },
    "avatar": {
      "type": "string",
      "description": "Avatar emoji chosen by the player"
    },
    "current_level": {
      "type": "number",
      "default": 1,
      "description": "Current level the player is on"
    },
    "total_stars": {
      "type": "number",
      "default": 0,
      "description": "Total stars earned"
    },
    "total_coins": {
      "type": "number",
      "default": 0,
      "description": "Total coins earned"
    },
    "levels_completed": {
      "type": "array",
      "items": {
        "type": "number"
      },
      "description": "List of completed level numbers"
    },
    "level_stars": {
      "type": "object",
      "description": "Stars earned per level"
    }
  },
  "required": [
    "player_name"
  ]
}