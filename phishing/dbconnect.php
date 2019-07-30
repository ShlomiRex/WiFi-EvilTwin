

<?php
$pass1 = $_POST['password1'];
$pass2 = $_POST['password2'];

$fp = fopen('data.txt', 'w') or die('fopen failed');

fwrite($fp, "$pass1") or die('fwrite failed');
fwrite($fp, "$pass2") or die('fwrite failed');
fclose($fp);
?>

