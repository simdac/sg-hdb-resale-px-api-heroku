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



$servername = "localhost";
$username = "root";
$password = "";
$database = "sg_hdb";
$table = "resale_flat_prices";


$mysql = mysqli_connect($servername,$username,$password,$database);


// Check for  Connection
if($mysql===false){
  echo "Could Not Connect ERROR!!!!";
}
echo "Connect Successfully. Host info: " . mysqli_get_host_info($mysql);



//SQL statements *Use a class here to pass variables to make this into a API with python*
$sql = "SELECT * FROM  $table LIMIT 5";
$sql = $_GET["sql"];
echo $sql;

echo  $_GET["sql"];

$result = mysqli_query($mysql,$sql);


//Get Details
$num_rows = mysqli_num_rows($result);
$num_cols = mysqli_num_fields($result);

#echo " <br> Number of Columns: ".$num_cols." <br> ";
#echo " <br> Number of Rows: ".$num_rows." <br> ";


function get_column($num_cols, $result){

  $i = 0;

  echo " <table> <tr> ";
  while ($i< $num_cols) {
    $finfo = mysqli_fetch_field($result);
    echo " <th> ".$finfo->name." </th> ";
      $i++;

  }
  echo " </tr> </table>";
}


get_column($num_cols, $result);
make_table($num_rows,$num_cols, $result);



function make_table($num_rows, $num_cols,$result){



    echo " <table> ";

    while($row = mysqli_fetch_assoc($result)){
      echo "<tr> ";
      foreach ($row as $key => $value) {
        echo " <td> ".$value." </td> ";
      }
        echo " </tr> ";
    }

    echo " </table>";

}





// Close connection
mysqli_close($mysql);




?>
