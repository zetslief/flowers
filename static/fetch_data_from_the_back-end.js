fetch('http://localhost:5000/flowers')
  .then(response => response.json())
  .then(data => console.log(data))
