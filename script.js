const container = document.getElementById("portfolio");
const modalImage = document.getElementById("modal-image");
const modal = document.getElementById("modal");
const images = container.querySelectorAll("img");


for(let i=0; i < images.length; i++){
    
    images[i].addEventListener("click", function(){
        modalImage.src = images[i].src;
        modal.classList.remove("no-display");
    });
}

modal.addEventListener("click", function(){
    modal.classList.add("no-display");
    modalImage.src = null;
})