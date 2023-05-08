const FLOWERS_URL = document.location.origin + '/flowers';
const CARD_BUY_URL = document.location.origin + '/card/buy';

console.log(FLOWERS_URL);
console.log(CARD_BUY_URL);

mainView();
cardView();

function mainView() {
    const flowersDiv = document.getElementById('flowers');
    const card = document.getElementById('card');

    const homeButton = document.getElementById('homeButton');
    const cardButton = document.getElementById('cardButton');

    homeButton.addEventListener('click', function() {
      flowersDiv.style.display = 'block';
      card.setAttribute('hidden', 'hidden');
      fetch(FLOWERS_URL)
        .then(response => response.json())
        .then(flowers => {
            flowers.forEach(flower => {
              const p = document.createElement('p');
              p.innerText = `${flower.name}, ${flower.image_path}`;
              flowersDiv.appendChild(p);
            });
          });
    });

    cardButton.addEventListener('click', function() {
      flowersDiv.style.display = 'none';
      card.removeAttribute('hidden');
    });
}


function cardView() {
  console.log("Card view initialization");
  const form = document.getElementById('cardForm');
  const firstName = document.getElementById('firstName'); 
  const lastName = document.getElementById('lastName'); 
  const email = document.getElementById('email'); 
  const phone = document.getElementById('phone'); 
  const address = document.getElementById('address'); 
  const buyCard = document.getElementById('buyCard'); 
  form.onsubmit = function(_) {
    const data = {
      firstName: form.elements.firstName.value,
      lastName: form.elements.lastName.value,
      email: form.elements.email.value,
      phone: form.elements.phone.value,
      address: form.elements.address.value,
    };
    console.log(JSON.stringify(data));
    return false;
  };
}
