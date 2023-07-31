<!-- loginProcess.jsp -->
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.util.*" %>

<%
    String validUsername = "user123";
    String validPassword = "password123";

    String username = request.getParameter("username");
    String password = request.getParameter("password");

    if (username.equals(validUsername) && password.equals(validPassword)) {
        session.setAttribute("loggedInUser", username);
        response.sendRedirect("welcome.jsp");
    } else {
        response.sendRedirect("login.jsp?error=1");
    }
%>
