<?php
include("flag.php");

if (isset ($_GET['__magic__'])) {
    $magic = $_GET['__magic__'];

    $check = urldecode($_SERVER['QUERY_STRING']); 

    if(preg_match("/_| /i", $check)) 
    { 
        die("Get yourself some coffee"); 
    } 

    if (ereg ("^[a-zA-Z0-9]+$", $magic) === FALSE)
        echo 'Only Alphanumeric accepted';
    else if (strpos ($magic, '$dark$') !== FALSE)
    {
        if (!is_array($magic)){
            echo "Congratulations! FLAG is : ".$flag;
        }
        else{
            die("You darn!!");
        }
    }
    else
        {
            die("Your magic doesn't work on me");
        }
} else {
  show_source(__FILE__);
}
?>