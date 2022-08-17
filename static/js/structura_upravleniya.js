let lev_two = document.getElementById('lev_two')
let sector_list = document.getElementById('sector_list')
let all_org = document.getElementById('all_org')

let child_lev_two = lev_two.children
let child_sector_list = sector_list.children
let child_all_org = all_org.children

let count = 0
let count_label = 0

for(item = 0; item <child_lev_two.length; item ++){
    let child_div = child_lev_two[item].children
    for(i = 0; i < child_div.length; i++){
        if(child_div[i].tagName == 'INPUT'){
            count++
            child_div[i].id = 'indicator' + count
        }
        if(child_div[i].tagName == 'LABEL'){
            count_label++
            child_div[i].htmlFor = 'indicator'+ count_label
        }
    }
}

for(sector = 0; sector < child_sector_list.length; sector ++){
    let child_div_sector = child_sector_list[sector].children
    for(j = 0; j < child_div_sector.length; j++){
        if(child_div_sector[j].tagName == 'INPUT'){
            count++
            child_div_sector[j].id = 'indicator' + count
        }
        if(child_div_sector[j].tagName == 'LABEL'){
            count_label++
            child_div_sector[j].htmlFor = 'indicator'+ count_label
            if(child_div_sector[j].innerText == '-' || child_div_sector[j].innerText == 'Аппарат Управления'){
                child_div_sector[j].parentElement.style.display = 'none'
            }
        }
    }
}

for(org = 0; org < child_all_org.length; org ++){
    let child_div_org = child_all_org[org].children
    for(q = 0; q < child_div_org.length; q++){
        if(child_div_org[q].tagName == 'INPUT'){
            count++
            child_div_org[q].id = 'indicator' + count
        }
        if(child_div_org[q].tagName == 'LABEL'){
            count_label++
            child_div_org[q].htmlFor = 'indicator'+ count_label
        }
    }
}