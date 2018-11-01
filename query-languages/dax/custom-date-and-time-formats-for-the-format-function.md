---
title: "Custom Date and Time formats for the FORMAT Function | Microsoft Docs"
ms.service: powerbi 

ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Custom Date and Time formats for the FORMAT Function
The following table shows characters you can use to create user-defined date/time formats.  
  
|Format specification|Description|  
|------------------------|---------------|  
|(:)|Time separator. In some locales, other characters may be used to represent the time separator. The time separator separates hours, minutes, and seconds when time values are formatted. The actual character that is used as the time separator in formatted output is determined by your application's current culture value.|  
|(/)|Date separator. In some locales, other characters may be used to represent the date separator. The date separator separates the day, month, and year when date values are formatted. The actual character that is used as the date separator in formatted output is determined by your application's current culture.|  
|(%)|Used to indicate that the following character should be read as a single-letter format without regard to any trailing letters. Also used to indicate that a single-letter format is read as a user-defined format. See what follows for additional details.|  
|d|Displays the day as a number without a leading zero (for example, 1). Use %d if this is the only character in your user-defined numeric format.|  
|dd|Displays the day as a number with a leading zero (for example, 01).|  
|ddd|Displays the day as an abbreviation (for example, Sun).|  
|dddd|Displays the day as a full name (for example, Sunday).|  
|M|Displays the month as a number without a leading zero (for example, January is represented as 1). Use %M if this is the only character in your user-defined numeric format.|  
|MM|Displays the month as a number with a leading zero (for example, 01/12/01).|  
|MMM|Displays the month as an abbreviation (for example, Jan).|  
|MMMM|Displays the month as a full month name (for example, January).|  
|gg|Displays the period/era string (for example, A.D.).|  
|h|Displays the hour as a number without leading zeros using the 12-hour clock (for example, 1:15:15 PM). Use %h if this is the only character in your user-defined numeric format.|  
|hh|Displays the hour as a number with leading zeros using the 12-hour clock (for example, 01:15:15 PM).|  
|H|Displays the hour as a number without leading zeros using the 24-hour clock (for example, 1:15:15). Use %H if this is the only character in your user-defined numeric format.|  
|HH|Displays the hour as a number with leading zeros using the 24-hour clock (for example, 01:15:15).|  
|m|Displays the minute as a number without leading zeros (for example, 12:1:15). Use %m if this is the only character in your user-defined numeric format.|  
|mm|Displays the minute as a number with leading zeros (for example, 12:01:15).|  
|s|Displays the second as a number without leading zeros (for example, 12:15:5). Use %s if this is the only character in your user-defined numeric format.|  
|ss|Displays the second as a number with leading zeros (for example, 12:15:05).|  
|AM/PM|Use the 12-hour clock and display an uppercase AM with any hour before noon; display an uppercase PM with any hour between noon and 11:59 P.M.|  
|am/pm|Use the 12-hour clock and display a lowercase AM with any hour before noon; display a lowercase PM with any hour between noon and 11:59 P.M.|
|A/P|	Use the 12-hour clock and display an uppercase A with any hour before noon; display an uppercase P with any hour between noon and 11:59 P.M.|
|a/p|Use the 12-hour clock and display a lowercase A with any hour before noon; display a lowercase P with any hour between noon and 11:59 P.M.|
|AMPM|Use the 12-hour clock and display the AM string literal as defined by your system with any hour before noon; display the PM string literal as defined by your system with any hour between noon and 11:59 P.M. AMPM can be either uppercase or lowercase, but the case of the string displayed matches the string as defined by your system settings. The default format is AM/PM.|  
|y|Displays the year number (0-9) without leading zeros. Use %y if this is the only character in your user-defined numeric format.|  
|yy|Displays the year in two-digit numeric format with a leading zero, if applicable.|  
|yyy|Displays the year in four-digit numeric format.|  
|yyyy|Displays the year in four-digit numeric format.|  
|z|Displays the timezone offset without a leading zero (for example, -8). Use %z if this is the only character in your user-defined numeric format.|  
|zz|Displays the timezone offset with a leading zero (for example, -08)|  
|zzz|Displays the full timezone offset (for example, -08:00)|  
  
## Remarks  
Formatting strings are case sensitive. Different formatting can be obtained by using a different case. For example, when formatting a date value with the string "D" you get the date in the long format (according to your current locale). However, if you change the case to "d" you get the date in the short format. Also, unexpected results or an error might occur if the intended formatting does not match the case of any defined format string.  
  
Date/Time formatting uses the current user locale to determine the ultimate format of the string. For example, to format the date March 18, 1995, with the following format string "M/d/yyyy", if the user locale is set to the United States of America (en-us) the result is '3/12/1995', but if the user locale is set to Germany (de-de) the result is '18.03.1995'.  
  
## See Also  
[FORMAT Function &#40;DAX&#41;](format-function-dax.md)  
[Custom Numeric Formats for the FORMAT Function](custom-numeric-formats-for-the-format-function.md)  
[Pre-defined Date and Time formats for the FORMAT Function](pre-defined-date-and-time-formats-for-the-format-function.md)  
  
