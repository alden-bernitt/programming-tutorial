(() => {
const ddsections = document.getElementsByClassName('dropdown-section');
for (const sect of ddsections) {
    const dropdowns = sect.querySelectorAll('& > .dropdown');
    const contents = sect.querySelectorAll('& > .dropdown-contents');

    for (const drops of dropdowns) {
        drops.addEventListener('click', () => {
            for (const c of contents) {
                c.hidden = !c.hidden;
            }
        });
    }
}
})()