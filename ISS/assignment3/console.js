// Format date to UTC YYYY-MM-DD HH:MM:SS
function formatDate(date) {
    return date.getUTCFullYear() + '-' +
           String(date.getUTCMonth() + 1).padStart(2, '0') + '-' +
           String(date.getUTCDate()).padStart(2, '0') + ' ' +
           String(date.getUTCHours()).padStart(2, '0') + ':' +
           String(date.getUTCMinutes()).padStart(2, '0') + ':' +
           String(date.getUTCSeconds()).padStart(2, '0');
}

// Determine element type
function getElementType(element) {
    if (element.classList.contains('profile-image')) return 'profile-image';
    if (element.classList.contains('gallery-item')) return 'gallery-image';
    if (element.classList.contains('nav-content')) return 'navigation';
    if (element.classList.contains('achievement-card')) return 'achievement-card';
    if (element.classList.contains('skill-tag')) return 'skill-tag';
    if (element.classList.contains('interest-card')) return 'interest-card';
    if (element.classList.contains('cv-button')) return 'download-button';
    if (element.classList.contains('timeline-content')) return 'timeline-item';
    if (element.classList.contains('gallery-caption')) return 'gallery-caption';
    if (element.classList.contains('quality-tag')) return 'quality-tag';
    // Add text analyzer elements
    if (element.id === 'textInput') return 'text-input-area';
    if (element.closest('.analyzer-container button')) return 'analyze-button';
    if (element.closest('#results')) return 'analysis-results';
    if (element.closest('.result-section')) return 'result-section';
    return element.tagName.toLowerCase();
}

// Track clicks
document.addEventListener('click', function(event) {
    console.log(`${formatDate(new Date())} , click , ${getElementType(event.target)}`);
});

// Track views using Intersection Observer
const viewObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            console.log(`${formatDate(new Date())} , view , ${getElementType(entry.target)}`);
            viewObserver.unobserve(entry.target); // Only log first view
        }
    });
}, {
    threshold: 0.5
});

// Initialize view tracking
document.addEventListener('DOMContentLoaded', function() {
    const elementsToTrack = [
        '.profile-card',
        '.gallery-item',
        '.achievement-card',
        '.skill-category',
        '.interest-card',
        '.timeline-content',
        // Add text analyzer elements to track
        '#text-analyzer',
        '.analyzer-container',
        '#results',
        '.result-section'
    ];

    elementsToTrack.forEach(selector => {
        document.querySelectorAll(selector).forEach(element => {
            viewObserver.observe(element);
        });
    });
});

// Additional tracking for text analyzer interactions
document.addEventListener('DOMContentLoaded', function() {
    const textInput = document.getElementById('textInput');
    if (textInput) {
        // Track when user starts typing
        textInput.addEventListener('focus', function() {
            console.log(`${formatDate(new Date())} , view , text-input-area`);
        });

        // Track when analysis is performed
        const analyzeButton = textInput.closest('.analyzer-container').querySelector('button');
        if (analyzeButton) {
            analyzeButton.addEventListener('click', function() {
                console.log(`${formatDate(new Date())} , click , analyze-button`);
            });
        }
    }
});