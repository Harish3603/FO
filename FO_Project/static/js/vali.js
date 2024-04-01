function validateForm() {
    var username = document.getElementById("username").value;
    var email = document.getElementById("email").value;
    var phno = document.getElementById("phno").value;
    var adr = document.getElementById("adr").value;

    // Simple validation for each field
    if (username.trim() === "") {
        alert("Username is required.");
        return false;
    }
    
    if (email.trim() === "") {
        alert("Email is required.");
        return false;
    } else if (!isValidEmail(email)) {
        alert("Please enter a valid email address.");
        return false;
    }
    
    if (phno.trim() === "") {
        alert("Phone number is required.");
        return false;
    } else if (!isValidPhoneNumber(phno)) {
        alert("Please enter a valid phone number.");
        return false;
    }

    if (adr.trim() === "") {
        alert("Address is required.");
        return false;
    }
    
    return true;
}

// Function to validate email format
function isValidEmail(email) {
    var emailRegex = /\S+@\S+\.\S+/;
    return emailRegex.test(email);
}

// Function to validate phone number format
function isValidPhoneNumber(phno) {
    var phoneRegex = /^\d{10}$/;
    return phoneRegex.test(phno);
}
