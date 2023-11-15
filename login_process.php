<?php
// login_process.php

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the password from the form
    $password = $_POST["password"];

    // Execute the Python script to check password strength
    $command = "python login_validator.py " . escapeshellarg($password);
    exec($command, $output, $returnCode);

    // Check the return code
    if ($returnCode === 0) {
        // Check if the output contains the message "Password is strong."
        if (in_array("Password is strong.", $output)) {
            // Password is strong, you can redirect to the welcome page if needed
            echo "Password is strong. Redirecting to the welcome page...";
            // Uncomment the next line if you want to redirect
            header("Location: welcome.html");
            exit();
        } else {
            // Output doesn't contain the expected message, display an error
            echo "Password does not meet the requirements. Reason: " . implode(", ", $output);
        }
    } else {
        // An error occurred during password validation, display an error
        echo "An error occurred during password validation.";
    }
} else {
    // If the form is not submitted, provide a default message
    echo "Please submit the form with a password.";
}
?>
