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

const slides = document.querySelectorAll(".ss");
var counter = 0;

slides.forEach((slides, index) => {
  slides.style.left = `${index * 100}%`;
});

const goNext = () => {
  if (counter == 4) {
    counter = 0;
    slideImage();
  } else {
    counter++;
    slideImage();
  }
};

const goPrev = () => {
  if (counter == 0) {
    counter = 4;
    slideImage();
  } else {
    counter--;
    slideImage();
  }
};

const slideImage = () => {
  slides.forEach((slides) => {
    slides.style.transform = `translateX(-${counter * 100}%`;
  });
};

setInterval(() => {
  switch (counter) {
    case 0:
      counter = 4;
      slideImage();
    case 4:
      counter = 0;
      slideImage();
    default:
      counter++;
      slideImage();
  }
}, 5000);

const about = document.querySelector(".aboutus");
const ankush = document.querySelector(".ankush");
const shibam = document.querySelector(".shibam");
const swadhin = document.querySelector(".swadhin");

ankush.addEventListener("mouseover", function () {
  about.style.backgroundColor = "#02a9a364";
});
ankush.addEventListener("mouseout", function () {
  about.style.backgroundColor = "#00050100";
});
shibam.addEventListener("mouseover", function () {
  about.style.backgroundColor = "#d108e064";
});
shibam.addEventListener("mouseout", function () {
  about.style.backgroundColor = "#00050100";
});
swadhin.addEventListener("mouseover", function () {
  about.style.backgroundColor = "#ad0a0a64";
});
swadhin.addEventListener("mouseout", function () {
  about.style.backgroundColor = "#00050100";
});

const fwooshEl = document.querySelectorAll(".fwoosh");

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("show");
    } else {
      entry.target.classList.remove("show");
    }
  });
});

fwooshEl.forEach((el) => observer.observe(el));
