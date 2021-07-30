<?php

$sid = array();
$name = array();
$subject = array();
$marks = array();

$conn = mysqli_connect("localhost", "root", "", "sliet");

if ($conn)
{
    echo "Connection established <br>";
    $query = "select * from students";
    $result = $conn->query($query);

    if ($result->num_rows == 0)
    {
        echo "No students found";
    }
    else
    {
        #JSON Object
        while ( $row = mysqli_fetch_array($result) )
        {
            array_push($sid, $row['sid']);
            array_push($name, $row['name']);
            array_push($subject, $row['subject']);
            array_push($marks, $row['marks']);
        }
    }

}
else
{
    echo "Connection failed";
}

echo json_encode(array('sid'=> $sid, 'name' => $name, 'subject' => $subject, 'marks' => $marks))

?>