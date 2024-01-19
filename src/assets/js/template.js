const spaEl = document.getElementById("SPA");
const routes = [];

let lastDataId = null;

const toRoute = (path) => {
  const route = routes.find((rt) => rt.path === path);
  if (!route) return;

  spaEl.innerHTML = route.doc;
  if (route.script) {
    let dataId = Date.now();
    if (!lastDataId) {
      const script = document.createElement("script");
      script.setAttribute("data-id", dataId);
      script.textContent = route.script;
      return document.body.appendChild(script);
    }

    const newScript = document.createElement("script");
    newScript.setAttribute("data-id", dataId);
    newScript.textContent = route.script;

    oldScript = document.querySelector(`script[data-id="${lastDataId}"`);
    oldScript.replaceWith(newScript);

    lastDataId = dataId;
  }
};

window.addEventListener("pywebviewready", async () => {
  await pywebview.api.routes().then((res) => {
    res.forEach((route) => routes.push(route));
  });
  toRoute("/");
});
