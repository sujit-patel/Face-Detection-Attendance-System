<?php
// $_SESSION();
$servername = "localhost";
$username = "root";
$pass = "";
$database = "face";

$conn = new mysqli($servername,$username,$pass,$database);

if($conn->connect_error){
    echo"<br>you have not connected" .$conn->connect_error;
}else{
    echo"<br>connect successfull...";
}



$authority = $_POST["authority"];
$email = $_POST["email"];
$dusename = $_POST["username"];
$password = $_POST["password"];

// data inser 
$sql = "INSERT into facede (authority,email,username,password) VALUES ('$authority','$email','$dusername','$password')";

if ($conn->query($sql) == true) {
    echo "<br> Your Data Inser Successfull...";
    header("location:login.html");
}else{
    echo "<br> Your Data Not Inser " . $conn->error;
}


// $conn.close();

?>