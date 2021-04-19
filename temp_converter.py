from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import info as session_info


 #simple function to handle the temperature conversions
def temp_converter_calculator(x, y, z):
   
    if x == z:
         return put_markdown(f'Your tempeature is:`{y} {z}`')
    else:
        if x == "Celsius" and z == "Kelvin":
            output = y + 273.15
            return put_markdown(f'Your temperature is: `{output} {z}`')
        if x == "Celsius" and z == "Fahrenheit":
            output = y*9/5+32
            return put_markdown(f'your temperature is: `{output} {z}`')

        if x == "Kelvin" and z == "Celsius":
            output = y - 273.15
            return put_markdown(f'your temperature is: `{output} {z}`')
        if x == "Kelvin" and z == "Fahrenheit":
            output = y *9/5-496.7
            return put_markdown(f'your temperature is: `{output} {z}`')

        if x == "Fahrenheit" and z == "Celsius":
            output = (y-32)*5/9
            return put_markdown(f'your temperature is: `{output} {z}`')
        if x == "Fahrenheit" and z == "Kelvin":
          output = (y + 459.67) * 5/9
          return put_markdown(f'your temperature is: `{output} {z}`')

def temp_converter():

    """Simple temperature converter appplication using  PyWebIO
    https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature"""

    put_markdown('# Temperature converter')

    put_markdown(""" [Temperature Converter](https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature) is an easy way to convert units of temperature.
    Conversion is valid for Celsius, Kelvin and Fahrenheitt only '""")

    put_markdown('## Temeperature conversion table')

    put_text('Celsius')
    put_table([
        ['From',  'Celsius'],
        ['Fahrenheit', '[°C] = ([°F] − 32) × ​5⁄9'],
        ['Kelvin', '[°C] = [K] − 273.15']
        ])
    put_text('Fahrenheit')
    put_table([
        ['From',  'Fahrenheit'],
        ['Celsius', '[°F] = [°C] × ​9⁄5 + 32'],
        ['Kelvin', '[°F] = [K] × ​9⁄5 − 459.67']
        ])
    put_text('Kelvin')
    put_table([
        ['From',  'Kelvin'],
        ['Fahrenheit', 	'[K] = ([°F] + 459.67) × ​5⁄9'],
        ['Celsius', '[K] = [°C] + 273.15']
        ])
   
    temp_units = ['Kelvin', 'Celsius', 'Fahrenheit']

    temp_info = input_group('Temperature converstion calculation', [
                  select(label='Select your Temperature unit', options=temp_units, value='Arial', name='input_temp_unit'), #label: Name of the button; value: The value when the user clicks the button
                  input("Enter the temperature value", type=NUMBER, name='temp_value'),
                  select(label='Select the Temperature unit you wish to convert to', options=temp_units, value='Arial', name='output_temp_unit'),
                  ])
    #callling the tempperature conversion that was defined earlier
    temp_converter_calculator(temp_info['input_temp_unit'], temp_info['temp_value'], temp_info['output_temp_unit'])

    put_markdown('The source code for this application can be found [here] ()')

  




    



if __name__ == "__main__":
    temp_converter()


# #   http://localhost:80/