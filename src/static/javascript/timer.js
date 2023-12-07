var startButton = document.getElementById("start-button");
var timer = document.getElementById("timer");
var areaToWrite = document.getElementById("area-to-write");
var counter = undefined;

startButton.addEventListener("click", runTimer);


function runTimer() {
    disableButtonAndEnableTextArea(this);
    counter = setInterval(decreaseTimer, 1000);
}

function disableButtonAndEnableTextArea(element) {
    element.disabled = true;
    areaToWrite.disabled = false;
}

function decreaseTimer() {
    if(timer.textContent == 0) {
        clearInterval(counter);
    } else {
        timer.textContent = timer.textContent - 1;
    }
}