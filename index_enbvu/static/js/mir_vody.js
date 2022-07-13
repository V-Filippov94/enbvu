let galery = document.getElementById('galery')
let mod_container = document.getElementById('mod_container');
let modal_img = document.getElementById('modal_img');
let list_child_img = galery.children
let btn_off = document.getElementById('btn_mod');


function point_modal() {
    modal_img.children[0].src = this.children[0].src
    mod_container.style.display = 'block'
}
for (i = 0; i < list_child_img.length; i++) {
    list_child_img[i].onclick = point_modal
}
btn_off.addEventListener('click', function(e) {
    mod_container.style.display = 'none'
});