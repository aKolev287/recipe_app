const header = document.querySelector(".nav-container");
const toggleClass = "sticky";

document.addEventListener("scroll", () => {
  const currentScroll = document.documentElement.scrollTop;
  if (currentScroll > 60) {
    header.classList.add(toggleClass);
  } else {
    header.classList.remove(toggleClass);
  }
});
