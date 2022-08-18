let data = document.getElementById('data')
let list_tag = []
let list_li = []
flag = 0

for(tag=0; tag < data.children.length; tag++){
    console.log(data.children[tag])
    if(data.children[tag].tagName == 'DIV'){

        if(data.children[tag].className == 'rect'){
            list_tag.push(data.children[tag])
            let ol = data.children[tag].children
            list_li.push(ol[0].children)
        }
    }
}

function onEntry(entry) {
    entry.forEach(change => {
        if (change.isIntersecting) {
            change.target.classList.add('el-show');
        }
    })
}

let options = { threshold: [1] };
let observer = new IntersectionObserver(onEntry, options);



for (i=0; i < list_li.length; i++){
    for(item=0; item < list_li[i].length; item++){
        observer.observe(list_li[i][item])
    }
}
