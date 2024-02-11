document.getElementById('revealButton').addEventListener('click', function() {
  var messageContainer = document.getElementById('messageContainer');
  if (messageContainer.classList.contains('hidden')) {
      messageContainer.classList.remove('hidden');
  } else {
      messageContainer.classList.add('hidden');
  }
});
