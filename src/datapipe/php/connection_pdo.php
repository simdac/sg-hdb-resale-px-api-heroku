<?php
$servername = "localhost";
$username = "id10808214_root";
$password = "CzmurXkOqDg5x2Uy";
$database = "id10808214_hdb_rp_db";

try {

    $conn = new PDO("mysql:host=$servername;dbname=$database", $username, $password);
    // set the PDO error mode to exception


    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connected successfully";
    $sql = ("SELECT * FROM resale_flat_prices LIMIT 5");
    foreach ($conn->query($sql) as $row) {
      // code...
    }
    echo $stmt;

    } catch(PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
  }



?>
