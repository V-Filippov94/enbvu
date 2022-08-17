let body = document.getElementById('body')
function isInternetExplorer() {
    return window.navigator.userAgent.indexOf('MSIE ') > -1 || window.navigator.userAgent.indexOf('Trident/') > -1;
}
console.log(isInternetExplorer());
if (isInternetExplorer() === false) {
    body.style.opacity = '1'
}
else {
    console.log('Сочувствую, браузер IE');
}