export const getCurrentUrl = () => {
  return location.href;
}

export const copyToClipboard = (text) => {
  navigator.clipboard.writeText(text).then((response) => {

  }).catch((error) => {

  })
}

export const copyUrl = (target) => {
  const copyUrlButtons = document.getElementsByClassName(target);

  for (const copyUrlButton of copyUrlButtons) {
    copyUrlButton.isCopied = false;
    
    copyUrlButton.addEventListener("click", () => {
      copyToClipboard(getCurrentUrl());

      for (const child of copyUrlButton.children) {

        if (child.classList.contains("copiedAlert") && !copyUrlButton.isCopied) {
          copyUrlButton.isCopied = true;

          child.style.display = "block";

          window.setTimeout(() => {
            child.style.display = "none";
            copyUrlButton.isCopied = false;
          }, 2000)

        }

      }

    })
  
  }

}