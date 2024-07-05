// gallery.js
const gallery = document.querySelector('.gallery-logo');
const items = document.querySelectorAll('.gallery-item');
const prevButton = document.querySelector('.gallery-control.prev');
const nextButton = document.querySelector('.gallery-control.next');
let currentIndex = 0;

function updateGallery() {
    const itemWidth = items[0].clientWidth;
    gallery.style.transform = `translateX(${-currentIndex * itemWidth}px)`;
}

prevButton.addEventListener('click', () => {
    currentIndex = (currentIndex > 0) ? currentIndex - 1 : items.length - 1;
    updateGallery();
});

nextButton.addEventListener('click', () => {
    currentIndex = (currentIndex < items.length - 1) ? currentIndex + 1 : 0;
    updateGallery();
});

// Auto slide functionality (optional)
setInterval(() => {
    nextButton.click();
}, 3000); // Change slides every 3 seconds