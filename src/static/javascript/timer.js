var startButton = document.getElementById("start-button");
var finishButton = document.getElementById("finish-button");
var resetButton = document.getElementById("reset-button");
var timer = document.getElementById("timer");
var areaToWrite = document.getElementById("area-to-write");
var counter = undefined;

startButton.addEventListener("click", runTimer);
finishButton.addEventListener("click", onFinishButtonClick);

finishButton.hidden = true;
resetButton.hidden = true;


function runTimer() {
    disableButtonAndEnableTextArea(this);
    counter = setInterval(decreaseTimer, 1000);

    startButton.hidden = true;
    finishButton.hidden = false;
    resetButton.hidden = false;
}

function onFinishButtonClick() {
    clearInterval(counter);
    areaToWrite.disabled = true;
}

function disableButtonAndEnableTextArea(element) {
    element.disabled = true;
    areaToWrite.disabled = false;
}

function decreaseTimer() {
    if(timer.textContent == 0) {
        clearInterval(counter);
        finishButton.click()
    } else {
        timer.textContent = timer.textContent - 1;
    }
}