var acc = document.getElementsByClassName("accordion");
var subAcc = document.getElementsByClassName("sub-accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = 1000 + "px";
    }
  });
}

for (i = 0; i < subAcc.length; i++) {
  subAcc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var subpanel = this.nextElementSibling;
    if (subpanel.style.maxHeight) {
      subpanel.style.maxHeight = null;
    } else {
      subpanel.style.maxHeight = subpanel.scrollHeight + "px";
    }
  });
}

function openNav() {
  document.getElementById("SideNavID").style.width = "400px";
}

function closeNav() {
  document.getElementById("SideNavID").style.width = "0";
}