#whenever you import a module, python executes the code in the module
import main


def test_check_api():
    print(__name__)
    # city=main.input
    data=main.get_weather_data("Ikebukuro")   
    print(data['cod'])
    #assert raises an error if the below condition is false
    assert data['cod']==200