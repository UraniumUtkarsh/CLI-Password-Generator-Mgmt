from printfile import data_out



def print_html():
    title=input("title of webpage: ")
    bg=input("Bgcolor: ")
    text=input("Text: ")
    content=input("Content of webpage: ")
    
    html=f"""
<html>
<head><title> {title}
</title> </head>
<body bgcolor='{bg}' text='{text}'>
{content}
</body>
</html>
"""
    data_out(html)


    
