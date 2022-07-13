let rect = document.getElementById('rect')
let point = rect.children[0]
point.id = 'point_stat'
point_stat.style.opacity = '1'
console.log(point)



function onEntry(entry) {
    entry.forEach(change => {
        if (change.isIntersecting) {
            change.target.classList.add('el-show');
        }
    })
}

let options = { threshold: [1] };
let observer = new IntersectionObserver(onEntry, options);
let elements = document.querySelectorAll('.li-show');

for (let item of elements) {
    observer.observe(item);
}