function validateForm() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Simple validation
    if (username === "" && password === "") {
        alert("Username and password are required.");
        return false;
    } else if (username === "") {
        alert("Username is required.");
        return false;
    } else if (password === "") {
        alert("Password is required.");
        return false;
    }
    
    // You can add more complex validation here if needed
    
    return true;
}
