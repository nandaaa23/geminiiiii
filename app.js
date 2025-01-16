function generateHoroscope() {
    const zodiac = document.getElementById("zodiac").value;
  
    fetch('http://localhost:5000/generate_horoscope', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ zodiac: zodiac })
    })
    .then(response => response.json())
    .then(data => {
      if (data.horoscope) {
        document.getElementById('horoscope-result').innerText = data.horoscope;
      } else {
        document.getElementById('horoscope-result').innerText = "Sorry, something went wrong. Please try again.";
      }
    })
    .catch(error => {
      document.getElementById('horoscope-result').innerText = "Error fetching horoscope. Please try again.";
      console.error('Error fetching horoscope:', error);
    });
  }
  