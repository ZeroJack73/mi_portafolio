const menuToggle = document.querySelector(".menu-toggle");
const siteNav = document.querySelector("#site-nav");

if (menuToggle && siteNav) {
    menuToggle.addEventListener("click", () => {
        const isExpanded = menuToggle.getAttribute("aria-expanded") === "true";
        menuToggle.setAttribute("aria-expanded", String(!isExpanded));
        siteNav.classList.toggle("is-open", !isExpanded);
    });
}

document.querySelectorAll("[data-filter]").forEach((filterButton) => {
    filterButton.addEventListener("click", () => {
        const filter = filterButton.dataset.filter;

        document.querySelectorAll("[data-filter]").forEach((button) => {
            const isSelected = button === filterButton;
            button.classList.toggle("is-selected", isSelected);
            button.setAttribute("aria-pressed", String(isSelected));
        });

        document.querySelectorAll("[data-category]").forEach((card) => {
            card.hidden = filter !== "todos" && card.dataset.category !== filter;
        });
    });
});

const currentYear = document.querySelector("[data-current-year]");

if (currentYear) {
    currentYear.textContent = new Date().getFullYear();
}
