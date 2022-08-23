#whenever you import a module, python executes the code in the module
import main



def test_check_api():
    # city=main.input
    data=main.get_weather_data("Pune")   
    assert data=