fetch('http://localhost:9874//flowers')
  .then(response => response.json())
  .then(data => console.log(data))

