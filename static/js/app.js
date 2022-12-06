// REMOVING MESSAGES
const alertWrapper = document.querySelector('.alert')
const alertClose = document.querySelector('.alert__close')

if (alertWrapper) {
    alertClose.addEventListener('click', () => {
        alertWrapper.style.display = 'none'
    })
}

// REMOVING TAGS
const tags = document.querySelectorAll('.deletePosition')

tags.forEach(tag => tag.addEventListener('click', (e) => {
    const tagID = e.target.dataset.tag
    const constructionID = e.target.dataset.construction
    
    fetch('http://127.0.0.1:8000/api/remove-tag/', {
        method:'DELETE',
        headers:{
            'Content-Type':'application/json'
        },
        body: JSON.stringify({'construction':constructionID, 'tag':tagID})
    })
    .then(response => response.json())
    .then(data => {
        e.target.closest('span').remove()
    })
}))

// CALCULATE TOTAL
const quantities = document.querySelectorAll('.data__quantity')
const totalEl = document.getElementById('total')
const measureUnits = document.querySelectorAll('.measure__units')
const measureUnitEl = document.getElementById('measure__unit')

const quantityArray = []

quantities.forEach(quantity => {
    quantityArray.push(parseInt(quantity.textContent));
})

const total = quantityArray.reduce((accumulator, value) => {
    return accumulator + value
}, 0).toFixed(2)

if (totalEl){totalEl.textContent = `${total.toString()}`}

const measureUnitsArray = []

measureUnits.forEach(el => {
    measureUnitsArray.push((el.textContent))
})

function allEqual(arr) {
    return new Set(arr).size == 1;
  }

if (allEqual(measureUnitsArray)) {
    measureUnitEl.textContent = `${measureUnitsArray[0]}`
}

// SORT BUTTON
const sortBtn = document.querySelector('.sort')
const dataContainer = document.querySelector('.data__container')
const dataFeatures = document.querySelectorAll('.data__features')


let sorted = false
function sortByQuantity(sorted = true) {
    const array = sorted ? quantityArray.slice().sort((a, b) => b - a) : quantityArray
    console.log(array);
  
    array.forEach(el => {
        dataFeatures.forEach(feature => {
            if(parseInt(feature.children[4].children[1].textContent) === el) {
                dataContainer.insertAdjacentElement('beforeend',feature);
            };
        });
    })
}


if(sortBtn) {
    sortBtn.addEventListener('click', function(e) {
        e.preventDefault()
        sortByQuantity(!sorted)
        sorted = !sorted
    })
}

// MENU BUTTON
const menuBtn = document.querySelector('.menu__btn')
const menuLinks = document.querySelectorAll('.header__menuItem')
const closeMenuBtn = document.querySelector('.close__menu-btn')

menuBtn.addEventListener('click', (e) => {
    menuLinks.forEach(link => link.classList.remove('close'))
    menuBtn.style.display = 'none'
    closeMenuBtn.style.display = 'block'
})

closeMenuBtn.addEventListener('click', (e) => {
    menuLinks.forEach(link => link.classList.add('close'))
    menuBtn.style.display = 'block'
    closeMenuBtn.style.display = 'none'
})

window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
        menuLinks.forEach(link => link.classList.add('close'))
        menuBtn.style.display = 'block'
        closeMenuBtn.style.display = 'none'
    }
})

window.addEventListener("resize", () => {
    if (window.innerWidth > 704) {
        menuLinks.forEach(link => link.classList.add('close'))
        menuBtn.style.display = 'none'
        closeMenuBtn.style.display = 'none'
    }
})

window.addEventListener("resize", () => {
    if (window.innerWidth <= 704 && closeMenuBtn.style.display === 'none') {        
        menuBtn.style.display = 'block'
        closeMenuBtn.style.display = 'none'
    }
})

// Change selection first item to selected
try {
    const options = document.getElementById('id_measure_unit_dropdown').children
    if (options) {
        options[0].remove();
    }
}    
catch {
    //pass
}
