function isInternetExplorer() {
    return window.navigator.userAgent.indexOf('MSIE ') > -1 || window.navigator.userAgent.indexOf('Trident/') > -1;
}

if (isInternetExplorer() === false) {
    console.log('Не IE')
}
else{
    for(news=0; news<container_news.children.length; news++){
        container_news.children[news].style.opacity = '1'
    }
}