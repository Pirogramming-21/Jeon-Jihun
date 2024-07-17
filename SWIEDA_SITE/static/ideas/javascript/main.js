document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.increase-button, .decrease-button').forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const ideaId = this.dataset.ideaId; 
            const action = this.classList.contains('increase-button') ? 'increase' : 'decrease'; 

            fetch(`/interest/${ideaId}/${action}/`,{
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                },
            })
            .then(response => response.json())
            .then(data => {
                const interestValue = this.parentElement.querySelector('.interest-value');
                interestValue.textContent = data.interest;
            });
        
        });
    });
});