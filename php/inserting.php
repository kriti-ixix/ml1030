<?php

#mysqli_connect(server address, username, password, database name);
$connection = mysqli_connect("localhost", "root", "", "sliet");

if ($connection)
{
    echo "Connection established <br>";   
    $command = "insert into students values (3, 'XYZ', 'JAVA', 60)";
    $result = $connection -> query($command);

    if ($result == 0)
    {
        echo "No changes occured";
    }
    else
    {
        echo "Values inserted";
    }

}
else
{
    echo "Connection failed";
}

?>