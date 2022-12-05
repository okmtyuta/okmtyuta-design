import { copyUrl } from "./utils/articles.js";
import { initializeKaTex } from "./utils/export.js"

window.onload = () => {
  initializeKaTex();
  copyUrl("copyUrl")
};