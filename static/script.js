function validateForm() {
    const username = document.getElementById("username").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    if (!username) {
        alert("Please enter your username.");
        return false;
    }

    if (!email || !email.includes("@")) {
        alert("Please enter a valid email address.");
        return false;
    }

    if (!password || password.length < 6) {
        alert("Password must be at least 6 characters long.");
        return false;
    }

    alert("Form submitted successfully!");
    return true;
}
