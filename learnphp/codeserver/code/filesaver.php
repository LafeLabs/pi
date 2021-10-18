<h1>
    <a href = "index.php">index.php</a>
</h1>
<?php
    //filesaver.php?filename=newtext.txt&data=derp
    $data = "text to save into text file"; //get data 
    $filename = "textfile.txt";
    $file = fopen($filename,"w");// create new file with this name
    fwrite($file,$data); //write data to file
    fclose($file);  //close file
?>