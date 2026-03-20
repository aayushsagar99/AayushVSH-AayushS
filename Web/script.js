const display = document.querySelector('.Answer-box');
const MAX_CHARS = 12; // Limits digits so they don't break the UI

function appendNumber(num) {
    // 1. Safety: Don't let the string get too long
    if (display.innerText.length >= MAX_CHARS) return;

    // 2. Logic: Handle the initial '0' or 'Error' state
    if (display.innerText === "0" || display.innerText === "Error") {
        display.innerText = num;
    } else {
        display.innerText += num;
    }
    
    updateFontSize();
}

function appendOperator(op) {
    const lastChar = display.innerText.slice(-1);
    const operators = ['+', '-', '*', '/'];

    // 3. Logic: Don't allow two operators in a row (e.g., "++")
    if (operators.includes(lastChar)) {
        display.innerText = display.innerText.slice(0, -1) + op;
    } else {
        display.innerText += op;
    }
}

function appendDecimal() {
    // 4. Logic: Don't allow multiple decimals in one number
    const parts = display.innerText.split(/[\+\-\*\/]/);
    const currentNumber = parts[parts.length - 1];

    if (!currentNumber.includes('.')) {
        display.innerText += '.';
    }
}

function clearDisplay() {
    display.innerText = "0";
    updateFontSize();
}

function deleteLast() {
    if (display.innerText.length > 1) {
        display.innerText = display.innerText.slice(0, -1);
    } else {
        display.innerText = "0";
    }
    updateFontSize();
}

function calculate() {
    try {
        // 5. Logic: Evaluate the string. 
        // We use Number.isInteger to keep decimals clean (e.g., 0.1 + 0.2)
        let result = eval(display.innerText);
        
        // Round long decimals to fit the screen
        if (!Number.isInteger(result)) {
            result = parseFloat(result.toFixed(4)); 
        }

        display.innerText = result;
    } catch (e) {
        display.innerText = "Error";
    }
    updateFontSize();
}

// 6. UI: Shrink text as it gets longer to stay inside the box
function updateFontSize() {

    const len = display.innerText.length;
    else if (len > 57) {
        display.style.fontSize = "0.75rem";
    }
    else if (len > 54) {
        display.style.fontSize = "0.75rem";
    }
    else if (len > 51) {
        display.style.fontSize = "0.75rem";
    } else if (len > 48) {
        display.style.fontSize = "0.85rem";
    } else if (len > 45) {
        display.style.fontSize = "0.9rem";
    } else if (len > 42) {
        display.style.fontSize = "0.95rem";
    } else if (len > 39) {
        display.style.fontSize = "1rem";
    } else if (len > 36) {
        display.style.fontSize = "1.05rem";
    } else if (len > 33) {
        display.style.fontSize = "1.1rem";
    } else if (len > 30) {
        display.style.fontSize = "1.15rem";
    } else if (len > 27) {
        display.style.fontSize = "1.2rem";
    } else if (len > 24) {
        display.style.fontSize = "0.75rem";
    } else if (len > 21) {
        display.style.fontSize = "0.85rem";
    } else if (len > 18) {
        display.style.fontSize = "1.35rem";
    } else if (len > 15) {
        display.style.fontSize = "1.4rem";
    }else if (len > 12) {
        display.style.fontSize = "1.5rem";
    } else if (len > 9) {
        display.style.fontSize = "2rem";
    } else if (len > 6) {
        display.style.fontSize = "2.25rem";
    } else if (len > 3) {
        display.style.fontSize = "2.5rem";
    }   else (len > 0) {
        display.style.fontSize = "3rem";
    }
}
