console.log("Oia o Home");

// const realEl = document.getElementById("real_companies_path");
// const simplesEl = document.getElementById("simples_companies_path");
// const presumidoEl = document.getElementById("presumido_companies_path");
// const userEl = document.getElementById("username");

// window.addEventListener("load", () => {
//   getStorageConfig();
// });

// window.addEventListener("pywebviewready", () => {
//   initConfig();
// });

// const initConfig = () => {
//   try {
//     pywebview.api.getConfig().then(async (config) => {
//       if (!config)
//         return console.log("Arquivo de configuração não encontrado!");

//       Object.keys(config).forEach((key) =>
//         window.localStorage.setItem(key, config[key])
//       );

//       getStorageConfig();
//     });

//     pywebview.api.getUsername().then((res) => {
//       window.localStorage.setItem("username", res.user.split(" ")[0]);
//       getStorageConfig();
//     });
//   } catch (err) {
//     console.error(err);
//   }
// };

// const saveConfig = () => {
//   console.log(realEl.value, simplesEl.value, presumidoEl.value);
//   if (realEl.value.trim() === "") {
//     return (realEl.classList += " is-invalid");
//   } else if (simplesEl.value.trim() === "") {
//     return (simplesEl.classList += " is-invalid");
//   } else if (presumidoEl.value.trim() === "") {
//     return (presumidoEl.classList += " is-invalid");
//   }

//   pywebview.api.saveConfig({
//     realPath: realEl.value,
//     simplesPath: simplesEl.value,
//     presumidoPath: presumidoEl.value,
//   });
// };

// const getStorageConfig = () => {
//   realEl.value = window.localStorage.getItem("realPath");
//   simplesEl.value = window.localStorage.getItem("simplesPath");
//   presumidoEl.value = window.localStorage.getItem("presumidoPath");
//   userEl.innerText = window.localStorage.getItem("username");

//   if (realEl.value !== null && realEl.value.trim() !== "")
//     realEl.classList += " active";
//   if (simplesEl.value !== null && simplesEl.value.trim() !== "")
//     simplesEl.classList += " active";
//   if (presumidoEl.value !== null && presumidoEl.value.trim() !== "")
//     presumidoEl.classList += " active";
// };
