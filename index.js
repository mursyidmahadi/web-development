let countEl = document.getElementById("count-el")
let saveEl = document.getElementById("save-el")

let count = 0

function increment(){
    count = count + 1
    countEl.textContent = count
}

function save(){
    countStr = count + " - "
    saveEl.textContent = saveEl.textContent + countStr
}