const https = require('https');
const url = 'https://www.4devs.com.br/gerador_de_pessoas';
const postmanUrl = 'https://api.getpostman.com/collections';
const postmanKey = 'your_postman_api_key';

https.get(url, (response) => {
    let data = '';
    response.on('data', (chunk) => {
        data += chunk;
    });
    response.on('end', () => {
        // fazendo o parse para obter os dados em json
        let jsonData = JSON.parse(data);
        // criando o objeto para enviar via postman
        let postData = {
            "collection": {
                "name": "Nome da coleção",
                "requests": [
                    {
                        "name": "Nome da requisição",
                        "url": url,
                        "method": "GET",
                        "data": jsonData
                    }
                ]
            }
        };
        // configurações da requisição post
        let options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Api-Key': postmanKey
            }
        };
        // enviando os dados para o postman
        let req = https.request(postmanUrl, options, (res) => {
            console.log(`statusCode: ${res.statusCode}`);
            res.on('data', (d) => {
                process.stdout.write(d);
            });
        });
        req.write(JSON.stringify(postData));
        req.end();
    });
});

### 
Este código usa o módulo https do Node.js para fazer uma solicitação GET à URL especificada e armazenar os dados recebidos em uma variável. Em seguida, ele faz o parse dos dados para o formato JSON. Depois disso, ele cria um objeto para enviar os dados para o Postman via uma requisição POST. É necessário informar sua chave de API do Postman e configurar a url da coleção no Postman.

Obs: É importante notar que essa página não tem um endpoint para retornar um json, logo é necessário utilizar uma biblioteca de terceiros como o cheerio ou o puppeteer para navegar pelos elementos da página e extrair os dados desejados e tratá-los para o formato json. ###
