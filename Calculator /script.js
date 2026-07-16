

function AppendOperation() {
    document.getElementById("input").value += val;
}

function Clear() {
    document.getElementById("input").value = "";

}

function Evaluate() {
    try {
        document.getElementById("input").value = eval(input.value);
    } catch (error) {
        document.getElementById("input").value = "Error";
    }
}
