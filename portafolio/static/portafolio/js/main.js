const menuToggle = document.querySelector(".menu-toggle");
const siteNav = document.querySelector("#site-nav");

if (menuToggle && siteNav) {
    const setMenuOpen = (isOpen) => {
        menuToggle.setAttribute("aria-expanded", String(isOpen));
        menuToggle.setAttribute("aria-label", isOpen ? "Cerrar menú" : "Abrir menú");
        siteNav.classList.toggle("is-open", isOpen);
    };

    menuToggle.addEventListener("click", () => {
        const isExpanded = menuToggle.getAttribute("aria-expanded") === "true";
        setMenuOpen(!isExpanded);
    });

    siteNav.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => setMenuOpen(false));
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape" && menuToggle.getAttribute("aria-expanded") === "true") {
            setMenuOpen(false);
            menuToggle.focus();
        }
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

document.querySelectorAll("[data-copy-email]").forEach((copyButton) => {
    copyButton.addEventListener("click", async () => {
        const status = document.querySelector("[data-copy-status]");

        if (!navigator.clipboard) {
            status.textContent = "No se pudo copiar. Selecciona el correo para copiarlo.";
            return;
        }

        try {
            await navigator.clipboard.writeText(copyButton.dataset.copyEmail);
            status.textContent = "Correo copiado.";
        } catch {
            status.textContent = "No se pudo copiar. Selecciona el correo para copiarlo.";
        }
    });
});
