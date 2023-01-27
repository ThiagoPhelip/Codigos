const request = require("request");
const location = "New York";

request(`https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=YOUR_API_KEY`, function (error, response, body) {
    if (error) {
        console.log("Error: " + error);
        return;
    }

    let data = JSON.parse(body);
    let waterTemperature = data.main.temp - 273.15; // Convert Kelvin to Celsius
    console.log(`A temperatura da água em ${location} é de ${waterTemperature}ºC`);
});


#Este exemplo usa uma biblioteca chamada "request" para fazer uma solicitação à uma API de tempo que retorna a temperatura da água em uma determinada localização Note que é necessário adicionar uma chave de API válida para acessar a API do OpenWeatherMap.
Além disso, esse exemplo considera que a temperatura da água na localização especificada é a mesma que a temperatura do ar, mas em algumas localizações a temperatura da água pode ser diferente, então é necessário fazer as devidas adaptações.

Esse código irá imprimir a temperatura da água em Celsius na localização especificada (no exemplo, Nova York). Ele pode ser modificado para retornar a temperatura em outras unidades, ou para obter temperaturas de água em outras localizações.#
