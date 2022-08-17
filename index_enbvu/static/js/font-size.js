let content = document.getElementById('content')
let small_size = document.getElementById('small_size')
let average_size = document.getElementById('average_size')
let high_size = document.getElementById('high_size')
let h2 = document.querySelectorAll('h2')


function search_menu(size, height, size_h){
    for(i=0; i<list_menu.length; i++){
        list_menu[i].style.fontSize = size
        list_menu[i].style.height = height
    }
    for(j=0; j<submenu.length; j++){
        let sub_list = submenu[j].children
        for(s=0; s<sub_list.length; s++){
            sub_list[s].style.fontSize = size
        }
    }
    for(h=0; h<h2.length; h++){
        h2[h].style.fontSize = size_h
    }
}


small_size.addEventListener('click', function(e){
    content.style.fontSize = '16px'
    search_menu('15px', '48px', '28px')
})

average_size.addEventListener('click', function(e){
    content.style.fontSize = '22px'
    search_menu('22px', '80px', '32px')
})

high_size.addEventListener('click', function(e){
    content.style.fontSize = '26px'
    search_menu('26px', '90px', '36px')
})

