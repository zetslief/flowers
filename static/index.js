fetch('http://localhost:9874//flowers')
  .then(response => response.json())
  .then(flowers => {
    const flowersDiv = document.getElementById('flowers');
    flowers.forEach(flower => {
      const p = document.createElement('p');
      p.innerText = `${flower.name}, ${flower.image_path}`;
      flowersDiv.appendChild(p);
    });
  });