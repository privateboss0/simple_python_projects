print ('*** SI UNIT MASS CONVERTER ***')

def convert_length(value, from_unit, to_unit):
  """Converts a length value from one SI unit to another."""

  if from_unit not in MASS_CONVERSIONS:
    raise ValueError(f"Invalid input unit: {from_unit}")

  if to_unit not in MASS_CONVERSIONS:
    raise ValueError(f"Invalid output unit: {to_unit}")

  base_value = value * MASS_CONVERSIONS[from_unit]
  converted_value = base_value / MASS_CONVERSIONS[to_unit]

  return converted_value

MASS_CONVERSIONS = {
    
        "kg": 1,
        "g": 0.001,
        "mg": 0.000001,
        "lb": 0.453592,
        "oz": 0.0283495
}

value = int(input('Enter the Mass you want to convert: '))  # Value to convert
from_unit = str(input('Enter the FROM UNIT in "kg","g","mg","lb","oz": '))  # Input unit
to_unit = str(input('Enter the OUTPUT UNIT in "kg","g","mg","lb","oz": '))  # Output unit

converted_value = convert_length(value, from_unit, to_unit)
print(f"{value} {from_unit} is EQUAL TO {converted_value:.2f} {to_unit}")