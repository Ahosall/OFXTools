const presumidoEl = document.getElementById("presumido_path");
const realEl = document.getElementById("real_path");
const simplesEl = document.getElementById("simples_path");
const userEl = document.getElementById("username");

window.addEventListener("load", () => {
  getStorageConfig();
});

const initConfig = () => {
  try {
    pywebview.api.getConfig().then(async (config) => {
      if (!config)
        return console.log("Arquivo de configuração não encontrado!");

      Object.keys(config).forEach((key) =>
        window.localStorage.setItem(key, config[key])
      );

      getStorageConfig();
    });

    pywebview.api.getUsername().then((res) => {
      window.localStorage.setItem("username", res.user.split(" ")[0]);
      getStorageConfig();
    });
  } catch (err) {
    console.error(err);
  }
};

const saveConfig = () => {
  console.log(realEl.value, simplesEl.value, presumidoEl.value);
  realEl.classList =
    presumidoEl.value.trim() === ""
      ? presumidoEl.classList.toString() + " is-invalid"
      : presumidoEl.classList.toString().replace("is-invalid", "");

  presumidoEl.classList =
    realEl.value.trim() === ""
      ? realEl.classList.toString() + " is-invalid"
      : realEl.classList.toString().replace("is-invalid", "");

  simplesEl.classList =
    simplesEl.value.trim() === ""
      ? simplesEl.classList.toString() + " is-invalid"
      : simplesEl.classList.toString().replace("is-invalid", "");

  pywebview.api.saveConfig({
    realPath: realEl.value,
    simplesPath: simplesEl.value,
    presumidoPath: presumidoEl.value,
  });
};

const getStorageConfig = () => {
  userEl.innerText = window.localStorage.getItem("username");
  presumidoEl.value = window.localStorage.getItem("presumidoPath");
  realEl.value = window.localStorage.getItem("realPath");
  simplesEl.value = window.localStorage.getItem("simplesPath");

  presumidoEl.classList = presumidoEl.classList
    .toString()
    .replace("is-invalid", "");
  realEl.classList = realEl.classList.toString().replace("is-invalid", "");
  simplesEl.classList = simplesEl.classList
    .toString()
    .replace("is-invalid", "");
};

initConfig();
