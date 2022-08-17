let cont_rating = document.getElementById('container-rating')
let btn_result = document.getElementById('btn_result')
let golos = document.getElementById('golos')
cont_rating_child = cont_rating.children



function show_rating(){
    for(i=0; i<cont_rating_child.length; i++){
    let child_span = cont_rating_child[i]
        for(j=0; j<child_span.children.length; j++){
            if(child_span.children[j].tagName == 'SPAN'){
                child_span.children[j].style.opacity = '1'
            }
            if(child_span.children[j].tagName == 'INPUT'){
                console.log(child_span.children[j])
                child_span.children[j].style.display = 'none'
            }
            golos.style.display = 'none'
            btn_result.style.display = 'none'
        }
    }
}

btn_result.onclick = show_rating