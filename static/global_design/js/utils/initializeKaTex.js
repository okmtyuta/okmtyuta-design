export const initializeKaTex = () => {
  let renderKaTeX = function () {
    if (typeof renderMathInElement === "undefined") return;
    renderMathInElement(document.body, {
      delimiters: [
        { left: "$", right: "$", display: false },
        { left: "\\[", right: "\\]", display: true },
      ],
    });
  };

  (function () {
    let alpha = false;
    let beta = false;
    let gamma = false;
    let katexLoaded = function () {
      if (this.outerHTML.indexOf("katex.min.js") != -1) alpha = true;
      else if (this.outerHTML.indexOf("auto-render.min.js") != -1) beta = true;
      else if (this.outerHTML.indexOf("katex.min.css") != -1) gamma = true;

      if (alpha && beta && gamma) renderKaTeX();
    };

    let insertElement = function (elm, uri, sri) {
      let e = document.createElement(elm);
      e.setAttribute(elm === "script" ? "src" : "href", uri);
      e.setAttribute("integrity", sri);
      e.setAttribute("crossorigin", "anonymous");

      if (elm === "script") e.type = "text/javascript";
      else (e.type = "text/css"), (e.rel = "stylesheet");

      if (window.attachEvent) e.attachEvent("onload", katexLoaded);
      else if (window.addEventListener) e.addEventListener("load", katexLoaded);
      else e.onload = katexLoaded;

      document.head.appendChild(e);
    };

    insertElement(
      "script",
      "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/katex.min.js",
      "sha256-gNVpJCw01Tg4rruvtWJp9vS0rRchXP2YF+U+b2lp8Po="
    );

    insertElement(
      "script",
      "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/contrib/auto-render.min.js",
      "sha256-ExtbCSBuYA7kq1Pz362ibde9nnsHYPt6JxuxYeZbU+c="
    );

    insertElement(
      "link",
      "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/katex.min.css",
      "sha256-tkzDFSl16wERzhCWg0ge2tON2+D6Qe9iEaJqM4ZGd4E="
    );
  })();
};