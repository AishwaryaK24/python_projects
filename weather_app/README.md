This project returns the weather details of the city entered by the user.
It takes the weather data from OpenWeather website using the API key.

Unit Testing
The JSON response from the server includes a field called "cod".
If the city name is valid, then the cod value is 200.
If the city name is invalid, then the cod value is 404.
Other assert check could to check no response from the server i.e. a NULL buffer.