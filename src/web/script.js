document.addEventListener("DOMContentLoaded", function() {
    const tabButtons = document.querySelectorAll(".tab-button");
    const tabContents = document.querySelectorAll(".tab-content");

    tabButtons.forEach(button => {
        button.addEventListener("click", function() {
            const tabId = this.getAttribute("data-tab");
            tabContents.forEach(content => {
                content.classList.remove("active");
            });
            document.getElementById(tabId).classList.add("active");
        });
    });

    // Inicializar el slider
    var mySwiper = new Swiper('.swiper-container', {
        // Configuración del slider (puedes personalizarla)
        slidesPerView: 1,
        spaceBetween: 10,
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });

    // Mostrar la pestaña de inicio por defecto
    document.getElementById("home").classList.add("active");
});
