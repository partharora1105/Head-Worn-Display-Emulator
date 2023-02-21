document.onkeydown = checkKey;

var deltaPos = 10;
var deltaSize = 10;

var pos = [10,20,30,40]
var size = [50,60]

document.getElementById("demoImg").style.marginLeft = pos[0] + "%";
document.getElementById("demoImg").style.height = size[0]+ "%";

function checkKey(e) {

    e = e || window.event;
    var currPos = document.getElementById("demoImg").style.marginLeft;
    currPos = parseInt(currPos.trim("%"))

    var currSize = document.getElementById("demoImg").style.height;
    currSize = parseInt(currSize.trim("%"))

    if (e.keyCode == '38') {
        currSize += deltaSize;
    }
    else if (e.keyCode == '40') {
        currSize -= deltaSize;
    }
    else if (e.keyCode == '37') {
       currPos -= deltaPos;
    }
    else if (e.keyCode == '39') {
        currPos += deltaPos;
    }
    document.getElementById("demoImg").style.marginLeft = currPos + "%";
    document.getElementById("demoImg").style.height = currSize + "%";
}

function setPos(num) {
    var currPos = document.getElementById("demoImg").style.marginLeft;
    currPos = parseInt(currPos.trim("%"))
    pos[num - 1] = currPos
}

function setSize(num) {
    var currSize = document.getElementById("demoImg").style.height;
    currSize = parseInt(currSize.trim("%"))
    size[num - 1] = currSize
}

function getPos(num) {
    document.getElementById("demoImg").style.marginLeft = pos[num - 1] + "%";
}

function getSize(num) {
    document.getElementById("demoImg").style.height = size[num - 1] + "%";
}