<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%
	System.out.println("hello_sysout");
%>    
    
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=EUC-KR">
<title>Insert title here</title>
<script type="text/javascript">
	function init(){
		var str = document.getElementById("mydiv").innerHTML;
		var txt = document.getElementById("mydiv").innerText;
	}

</script>

</head>
<body onload="init()">
<div id="mydiv"><a>tttt</a></div>
<table>
	<tr>
		<td>김은대</td>
		<td>010-1123-1234</td>
	</tr>
</table>
<ul class="rank_top1000_list">
	<li>박주영</li>
	<li>손흥민</li>
	<li>차범근</li>
	<li>기성룡</li>
	<li>안정환</li>

</ul>
hello
</body>
</html>