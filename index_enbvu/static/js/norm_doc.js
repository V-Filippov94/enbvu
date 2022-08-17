let main = document.getElementById('main')
let list_tag = []
let list_li = []
flag = 0

for(t=0; t < main.children.length; t++){
    if(main.children[t].className == 'data'){
        for(tag=0; tag < main.children[t].children.length; tag++){
            if(main.children[t].children[tag].className == 'rect'){
                list_tag.push(main.children[t].children[tag])
                let ol = main.children[t].children[tag].children
                list_li.push(ol[0].children)
            }
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

let options = { threshold: [0.5] };
let observer = new IntersectionObserver(onEntry, options);



for (i=0; i < list_li.length; i++){
    for(item=0; item < list_li[i].length; item++){
        observer.observe(list_li[i][item])
    }
}