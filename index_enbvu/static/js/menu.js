let menu = document.getElementById('menu')
let point_m = menu.children
function show_point(){
    if(this.children[1].style.display != 'block' &&
    this.children[0].innerText != 'Главная' && this.children[0].innerText != 'Новости'){
        this.children[1].style.maxHeight = '1000px'
        this.children[1].style.display = 'block'
    }
    else{
        this.children[1].style.display = 'none'
    }
}
for(p=0; p<point_m.length; p++){
    point_m[p].onclick = show_point
}