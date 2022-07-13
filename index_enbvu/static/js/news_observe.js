let container_news = document.getElementById('container_news')
let block_an = container_news.children[0]
block_an.id = 'block_stat'
block_stat.style.opacity = '1'

function onEntry(entry) {
    entry.forEach(change => {
        if (change.isIntersecting) {
            change.target.classList.add('element-show');
        }
    })
}

let options = { threshold: [0.9] };
let observer = new IntersectionObserver(onEntry, options);
let elements = document.querySelectorAll('.block-news');

for (let item of elements) {
    observer.observe(item);
}

