function isInternetExplorer() {
    return window.navigator.userAgent.indexOf('MSIE ') > -1 || window.navigator.userAgent.indexOf('Trident/') > -1;
}
console.log(isInternetExplorer());
if (isInternetExplorer() === false) {
    console.log('Браузер не IE');
}
else {
    console.log('Сочувствую, браузер IE');
}