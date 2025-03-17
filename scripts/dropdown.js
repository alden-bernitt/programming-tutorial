(() => {

const upArrowClass = 'up-arrow';
const downArrowClass = 'down-arrow';

function setDropdownIcon(arrowIcon, hidden)
{
    arrowIcon.classList.remove(upArrowClass);
    arrowIcon.classList.remove(downArrowClass);

    const arrowClass = hidden ? downArrowClass : upArrowClass;
    arrowIcon.classList.add(arrowClass);
}

// Setup all dropdown sections.
const ddsections = document.getElementsByClassName('dropdown-section');
for (const sect of ddsections) {
    const dropdowns = sect.querySelectorAll('& > .dropdown');
    const contents = sect.querySelectorAll('& > .dropdown-contents');

    // Initialize dropdown state
    for (const drop of dropdowns) {
        const arrowIcon = drop.querySelector('.arrow-icon')
        // Hide the dropdown contents if they are not already.
        for (const c of contents) {
            c.hidden = true;
            arrowIcon.classList.add(downArrowClass);   
        }

       // Reveal the dropdown contents when the dropdown is clicked.
        drop.addEventListener('click', () => {
            for (const c of contents) {
                c.hidden = !c.hidden;
                setDropdownIcon(arrowIcon, c.hidden);
            }
        });
    }
}
})();
