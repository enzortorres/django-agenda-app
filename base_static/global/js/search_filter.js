const filter_icon = document.getElementById("filter-icon");
const close_filter = document.getElementById("close-filter");
const overlay = document.getElementById("overlay");
const filter = document.querySelector(".filter");
let isOpen = false;

function openFilter() {
    filter.style.right = "0px";
    overlay.classList.add("active");
    isOpen = true;
}

function closeFilter() {
    filter.style.right = "-310px";
    overlay.classList.remove("active");
    isOpen = false;
}

filter_icon.addEventListener("click", () => {
    if (isOpen) {
        closeFilter();
    } else {
        openFilter();
    }
})

overlay.addEventListener("click", () => {
    closeFilter();
})

close_filter.addEventListener("click", () => {
    closeFilter();
})