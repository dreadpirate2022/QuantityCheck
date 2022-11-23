// PAGINATION
const searchForm = document.getElementById('searchForm')
const pageLinks = document.querySelectorAll('.pagination__btn')

if (searchForm) {
    pageLinks.forEach(link => link.addEventListener('click', function(e) {
        e.preventDefault();
        
        const page = this.dataset.page
        
        searchForm.innerHTML += `<input value=${page} name='page' hidden />`
        searchForm.submit()
    })
)}

