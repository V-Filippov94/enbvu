let menu = document.getElementById('list_menu')
let list_menu = menu.children


for(point=0; point<list_menu.length; point++){
    if(list_menu[point].innerText == 'Енисейское БВУ'){
        list_menu[point].children[0].style.top = '-200%'
        list_menu[point].children[0].style.height = '500px'
        list_menu[point].children[0].style.overflowY = 'scroll'
    }
    if(list_menu[point].innerText == 'Нормативные Документы'){
        list_menu[point].children[0].style.top = '-250%'
    }
    if(list_menu[point].innerText == 'Деятельность'){
        list_menu[point].children[0].style.top = '-270%'
        list_menu[point].children[0].style.height = '470px'
        list_menu[point].children[0].style.overflowY = 'scroll'
    }
    if(list_menu[point].innerText == 'Оказание Государственных Услуг'){
        list_menu[point].children[0].style.top = '-270%'
        list_menu[point].children[0].style.height = '470px'
        list_menu[point].children[0].style.overflowY = 'scroll'
    }
    if(list_menu[point].innerText == 'Противодействие Коррупции'){
        list_menu[point].children[0].style.top = '-400%'
        list_menu[point].children[0].style.overflowY = 'scroll'
        list_menu[point].children[0].style.height = '470px'
    }
}