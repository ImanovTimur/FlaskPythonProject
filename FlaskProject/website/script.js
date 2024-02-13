function rate(stars) {
    // Clear previous selections
    document.querySelectorAll('.star').forEach(star => star.classList.remove('selected'));
    
    // Mark selected stars
    for (let i = 0; i < stars; i++) {
        document.querySelectorAll('.star')[i].classList.add('selected');
    }
    
    // Store selected rating in hidden input field (optional)
    document.getElementById('rating').value = stars;
}
