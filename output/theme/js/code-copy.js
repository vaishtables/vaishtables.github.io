document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('pre > code').forEach(function (codeBlock) {
    const pre = codeBlock.parentElement;

    if (pre.querySelector('.copy-button')) return;

    const button = document.createElement('button');
    button.innerText = 'Copy';
    button.className = 'copy-button';

    button.addEventListener('click', function () {
      navigator.clipboard.writeText(codeBlock.textContent).then(function () {
        button.innerText = 'Copied';
        setTimeout(() => button.innerText = 'Copy', 2000);
      }, function (err) {
        console.error('Copy failed:', err);
      });
    });

    pre.style.position = 'relative';
    button.style.position = 'absolute';
    button.style.top = '10px';
    button.style.right = '10px';
    button.style.padding = '4px 8px';
    button.style.fontSize = '1em';
    button.style.cursor = 'pointer';
    button.style.width = '28m';

    pre.appendChild(button);
  });
});
