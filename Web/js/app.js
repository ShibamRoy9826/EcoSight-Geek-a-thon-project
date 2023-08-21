let menuToggle = document.querySelector(".menuToggle");
let header = document.querySelector("header");

menuToggle.onclick = function () {
  header.classList.toggle("active");
};

//nav on scroll
let lastScrollTop = window.pageYOffset || document.documentElement.scrollTop;
let navbar = document.getElementById("navbar");

window.addEventListener(
  "scroll",
  function handleScroll() {
    const scrollTopPosition =
      window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTopPosition > lastScrollTop) {
      console.log("scrolling down");
      navbar.style.top = "-50px";
    } else if (scrollTopPosition < lastScrollTop) {
      console.log("scrolling up");
      navbar.style.top = "0";
    }
    lastScrollTop = scrollTopPosition <= 0 ? 0 : scrollTopPosition;
  },
  false
);
