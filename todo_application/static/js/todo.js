function toggleTheme() {
  document.body.classList.toggle("light-mode");

  const isLight = document.body.classList.contains("light-mode");

  localStorage.setItem("theme", isLight ? "light" : "dark");

  document.getElementById("themeBtn").innerText = isLight ? "☀️" : "🌙";
}

window.onload = () => {
  const savedTheme = localStorage.getItem("theme");

  if (savedTheme === "light") {
    document.body.classList.add("light-mode");
    document.getElementById("themeBtn").innerText = "☀️";
  } else {
    document.getElementById("themeBtn").innerText = "🌙";
  }
};