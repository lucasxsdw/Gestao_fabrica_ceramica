document.addEventListener("DOMContentLoaded", function () {
  const input = document.querySelector("input[name='foto']");
  const previewContainer = document.getElementById("preview-container");
  const previewImage = document.getElementById("preview-image");

  if (input) {
    input.addEventListener("change", function () {
      const file = this.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
          previewImage.setAttribute("src", e.target.result);
          previewContainer.style.display = "block";
        };
        reader.readAsDataURL(file);
      } else {
        previewContainer.style.display = "none";
      }
    });
  }
});
