let box_cont = document.getElementById('box_cont')
for(i=0; i<box_cont.children.length; i++){
    if(box_cont.children[i].tagName == 'HR'){
        box_cont.children[i].className = 'hr_head'
    }
}
console.log(box_cont.children[i])
