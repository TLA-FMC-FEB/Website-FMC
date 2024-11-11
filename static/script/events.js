const fgts = document.querySelectorAll(".fgts");
const fmcCollaboration = document.querySelectorAll(".fmcCollaboration");
const shasaPeka = document.querySelectorAll(".shasaPeka");
const content = document.querySelectorAll("[data-content]");
const fgtsContent = document.querySelector(".fgtsContent");
const fmcCollaborationContent = document.querySelector(".fmcCollaborationContent");
const shasaPekaContent = document.querySelector(".shasaPekaContent");
const image = document.querySelector("#image");


function displayNone(list) {
  for (let i = 0, len = list.length; i < len; i++) {
    list[i].setAttribute("style", "display:none");
  }
}

function changeToFGTS() {
  displayNone(content);
  // image.setAttribute("style", "@media (max-width: 1000px) {width: 85vw}");
  image.setAttribute("src", "static/media/Event/FGTS_logo.webp");
  fgtsContent.setAttribute("style", "display:block");
}

function changeToFMCCollaboration() {
  displayNone(content);
  image.setAttribute("src", "static/media/Event/FMC COLLABORATION.webp");
  fmcCollaborationContent.setAttribute("style", "display:block");
  // image.setAttribute("style", "@media (max-width: 1000px) {width: 85vw}");
}

function changeToShasaPeka() {
  displayNone(content);
  image.setAttribute("src", "static/media/Event/SHASHA PEKA.webp");
  shasaPekaContent.setAttribute("style", "display:block");
  // image.setAttribute("style", "@media (max-width: 1000px) {width: 80vw}");
}

function addEventListenerList(list, event, fn) {
  for (var i = 0, len = list.length; i < len; i++) {
    list[i].addEventListener(event, fn, false);
  }
}

addEventListenerList(fgts, "click", changeToFGTS);
addEventListenerList(fmcCollaboration, "click", changeToFMCCollaboration);
addEventListenerList(shasaPeka, "click", changeToShasaPeka);