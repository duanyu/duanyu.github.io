a = {
  "type": "object",
  "properties": {
    "reasoning": {
      "type": "string"
    },
    "pass": {
      "type": "boolean"
    }
  },
  "required": ["reasoning", "pass"],
  "additionalProperties": False
}
print(a)
