script.js:
document.addEventListener("DOMContentLoaded", () => {

const btn = document.getElementById("themeToggle")

function setTheme(mode){

if(mode === "dark"){
document.body.classList.add("dark")
document.body.style.background="#0b1220"
document.body.style.color="#e6edf3"
btn.innerHTML="☀"
}
else{
document.body.classList.remove("dark")
document.body.style.background="#f4f6fb"
document.body.style.color="#111"
btn.innerHTML="🌙"
}

localStorage.setItem("theme",mode)
}

btn.onclick = () => {

if(document.body.classList.contains("dark")){
setTheme("light")
}else{
setTheme("dark")
}

}

let savedTheme = localStorage.getItem("theme")

if(savedTheme){
setTheme(savedTheme)
}else{
setTheme("dark")
}

})