//main header
let header = document.querySelector("header");

var hamburger = document.querySelector(".hamburger");
hamburger.addEventListener("click", function () {
  hamburger.classList.toggle("is-active");
  header.classList.toggle("active");
});

//nav on scroll
let lastScrollTop = window.pageYOffset || document.documentElement.scrollTop;
let navbar = document.getElementById("navbar");

window.addEventListener(
  "scroll",
  function handleScroll() {
    const scrollTopPosition =
      window.pageYOffset || document.documentElement.scrollTop;
    if (700 < window.innerWidth < 880) {
      if (scrollTopPosition > lastScrollTop) {
        navbar.style.top = "-80px";
      } else if (scrollTopPosition < lastScrollTop) {
        navbar.style.top = "0";
      }
    } else {
      if (scrollTopPosition > lastScrollTop) {
        navbar.style.top = "-50px";
      } else if (scrollTopPosition < lastScrollTop) {
        navbar.style.top = "0";
      }
    }
    lastScrollTop = scrollTopPosition <= 0 ? 0 : scrollTopPosition;
  },
  false
);

// loading screen
var loader = document.getElementById("loader");

function disableEverything() {
  document.body.style.overflow = "hidden";
  const allElements = document.querySelectorAll("*");

  allElements.forEach((element) => {
    element.style.pointerEvents = "none";
  });
}
disableEverything(); //disabling everything

function enableEverything() {
  document.body.style.overflowY = "auto";

  const allElements = document.querySelectorAll("*");

  allElements.forEach((element) => {
    element.style.pointerEvents = "auto";
  });
}

window.addEventListener("load", function () {
  setTimeout(() => {
    loader.style.display = "none";
    enableEverything(); //enablling everything
  }, 1000);
});

// Sliding slides
const slides = document.querySelectorAll(".slide");
var counter = 0;

slides.forEach((slide, index) => {
  slide.style.left = `${index * 100}%`;
});

const goNext = () => {
  if (counter == 4) {
    return;
  }
  counter++;
  slideImage();
};

const goPrev = () => {
  if (counter == 0) {
    return;
  }
  counter--;
  slideImage();
};

const slideImage = () => {
  slides.forEach((slide, index) => {
    const opacity = 1 - Math.abs(index - counter);
    slide.style.transform = `translateX(-${counter * 100}%)`;
    slide.style.opacity = opacity;
  });
};
