<h1>
    <a href = "index.php">index.php</a>
</h1>
<ul>
<?php
    $text = "this is a sequence of words";
    $words = explode(" ",$text);
    foreach($words as $value){
        echo "<li>".$value."</li>";   
    }

?>
</ul>