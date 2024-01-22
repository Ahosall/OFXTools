const spaEl = document.getElementById("SPA");
const routes = [];

const getPage = () => {
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  const page = urlParams.get("page");
  return page === null ? "/" : page;
};

const toRoute = (path) => {
  const route = routes.find((rt) => rt.path === path);
  if (!route) return;

  window.history.replaceState(
    "page",
    "OFX-Tools",
    `/template.html?page=${route.path}`
  );

  spaEl.innerHTML = route.doc;
  // TODO: Bug in scripts
  if (route.script) {
    const lastDataId = window.localStorage.getItem("lastDataId");
    const dataId = Date.now();

    console.log(dataId, lastDataId);
    const script = document.createElement("script");
    script.setAttribute("data-id", dataId);
    script.textContent = route.script;
    document.body.appendChild(script);
    window.localStorage.setItem("lastDataId", dataId);
  } else {
    const lastDataId = window.localStorage.getItem("lastDataId");
    oldScript = document.querySelector(`script[data-id="${lastDataId}"`);
    window.localStorage.removeItem("lastDataId");
    if (!oldScript) return;
    document.body.removeChild(oldScript);
    window.location.reload();
  }
};

window.addEventListener("pywebviewready", async () => {
  await pywebview.api.routes().then((res) => {
    res.forEach((route) => routes.push(route));
  });

  toRoute(getPage());
});
