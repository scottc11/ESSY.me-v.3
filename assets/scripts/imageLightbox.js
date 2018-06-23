


// Open the Modal
function openModal(path) {
  document.getElementById('myModal').style.display = "block";
  $('#modal-image').attr('src', path);
}

// Close the Modal
function closeModal() {
  document.getElementById('myModal').style.display = "none";
}

// particlesJS.load('particles-js', './static/particlesConfig.json', function() {
//   console.log('callback - particles.js config loaded');
// });
