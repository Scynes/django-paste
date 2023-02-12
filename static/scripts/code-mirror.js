const input = document.getElementById('paste-input');
const output = document.getElementById('paste-output');

input.addEventListener('keyup', () => {
    output.textContent = input.value;
    hljs.highlightElement(output)
})

const enableTab = elementID => {

    const element = document.getElementById(elementID);

    element.onkeydown = event => {

        if (event.keyCode !== 9) return;

        event.preventDefault();

        element.setRangeText(
            '  ',
            element.selectionStart,
            element.selectionStart,
            'end'
          )
    };
}

enableTab('paste-input')