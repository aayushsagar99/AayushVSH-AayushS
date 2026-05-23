<%@ Language=VBScript %>
<%
Option Explicit

' Function to sanitize input data
Function SanitizeInput(ByVal inputData)
    If IsNull(inputData) Then
        SanitizeInput = ""
    Else
        Dim cleanData
        cleanData = Replace(inputData, "<", "&lt;")
        cleanData = Replace(cleanData, ">", "&gt;")
        SanitizeInput = Trim(cleanData)
    End If
End Function

Dim userName, userMessage, isSubmitted
isSubmitted = False

' Check if form was submitted
If Request.ServerVariables("REQUEST_METHOD") = "POST" Then
    userName = SanitizeInput(Request.Form("txtName"))
    userMessage = SanitizeInput(Request.Form("txtMessage"))
    isSubmitted = True
End If
%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Classic ASP Contact Form</title>
</head>
<body>
    <h2>Submit Your Feedback</h2>
    
    <% If isSubmitted Then %>
        <div style="color: green; margin-bottom: 20px;">
            <strong>Thank you, <%= userName %>!</strong><br>
            We received your message: "<em><%= userMessage %></em>"
        </div>
    <% End If %>

    <form method="POST" action="">
        <label for="txtName">Name:</label><br>
        <input type="text" id="txtName" name="txtName" required><br><br>
        
        <label for="txtMessage">Message:</label><br>
        <textarea id="txtMessage" name="txtMessage" required></textarea><br><br>
        
        <input type="submit" value="Send Feedback">
    </form>
</body>
</html>
