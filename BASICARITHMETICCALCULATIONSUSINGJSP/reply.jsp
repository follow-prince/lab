<!-- reply.jsp -->
<%@page contentType="text/html" pageEncoding="UTF-8"%>

<%@page import="java.io.*,java.util.*"%>

<%
    double num1 = Double.parseDouble(request.getParameter("num1"));
    double num2 = Double.parseDouble(request.getParameter("num2"));
    String operation = request.getParameter("operation");
    double result = 0;

    if (operation.equals("+")) {
        result = num1 + num2;
    } else if (operation.equals("-")) {
        result = num1 - num2;
    } else if (operation.equals("*")) {
        result = num1 * num2;
    } else if (operation.equals("/")) {
        result = num1 / num2;
    }

    out.print(result);
%>
