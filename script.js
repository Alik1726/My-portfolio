// script.js
document.addEventListener('DOMContentLoaded', function() {
    var topLink = document.querySelector('footer a[href="#top"]');
    if (topLink) {
      topLink.addEventListener('click', function(e) {
        e.preventDefault();
        document.getElementById('top').scrollIntoView({ behavior: 'smooth' });
      });
    }
  });
window.addEventListener('load', () => {
    const skillProgressBars = document.querySelectorAll('.skill-progress');
    skillProgressBars.forEach(bar => {
      const width = bar.style.width;
      bar.style.width = '0'; // Reset
      setTimeout(() => {
        bar.style.width = width; // Animate to real width
      }, 300);
    });
  });
  