<h1>
    <a href = "index.php">home</a>
</h1>

<?php

// copy from a url to a local file on server 
// usage: copy.php?from=[from file]&to=[to file]

if(isset($_GET["from"]) && isset($_GET["to"])){
    $from = $_GET["from"];
    $to = $_GET["to"];
    copy($from,$to);
}


?>

<style>
a{
    font-size:3em;
}
</style>
