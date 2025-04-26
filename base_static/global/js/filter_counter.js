const filters = document.querySelectorAll(".filter-checkbox")
const filterCount = document.querySelector('.count-filters')

function updateFilterCount() {
    const selectedFilters = document.querySelectorAll('.filter-checkbox:checked');

    if (selectedFilters.length > 0) {
        filterCount.style.display = 'flex';
    } else {
        filterCount.style.display = 'none';
    }
    
    filterCount.textContent = selectedFilters.length;
}

filters.forEach(filter => {
    filter.addEventListener("change", () => {
        updateFilterCount();
    });
});

updateFilterCount();