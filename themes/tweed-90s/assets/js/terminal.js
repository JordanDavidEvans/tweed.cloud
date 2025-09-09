function typeNode(node, parent, done, speed) {
  if (node.nodeType === Node.TEXT_NODE) {
    const text = node.textContent;
    let i = 0;
    (function type() {
      if (i < text.length) {
        parent.appendChild(document.createTextNode(text[i]));
        i++;
        setTimeout(type, speed);
      } else {
        done();
      }
    })();
  } else if (node.nodeType === Node.ELEMENT_NODE) {
    const el = document.createElement(node.tagName.toLowerCase());
    for (const attr of node.attributes) {
      el.setAttribute(attr.name, attr.value);
    }
    parent.appendChild(el);
    let i = 0;
    (function next() {
      if (i < node.childNodes.length) {
        typeNode(node.childNodes[i], el, () => {
          i++;
          next();
        }, speed);
      } else {
        done();
      }
    })();
  } else {
    done();
  }
}

function typeWriter(element, speed, callback) {
  const clone = element.cloneNode(true);
  element.innerHTML = "";
  let i = 0;
  (function next() {
    if (i < clone.childNodes.length) {
      typeNode(clone.childNodes[i], element, () => {
        i++;
        next();
      }, speed);
    } else if (callback) {
      callback();
    }
  })();
}

document.addEventListener("DOMContentLoaded", () => {
  document.body.style.backgroundColor = "#0d0d0d";
  document.body.style.color = "#00ff00";
  document.body.style.fontFamily = "monospace";
  const elements = [
    document.querySelector('.site-header'),
    document.querySelector('main'),
    document.querySelector('.site-footer')
  ].filter(Boolean);
  let index = 0;
  (function next() {
    if (index < elements.length) {
      typeWriter(elements[index], 20, () => {
        index++;
        next();
      });
    }
  })();
});
