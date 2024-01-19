const spaEl = document.getElementById("SPA");
const routes = [];

const toRoute = (path) => {
  const route = routes.find((rt) => rt.path === path);
  if (route) return (spaEl.innerHTML = route.doc);
};

window.addEventListener("pywebviewready", async () => {
  await pywebview.api.routes().then((res) => {
    res.forEach((route) => routes.push(route));
  });
  toRoute("/");
});
