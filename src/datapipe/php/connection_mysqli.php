<style>

table{
border-spacing: 50px;
border-collapse: collapse;
table-layout: fixed;

width: 100%;
margin: 20px auto;


}
td, th{

text-align: left;
border: 1px solid black;
word-wrap: break-word;
}

</style>





<?php

# Database Variables
#include('style.css');
$servername = "localhost";
$username = "id10808214_root";
$password = "CzmurXkOqDg5x2Uy";
$database = "id10808214_hdb_rp_db";
$table = "resale_flat_prices";


$mysql = mysqli_connect($servername,$username,$password,$database);

// Check for  Connection
if($mysql===false){
  echo "Could Not Connect ERROR!!!!";
}
echo "Connect Successfully. Host info: " . mysqli_get_host_info($mysql);



//SQL statements *Use a class here to pass variables to make this into a API with python*
$sql = "SELECT * FROM  $table LIMIT 5";

//Make a function and connect to python
// sql make into , array so it changes accordingly to the function.
// COnvert this into a REST API kinda thing
#$result = $mysql->query($sql);






$result = mysqli_query($mysql,$sql);


//Get Details
$num_rows = mysqli_num_rows($result);
$num_cols = mysqli_num_fields($result);

echo "<br> Number of Columns: ".$num_cols."<br>";
echo "<br> Number of Rows: ".$num_rows."<br>";




$i = 0;

echo "<table><tr>";
while ($i< $num_cols) {
  $finfo = mysqli_fetch_field($result);
  echo "<th> ".$finfo->name."</th>";
    $i++;

}
echo "</tr></table>";


make_table($num_rows,$num_cols, $result);



function make_table($num_rows, $num_cols,$result){


  echo "<table>";

  while($row = mysqli_fetch_assoc($result)){

    echo "<tr> ";

    foreach ($row as $key => $value) {
      echo "<td> ".$value."</td>";
      // code...
    }
      echo " </tr>";

  }
  echo "</table>";



}









// Close connection
mysqli_close($mysql);



?>
