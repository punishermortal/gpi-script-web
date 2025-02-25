document.getElementById('uploadForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent default form submission

    var fileInput = document.getElementById('fileInput');
    var file = fileInput.files[0];

    if (!file) {
        alert('Please select a file.');
        return;
    }

    var formData = new FormData();
    formData.append('file', file);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://127.0.0.1:8000/upload/', true);  // Make sure the URL is correct
    xhr.onload = function() {
        if (xhr.status === 200) {
            alert('File uploaded successfully!');
        } else {
            alert('Error uploading file.');
        }
    };
    xhr.send(formData);
});


