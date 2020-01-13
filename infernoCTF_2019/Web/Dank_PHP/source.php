<?php
include "flag.php";

show_source(__FILE__);

class user {
  var $name;
  var $pass;
  var $secret;
}

if (isset($_GET['id'])) {

  $id = $_GET['id'];

  $usr = unserialize($id);
  if ($usr) {
    $usr->secret = $flag1;
    if ($usr->name === "admin" && $usr->pass === $usr->secret) {
      echo "Congratulation! Here is something for you...  " . $usr->pass;
      if (isset($_GET['caption'])) {
        $cap = $_GET['caption'];
        if (strlen($cap) > 45) {
          die("Naaaah, Take rest now");
        }
        if (preg_match("/[A-Za-z0-9]+/", $cap)) {
          die("Don't mess with the best language!!");
        }
        eval($cap);
        // Try to execute echoFlag()
      } else {
        echo "NVM You are not eligible";
      }
    } else {
      echo "Oh no... You can't fool me";
    }

  } else {
    echo "are you trolling?";
  }

} else {
  echo "Go and watch some Youthoob Tutorials Kidosss!!";
}
Go and watch some Youthoob Tutorials Kidosss!!