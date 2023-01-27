// Importar o módulo http
const http = require('http');

// URL da página
const url = 'https://www.4devs.com.br/gerador_de_pessoas';

// Fazer uma solicitação HTTP GET à URL
http.get(url, (response) => {
    // Declarar uma variável para armazenar os dados
    let data = '';
    
    // Quando os dados são recebidos, adicioná-los à variável "data"
    response.on('data', (chunk) => {
        data += chunk;
    });
    
    // Quando todos os dados são recebidos, mostrar os dados na tela
    response.on('end', () => {
        console.log(data);
    });
});


#Este código usa o módulo http do Node.js para fazer uma solicitação GET à URL especificada e armazenar os dados recebidos em uma variável. Ele, então, imprime esses dados na tela.

#No entanto, essa página utiliza um formato específico de dados, como por exemplo json, que para extrair esses dados é necessário um tratamento específico, como utilizar bibliotecas de terceiros como o cheerio ou o puppeteer para navegar pelos elementos da página e extrair os dados desejados.
