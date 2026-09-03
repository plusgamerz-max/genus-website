const textarea = document.getElementById('input');

textarea.addEventListener('input', function () {
    if (this.value === '') {
        this.style.height = '';
        return;
    }
    this.style.height = 'auto';
    this.style.height = this.scrollHeight + 'px';
}); 