document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll('.dropdown-submenu > a').forEach(function (element) {
    element.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();

      const parent = this.parentElement;

      // Fecha outros submenus
      document.querySelectorAll('.dropdown-submenu').forEach(function (submenu) {
        if (submenu !== parent) {
          submenu.classList.remove('show');
        }
      });

      // Alterna o submenu atual
      parent.classList.toggle('show');
    });
  });
});
