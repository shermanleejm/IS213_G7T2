<?php
require_once 'common.php';
require_once 'token.php';

$error = '';

if ( isset($_GET['error']) ) {
    $error = $_GET['error'];
} elseif ( isset($_POST['username']) && isset($_POST['password']) ) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $userDAO = new UserDAO();
   
    $user = $userDAO->retrieve($username);
    $_SESSION['token'] = generate_token($username);
        
        if($user!=null){
            if($user->authenticate($password)){
                $_SESSION['username'] = $username;
                header("Location: home.html");  #im not sure where i should put the header as 
                return;
            }
            else{
                $error = 'Invalid password';
            }
        }
        if($user==null){
            $error='Invalid username!';
        }
        else{
            $error = 'Invalid password!';
        }
        
    }
?>

