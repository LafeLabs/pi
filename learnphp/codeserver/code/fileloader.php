<h1>
    <A href = "index.html">index.html</A>
</h1>

copy.php code:
<pre>
<?php
    $filename = "copy.php";
    $data = file_get_contents($filename);
    echo $data;
?>
</pre>
