from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import info as session_info


 #simple function to handle the temperature conversions
def temp_converter_calculator(x, y, z):
   
    if x == z:
         return put_markdown(f'Your tempeature is:`{y} {z}`')
    else:
        # for celsius conversions
        if x == "Celsius" and z == "Kelvin":
            output = y + 273.15
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x == "Celsius" and z == "Fahrenheit":
            output = y*9/5+32
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x == "Celsius" and z == "Rankine":
            output = (y - 491.67)*5/9
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x == "Celsius" and z == "Delisle":
            output = 100-(y*2/3)
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x == "Celsius" and z == "Newton":
            output = y*100/33
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        
            #for kelvin conversions
        if x == "Kelvin" and z == "Celsius":
            output = y - 273.15
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x == "Kelvin" and z == "Fahrenheit":
            output = y *9/5-496.7
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x == "Kelvin" and z == "Rankine":
            output = y *5/9
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x == "Kelvin" and z == "Delisle":
            output = 373.15 - (y*2/3)
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x == "Kelvin" and z == "Newton":
            output = y *5/4+273.15
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        
        #for fahrenheit conversions
        if x == "Fahrenheit" and z == "Celsius":
            output = (y-32)*5/9
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x == "Fahrenheit" and z == "Kelvin":
          output = (y + 459.67) * 5/9
          return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x == "Fahrenheit" and z == "Rankine":
            output = y - 459.67
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x == "Fahrenheit" and z == "Delisle":
            ouput = 212 -y*6/5
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x == "Fahrenheit" and z == "Newton":
            output = y*60/11+32
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        #for Rankine conversions
        if x== 'Rankine' and z == 'Celsius':
            output = (y +273.15)*9/5
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x== 'Rankine' and z == 'Fahrenheit':
            output = y + 459.67
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x== 'Rankine' and z == 'Kelvin':
            output = y*9/5
        if x == "Rankine" and z == 'Delisle':
            output = 671.67 - y*6/5
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x == "Rankine" and z == "Newton":
            output = y*60/11+491.67
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')  
        #for Delisle conversions
        if x == "Delisle" and z == "Celsius":
            output = (100-y)*3/2
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x == "Delisle" and z == "Fahrenheit":
            output = (212-y)*5/6
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x == "Delisle" and z == "Kelvin":
            output = (373.15-y)*3/2
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x == "Delisle" and z == "Rankine":
            output = (671.67 - y)*5/6
        if x == "Delisle" and z == "Newton":
            output = (33-y)*50/11
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        #for Newton Conversions
        if x == "Newton" and z == "Celsius":
            output = y* 33/100
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x == "Newton" and z == "Fahrenheit":
            output = (y-32)*11/60
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x == "Newton" and z == "Kelvin":
            output = (y-273.15)*33/100
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x == "Newton" and z == "Rankine":
            output = (y-491.67)*11/60
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
        if x == "Newton" and z == "Delisle":
            output = 33-y*11/50
            return put_markdown(f'Your temperature is: `{output:.2f} {z}`')
          

def temp_converter():

    """Simple temperature converter appplication using  PyWebIO
    https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature"""

    put_markdown('# Temperature converter')

    put_markdown(""" [Temperature Converter](https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature) is an easy way to convert units of temperature.
    Conversion is valid for Celsius, Kelvin, Fahrenheit, Rankine, Delisle, and Newton only """)

    put_markdown('## Temeperature conversion table')

    put_text('Celsius')
    put_table([
        ['From',  'Celsius'],
        ['Fahrenheit', '[°C] = ([°F] − 32) × ​5⁄9'],
        ['Kelvin', '[°C] = [K] − 273.15'],
        ['Rankine', '[°C] = ([°R] − 491.67) × ​5⁄9'],
        ['Delisle', '[°C] = 100 − [°De] × ​2⁄3'],
        ['Newton', 	'[°C] = [°N] × ​100⁄33'],
        ])
    
    put_text('Fahrenheit')
    put_table([
        ['From',  'Fahrenheit'],
        ['Celsius', '[°F] = [°C] × ​9⁄5 + 32'],
        ['Kelvin', '[°F] = [K] × ​9⁄5 − 459.67'],
        ['Rankine', '[°F] = [°R] − 459.67'],
        ['Delisle', '[°F] = 212 − [°De] × ​6⁄5'],
        ['Newton', 	'[°F] = [°N] × ​60⁄11 + 32'],
        ])
    put_text('Kelvin')
    put_table([
        ['From',  'Kelvin'],
        ['Fahrenheit', '[K] = ([°F] + 459.67) × ​5⁄9'],
        ['Celsius', '[K] = [°C] + 273.15'],
        ['Rankine', '[K] = [°R] × ​5⁄9'],
        ['Delisle', '[K] = 373.15 − [°De] × ​2⁄3'],
        ['Newton', 	'[K] = [°N] × ​100⁄33 + 273.15'],
        ])
    put_text('Rankine')
    put_table([
        ['From',  'Rankine'],
        ['Celsius', 	'[°R] = ([°C] + 273.15) × ​9⁄5'],
        ['Fahrenheit', '[°R] = [°F] + 459.67'],
        ['Kelvin', 	'[°R] = [K] × ​9⁄5'],
        ['Delisle',	'[°R] = 671.67 − [°De] × ​6⁄5'],
        ['Newton', 	'[°R] = [°N] × ​60⁄11 + 491.67'],
        ])
    put_text("Delisle")
    put_table([
         ['From', 'Delisle'],
         ['Celsius', '[°De] = (100 − [°C]) × ​3⁄2'],
         ['Fahrenheit','[°De] = (212 − [°F]) × ​5⁄6'],
         ['Kelvin', '[°De] = (373.15 − [K]) × ​3⁄2'],
         ['Rankine','[°De] = (671.67 − [°R]) × ​5⁄6'],
         ['Newton', '[°De] = (33 − [°N]) × ​50⁄11'],
    ])
    put_text("Newton")
    put_table([
        ['Celsius', '[°N] = [°C] × ​33⁄100'],
        ['Fahrenheit','[°N] = ([°F] − 32) × ​11⁄60'],
        ['Kelvin', 	'[°N] = ([K] − 273.15) × ​33⁄100'],
        ['Rankine', '[°N] = ([°R] − 491.67) × ​11⁄60'],
        ['Delisle', '[°N] = 33 − [°De] × ​11⁄50'],
    ])
    
    temp_units = ['Kelvin', 'Celsius', 'Fahrenheit', 'Rankine','Delisle','Newton']

    temp_info = input_group('Temperature converstion calculation', [
                  select(label='Select your Temperature unit', options=temp_units, value='Arial', name='input_temp_unit'), #label: Name of the button; value: The value when the user clicks the button
                  input("Enter the temperature value", type=NUMBER, name='temp_value'),
                  select(label='Select the Temperature unit you wish to convert to', options=temp_units, value='Arial', name='output_temp_unit'),
                  ])
    #calling the tempperature conversion that was defined earlier
    temp_converter_calculator(temp_info['input_temp_unit'], temp_info['temp_value'], temp_info['output_temp_unit'])

    put_markdown('The source code for this application can be found [here] ()')

  




    



if __name__ == "__main__":
    start_server(temp_converter, debug=True, port=80, cdn=False)

# #   http://localhost:80/
