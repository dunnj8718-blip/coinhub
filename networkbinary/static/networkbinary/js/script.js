
window.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('modal');
    const closeBtn = document.querySelector('.close-btn');
  
    // Show modal when page loads
    modal.style.display = 'block';
  
    // Close modal on button click
    closeBtn.addEventListener('click', () => {
      modal.style.display = 'none';
    });
  
    // Optional: close when clicking outside modal content
    window.addEventListener('click', (e) => {
      if (e.target === modal) {
        modal.style.display = 'none';
      }
    });
  });
  