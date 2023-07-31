<!-- welcome.jsp -->
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
    <h2>Welcome, <%= session.getAttribute("loggedInUser") %>!</h2>
    <a href="logout.jsp">Logout</a>
</body>
</html>
