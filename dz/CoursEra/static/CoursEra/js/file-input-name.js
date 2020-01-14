document.querySelector('.custom-file-input').addEventListener('change',function(e){
    let fileInput = document.getElementById("validatedCustomFile").children[0];
    let fileName = fileInput.files[0].name;
    let fileLabel = fileInput.nextElementSibling;
    fileLabel.innerText = fileName;
});