// Get all tabs
const tabs = document.querySelectorAll('.tabs ul li');

tabs.forEach(tab => {
    tab.addEventListener('click', function () {
        // Remove 'is-active' class from all tabs
        tabs.forEach(tab => tab.classList.remove('is-active'));

        // Add 'is-active' class to the clicked tab
        this.classList.add('is-active');

        // Get the target tab content ID
        const target = this.getAttribute('data-tab-id');

        // Hide all tab content
        document.querySelectorAll('.tab-content').forEach(content => {
            content.classList.remove('active');
        });

        // Show the clicked tab content
        document.getElementById(target).classList.add('active');
    });
});