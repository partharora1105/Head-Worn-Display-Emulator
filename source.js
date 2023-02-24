document.onkeydown = checkKey;

var deltaPos = 0.4;
var deltaSize = 2;

var pos = [45,33.5,17.6,0.3]
var size = [85,90]

document.getElementById("demoImg").style.marginLeft = pos[0] + "%";
// document.getElementById("demoImg").style.height = size[0]+ "%";

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
    console.log(currPos);
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