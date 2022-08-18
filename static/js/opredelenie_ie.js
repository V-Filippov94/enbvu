function isInternetExplorer() {
    return window.navigator.userAgent.indexOf('MSIE ') > -1 || window.navigator.userAgent.indexOf('Trident/') > -1;
}

if (isInternetExplorer() === false) {
    console.log('Не IE')
}
else {
    let data = document.getElementById('data')
    let list_data = data.children
    for(d=0; d<list_data.length; d++){
        if(list_data[d].className == 'rect'){
            let list_opacity = list_data[d].children
            for(i=0; i<list_opacity.length; i++){
                let li_opac = list_opacity[i].children
                for(j=0; j<li_opac.length; j++){
                    li_opac[j].style.opacity = '1'
                }
            }
        }
    }
}