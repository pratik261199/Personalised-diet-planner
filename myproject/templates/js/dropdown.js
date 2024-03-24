/*=============================================
=            Custom select                   =
=============================================*/
/* Generate custom select */
const selects = Array.from(document.getElementsByClassName('custom-select'));

selects.forEach((select)=> {
    const classes = select.getAttribute('class');
    const options = Array.from(select.getElementsByTagName('option'));
    const wrapper = createEl("div","custom-select-wrapper");
    const span = createEl("span", "custom-select-trigger");
    const options_wrapper = createEl("div","custom-options");
    const template = createTemplate(classes,span);

    span.innerText = select.getAttribute("placeholder");

    generateOptions(options, options_wrapper);

    template.appendChild(options_wrapper);
    wrap(select, wrapper);
    select.after(template);
})

/* Add event on clicked select */
const triggers = Array.from(document.getElementsByClassName('custom-select-trigger'));

triggers.forEach((trigger) => {
    trigger.addEventListener("click", ()=> {
        trigger.parentNode.classList.toggle("opened");

    })
})

/* Add event on clicked option */
const customOptions = Array.from(document.getElementsByClassName('custom-option'));

customOptions.forEach((option) => {
    option.addEventListener("click",() => {
        const customSelect = findAncestor(option,"custom-select");
        const select = customSelect.previousSibling;
        const trigger = findAncestor(option,"custom-options").previousSibling;

        select.value = option.getAttribute("data-value");
        customSelect.classList.toggle("opened");
        trigger.innerText = option.innerText;


    })
})

function findAncestor(el,cls) {
    while ((el = el.parentNode) && !el.classList.contains(cls));
    return el;
}

function generateOptions(options, wrapper) {
    options.forEach((option) => {
        const html_option = document.createElement('span');
        html_option.classList.add(`custom-option`);
        html_option.setAttribute("data-value",option.getAttribute("value"));
        html_option.innerText = option.innerText;
        wrapper.appendChild(html_option);
    });
}

function createEl(node, classes) {
    const el = document.createElement(node);
    el.classList.add(classes);
    return el;
}

function createTemplate(classes, child) {
    const template = document.createElement('div');
    template.classList.add(classes);
    template.appendChild(child);
    return template;
}

function wrap(el, wrapper) {
    el.parentNode.insertBefore(wrapper,el);
    wrapper.appendChild(el);
}


/*=====  End of Custom select         ======*/