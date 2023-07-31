<!-- index.jsp -->
<%@page contentType="text/html" pageEncoding="UTF-8"%>

<!DOCTYPE html>

<html>
<head>
    <title>Arithmetic Calculator</title>
</head>
<body>

    <h2>Arithmetic Calculator</h2>

    <form method="post" action="reply.jsp">

        Number 1: <input type="text" name="num1"><br>
        Number 2: <input type="text" name="num2"><br>
        Operation:
        <select name="operation">
            <option value="+">Addition</option>
            <option value="-">Subtraction</option>
            <option value="*">Multiplication</option>
            <option value="/">Division</option>
        </select><br>

        <input type="submit" value="Calculate">

    </form>

</body>
</html>
