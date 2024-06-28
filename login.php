<?php

$servername = "localhost";
$dusername = "root";
$pass = "";
$database = "face";

// Create connection
$conn = new mysqli($servername, $dusername, $pass, $database);

// Check connection
if ($conn->connect_error) {
    die("<br>Connection failed: " . $conn->connect_error);
} else {
    echo "<br>Connection successful...";
}

$authority = $_POST["authority"];
$username = $_POST["username"];
$password = $_POST["password"];

// Prepare and bind
$stmt = $conn->prepare("SELECT authority, username, password FROM facede WHERE authority = ? AND username = ? AND password = ?");
$stmt->bind_param("sss", $authority, $username, $password);

// Execute the statement
$stmt->execute();

// Store result
$stmt->store_result();

if ($stmt->num_rows > 0) {
    echo "<br>Your Data Insert Successful...";
    header("Location: index.html");
    exit(); // Ensure no further code is executed after the redirect
} else {
    echo "<br>Your Data Not Inserted: Invalid credentials.";
}

// Close the statement and connection
$stmt->close();
$conn->close();

?>
