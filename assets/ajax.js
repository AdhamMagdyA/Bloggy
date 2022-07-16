document.getElementById('signup').addEventListener('submit', function(e){
    e.preventDefault();
    // prepare form data
    var form = document.getElementById('signup');
    var formData = new FormData(form);
    // create ajax request
    var xhr = new XMLHttpRequest();
    // set the request method
    xhr.open('POST', '../ajax/');
    // send the request
    xhr.send(formData);
    // listen for the response
    xhr.onreadystatechange = function(){
        document.createElement('div');
        if(xhr.readyState == 4 && xhr.status == 200){
            var response = JSON.parse(xhr.responseText);
            if(response.success){
                document.getElementById('signup').innerHTML = response.exists;
            }
            else{
                document.getElementById('signup').innerHTML = response.exists;
            }
        }
    }
});