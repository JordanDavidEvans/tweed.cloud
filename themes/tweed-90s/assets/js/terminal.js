let typingSpeed = 20;
let skipTyping = false;
let totalChars = 0;
let typedChars = 0;
let progressBar;
let progressComplete = false;

function countText(node) {
  if (node.nodeType === Node.TEXT_NODE) {
    return node.textContent.length;
  }
  let count = 0;
  node.childNodes.forEach(child => {
    count += countText(child);
  });
  return count;
}

function updateProgress() {
  const progress = totalChars ? typedChars / totalChars : 0;
  const barLength = 20;
  const filled = Math.round(progress * barLength);
  const bar = '[' + '='.repeat(filled) + ' '.repeat(barLength - filled) + '] ' + Math.round(progress * 100) + '%';
  if (progress >= 1) {
    if (!progressComplete) {
      progressBar.textContent = 'Download complete';
      progressComplete = true;
      let flashes = 0;
      const flashInterval = setInterval(() => {
        progressBar.style.visibility = progressBar.style.visibility === 'hidden' ? 'visible' : 'hidden';
        flashes++;
        if (flashes >= 6) {
          clearInterval(flashInterval);
          progressBar.style.visibility = 'visible';
        }
      }, 200);
    }
  } else {
    progressBar.textContent = 'Loading ' + bar;
  }
}

function typeNode(node, parent, done) {
  if (skipTyping) {
    typedChars += countText(node);
    parent.appendChild(node.cloneNode(true));
    updateProgress();
    done();
    return;
  }
  if (node.nodeType === Node.TEXT_NODE) {
    const text = node.textContent;
    let i = 0;
    (function type() {
      if (skipTyping) {
        parent.appendChild(document.createTextNode(text.slice(i)));
        typedChars += text.length - i;
        updateProgress();
        done();
        return;
      }
      if (i < text.length) {
        parent.appendChild(document.createTextNode(text[i]));
        i++;
        typedChars++;
        updateProgress();
        setTimeout(type, typingSpeed);
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
      if (skipTyping) {
        while (i < node.childNodes.length) {
          typeNode(node.childNodes[i], el, () => {});
          i++;
        }
        done();
        return;
      }
      if (i < node.childNodes.length) {
        typeNode(node.childNodes[i], el, () => {
          i++;
          next();
        });
      } else {
        done();
      }
    })();
  } else {
    done();
  }
}

function typeWriter(element, clone, callback) {
  element.innerHTML = "";
  let i = 0;
  (function next() {
    if (skipTyping) {
      while (i < clone.childNodes.length) {
        typeNode(clone.childNodes[i], element, () => {});
        i++;
      }
      if (callback) callback();
      return;
    }
    if (i < clone.childNodes.length) {
      typeNode(clone.childNodes[i], element, () => {
        i++;
        next();
      });
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

  const clones = elements.map(el => el.cloneNode(true));
  totalChars = clones.reduce((sum, node) => sum + countText(node), 0);

  progressBar = document.createElement('div');
  progressBar.style.position = 'fixed';
  progressBar.style.bottom = '0';
  progressBar.style.left = '50%';
  progressBar.style.transform = 'translateX(-50%)';
  progressBar.style.backgroundColor = '#0d0d0d';
  progressBar.style.color = '#00ff00';
  progressBar.style.fontFamily = 'monospace';
  progressBar.style.padding = '2px 4px';
  progressBar.style.zIndex = '1000';
  document.body.appendChild(progressBar);
  updateProgress();

  elements.forEach(el => {
    el.style.minHeight = el.scrollHeight + 'px';
  });

  let index = 0;
  const updateSpeed = () => {
    const ratio = window.scrollY / (document.body.scrollHeight - window.innerHeight);
    const progress = totalChars ? typedChars / totalChars : 0;
    const diff = Math.max(0, ratio - progress);
    typingSpeed = Math.max(1, 20 - ratio * 18 - diff * 200);
  };
  window.addEventListener('scroll', updateSpeed);
  updateSpeed();

  (function next() {
    if (index < elements.length) {
      typeWriter(elements[index], clones[index], () => {
        elements[index].style.minHeight = '';
        index++;
        next();
      });
    }
  })();
});
