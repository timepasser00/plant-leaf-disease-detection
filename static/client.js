var imageInput = document.getElementById("fname");
var previewImage = document.getElementById("selected_image");
imageInput.addEventListener("change",function(event){
    if(event.target.files.length == 0){
        return;
    }
    var tempUrl = URL.createObjectURL(event.target.files[0]);
    previewImage.setAttribute("src",tempUrl);
})