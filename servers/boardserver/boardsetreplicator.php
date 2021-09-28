<pre>
<?php


$localboardsetraw = file_get_contents("data/boardset.txt");
$localboardset = json_decode($localboardsetraw);

$server = $localboardset->server;

$remoteboardsetraw = file_get_contents($server."data/boardset.txt");
$remoteboardset = json_decode($remoteboardsetraw);
$boards = $remoteboardset->boards;

foreach($boards as $value){

    copy($server."boards/".$value,"boards/".$value);

}

echo json_encode($boards,JSON_PRETTY_PRINT);
    
?>
</pre>
<a href = "index.html"><img src = "iconsymbols/home.svg" alt = "home"/></a>
<style>
body{
    font-size:1em;
    font-family:courier;
    color:#00ff00;
    background-color:black;
}
</style>
