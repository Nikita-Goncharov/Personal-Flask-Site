wrapper = document.querySelector('.wrapper')

if (wrapper.scrollHeight === wrapper.clientHeight) {
    window.wrapper.style = `min-height: ${window.innerHeight}px`
}

