var xhr = new XMLHttpRequest();
xhr.open('GET', 'https://example.com/data', true);
xhr.onload = function() {
  if (xhr.status === 200) {
    var data = JSON.parse(xhr.responseText);
    // Faça algo com os dados aqui
  }
};
xhr.send();
