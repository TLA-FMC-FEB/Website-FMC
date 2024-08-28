const fgts = document.querySelectorAll(".fgts")
const fmcCollaboration = document.querySelectorAll(".fmcCollaboration")

const image = document.querySelector("#image")
const description = document.querySelector(".description")

function changeToFgts() {
  image.setAttribute("src", "static/media/Event/FGTS_logo.webp")
}

function addEventListenerList(list, event, fn) {
    for (var i = 0, len = list.length; i < len; i++) {
        list[i].addEventListener(event, fn, false);
    }
}

addEventListenerList(fgts, "click", changeToFgts)