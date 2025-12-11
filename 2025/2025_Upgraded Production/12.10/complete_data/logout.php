<?php
require 'common.php';
if (isset($_SESSION['user'])) {
    write_log("LOGOUT user=" . $_SESSION['user']);
}
session_destroy();
header('Location: login.php');
exit;
?>
