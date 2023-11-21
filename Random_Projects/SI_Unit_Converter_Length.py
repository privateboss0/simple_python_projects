#wip
print ('*** SI UNIT LENGTH CONVERTER ***')

def convert_length(value, from_unit, to_unit):
  """Converts a length value from one SI unit to another."""

  if from_unit not in LENGTH_CONVERSIONS:
    raise ValueError(f"Invalid input unit: {from_unit}")

  if to_unit not in LENGTH_CONVERSIONS:
    raise ValueError(f"Invalid output unit: {to_unit}")

  base_value = value * LENGTH_CONVERSIONS[from_unit]
  converted_value = base_value / LENGTH_CONVERSIONS[to_unit]

  return converted_value

LENGTH_CONVERSIONS = {
    "m": 1,
    "cm": 0.01,
    "mm": 0.001,
    "km": 1000,
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144
}

value = int(input('Enter the Length you want to convert: '))  # Value to convert
from_unit = str(input('Enter the FROM UNIT in "m","cm","mm","km","in","ft","yd": '))  # Input unit
to_unit = str(input('Enter the OUTPUT UNIT in "m","cm","mm","km","in","ft","yd": '))  # Output unit

converted_value = convert_length(value, from_unit, to_unit)
print(f"{value} {from_unit} is EQUAL TO {converted_value} {to_unit}")
