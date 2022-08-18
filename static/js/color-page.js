let list_div = document.querySelectorAll('div')
let list_ul = document.querySelectorAll('li')
let list_h2 = document.querySelectorAll('h2')
let list_a = document.querySelectorAll('a')
let footer = document.getElementById('footer')
let flag = true

function get_color(color, background){
    for(point=0; point<list_div.length; point++){
        list_div[point].style.background = background
        list_div[point].style.color = color
    }
    for(point_ul=0; point_ul<list_ul.length; point_ul++){
        list_ul[point_ul].style.background = background
        list_ul[point_ul].style.color = color
    }
    for(point_h=0; point_h<list_h2.length; point_h++){
        list_h2[point_h].style.color = color
    }
    for(point_a=0; point_a<list_a.length; point_a++){
        list_a[point_a].style.color = color
    }
    footer.style.background = background

}

white_color.addEventListener('click', function(e){
    get_color('black', '#fff')
})
black_color.addEventListener('click', function(e){
    get_color('#fff', 'black')
})
blue_color.addEventListener('click', function(e){
    get_color('black', 'lightblue')
})
brown_color.addEventListener('click', function(e){
    get_color('rgb(169, 228, 77)', 'rgb(59, 39, 22)')
})