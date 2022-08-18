let l_region = document.getElementById('list_region')
let list_region = l_region.children

let list_district_kras = document.getElementById('list_district_kras')
let list_district_hakas = document.getElementById('list_district_hakas')
let list_district_tuva = document.getElementById('list_district_tuva')
let list_district_irk = document.getElementById('list_district_irk')
let list_district_bur = document.getElementById('list_district_bur')

let dist_kras = list_district_kras.children
let dist_hakas = list_district_hakas.children
let dist_tuva = list_district_tuva.children
let dist_irk = list_district_irk.children
let dist_bur = list_district_bur.children


let block_district = document.getElementById('block_district')
let list_files_block_dist = block_district.children
let flag = 0

function show_district(){
    if(this.innerText == 'Красноярский Край'){
        list_district_kras.style.display = 'block'
        list_district_hakas.style.display = 'none'
        list_district_tuva.style.display = 'none'
        list_district_irk.style.display = 'none'
        list_district_bur.style.display = 'none'
    }
    else if(this.innerText == 'Республика Хакасия'){
        list_district_kras.style.display = 'none'
        list_district_hakas.style.display = 'block'
        list_district_tuva.style.display = 'none'
        list_district_irk.style.display = 'none'
        list_district_bur.style.display = 'none'
    }
    else if(this.innerText == 'Республика Тыва'){
        list_district_kras.style.display = 'none'
        list_district_hakas.style.display = 'none'
        list_district_tuva.style.display = 'block'
        list_district_irk.style.display = 'none'
        list_district_bur.style.display = 'none'
    }
    else if(this.innerText == 'Иркутская Область'){
        list_district_kras.style.display = 'none'
        list_district_hakas.style.display = 'none'
        list_district_tuva.style.display = 'none'
        list_district_irk.style.display = 'block'
        list_district_bur.style.display = 'none'
    }
    else if(this.innerText == 'Республика Бурятия'){
        list_district_kras.style.display = 'none'
        list_district_hakas.style.display = 'none'
        list_district_tuva.style.display = 'none'
        list_district_irk.style.display = 'none'
        list_district_bur.style.display = 'block'
    }
}

for(reg=0; reg<list_region.length; reg++){
    list_region[reg].onclick = show_district
}



for(dist=0; dist<dist_kras.length; dist++){
    let p_dist = dist_kras[dist].children
    for(p=0; p<p_dist.length; p++){
        let p_block_dist = p_dist[p].children
        for(list_block_dist=0; list_block_dist<p_block_dist.length; list_block_dist++){
            flag ++
            p_block_dist[list_block_dist].id = 'sub_list_text' + flag
            p_block_dist[list_block_dist].style.display = 'none'
        }
    }
}
for(i=0; i<list_district_kras.children.length; i++){
    list_district_kras.children[i].onclick = open_list_file_kras
}
function open_list_file_kras(){
    for(j=0; j<this.children.length; j++){
        if(this.children[j].children[0].style.display != 'block'){
            this.children[j].children[0].style.display = 'block'
        }
        else{
            this.children[j].children[0].style.display = 'none'
        }
    }
}



for(dist=0; dist<dist_hakas.length; dist++){
    let p_dist = dist_hakas[dist].children
    for(p=0; p<p_dist.length; p++){
        let p_block_dist = p_dist[p].children
        for(list_block_dist=0; list_block_dist<p_block_dist.length; list_block_dist++){
            flag ++
            p_block_dist[list_block_dist].id = 'sub_list_text_hakas' + flag
            p_block_dist[list_block_dist].style.display = 'none'
        }
    }
}
for(i=0; i<list_district_hakas.children.length; i++){
    list_district_hakas.children[i].onclick = open_list_file_hakas
}
function open_list_file_hakas(){
    for(j=0; j<this.children.length; j++){
        if(this.children[j].children[0].style.display != 'block'){
            this.children[j].children[0].style.display = 'block'
        }
        else{
            this.children[j].children[0].style.display = 'none'
        }
    }
}



for(dist=0; dist<dist_tuva.length; dist++){
    let p_dist = dist_tuva[dist].children
    for(p=0; p<p_dist.length; p++){
        let p_block_dist = p_dist[p].children
        for(list_block_dist=0; list_block_dist<p_block_dist.length; list_block_dist++){
            flag ++
            p_block_dist[list_block_dist].id = 'sub_list_text_tuva' + flag
            p_block_dist[list_block_dist].style.display = 'none'
        }
    }
}
for(i=0; i<list_district_tuva.children.length; i++){
    list_district_tuva.children[i].onclick = open_list_file_tuva
}
function open_list_file_tuva(){
    for(j=0; j<this.children.length; j++){
        if(this.children[j].children[0].style.display != 'block'){
            this.children[j].children[0].style.display = 'block'
        }
        else{
            this.children[j].children[0].style.display = 'none'
        }
    }
}



for(dist=0; dist<dist_irk.length; dist++){
    let p_dist = dist_irk[dist].children
    for(p=0; p<p_dist.length; p++){
        let p_block_dist = p_dist[p].children
        for(list_block_dist=0; list_block_dist<p_block_dist.length; list_block_dist++){
            flag ++
            p_block_dist[list_block_dist].id = 'sub_list_text_irk' + flag
            p_block_dist[list_block_dist].style.display = 'none'
        }
    }
}
for(i=0; i<list_district_irk.children.length; i++){
    list_district_irk.children[i].onclick = open_list_file_irk
}
function open_list_file_irk(){
    for(j=0; j<this.children.length; j++){
        if(this.children[j].children[0].style.display != 'block'){
            this.children[j].children[0].style.display = 'block'
        }
        else{
            this.children[j].children[0].style.display = 'none'
        }
    }
}


for(dist=0; dist<dist_bur.length; dist++){
    let p_dist = dist_bur[dist].children
    for(p=0; p<p_dist.length; p++){
        let p_block_dist = p_dist[p].children
        for(list_block_dist=0; list_block_dist<p_block_dist.length; list_block_dist++){
            flag ++
            p_block_dist[list_block_dist].id = 'sub_list_text_bur' + flag
            p_block_dist[list_block_dist].style.display = 'none'
        }
    }
}
for(i=0; i<list_district_bur.children.length; i++){
    list_district_bur.children[i].onclick = open_list_file_bur
}
function open_list_file_bur(){
    for(j=0; j<this.children.length; j++){
        if(this.children[j].children[0].style.display != 'block'){
            this.children[j].children[0].style.display = 'block'
        }
        else{
            this.children[j].children[0].style.display = 'none'
        }
    }
}