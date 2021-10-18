
<ul>
    <li>
        <a href  = "../">back to code editor</a>
    </li>
<?php

// list files and or directories in a directory

$files = scandir(getcwd());

foreach($files as $value){
    if($value[0] != "."){
       echo "    <li><a href = \"".$value."\">".$value."</a></li>\n";
    }
}

?>
</ul>
<style>
    a{
        font-size:2em;
    }
</style>