---
title: "Custom date and time formats for the FORMAT function | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/31/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# Custom date and time formats for the FORMAT function

The following tables describe characters used to create user-defined date/time formats.  

## User-defined date/time formats 

|Character|Description|
|:-----|:-----|
|(**:**)|Time separator. In some [locales](../../Glossary/vbe-glossary.md#locale), other characters may be used to represent the time separator. The time separator separates hours, minutes, and seconds when time values are formatted. The actual character used as the time separator in formatted output is determined by your system settings.|
|(**/**)|[Date separator](../../Glossary/vbe-glossary.md#date-separators). In some locales, other characters may be used to represent the date separator. The date separator separates the day, month, and year when date values are formatted. The actual character used as the date separator in formatted output is determined by your system settings.|
|c|Display the date as  `ddddd` and display the time as `ttttt`, in that order. Display only date information if there is no fractional part to the date serial number; display only time information if there is no integer portion.|
|d|Display the day as a number without a leading zero (1&ndash;31).|
|dd|Display the day as a number with a leading zero (01&ndash;31).|
|ddd|Display the day as an abbreviation (Sun&ndash;Sat). Localized.|
|dddd|Display the day as a full name (Sunday&ndash;Saturday). Localized.|
|ddddd|Display the date as a complete date (including day, month, and year), formatted according to your system's short date format setting. The default short date format is  `m/d/yy`.|
|dddddd|Display a date serial number as a complete date (including day, month, and year) formatted according to the long date setting recognized by your system. The default long date format is  `mmmm dd, yyyy`.|
|w|Display the day of the week as a number (1 for Sunday through 7 for Saturday).|
|ww|Display the week of the year as a number (1&ndash;54).|
|m|Display the month as a number without a leading zero (1&ndash;12). If `m` immediately follows `h` or `hh`, the minute rather than the month is displayed.|
|mm|Display the month as a number with a leading zero (01&ndash;12). If `m` immediately follows `h` or `hh`, the minute rather than the month is displayed. |
|mmm|Display the month as an abbreviation (Jan&ndash;Dec). Localized.|
|mmmm|Display the month as a full month name (January&ndash;December). Localized.|
|q|Display the quarter of the year as a number (1&ndash;4).|
|y|Display the day of the year as a number (1&ndash;366).|
|yy|Display the year as a 2-digit number (00&ndash;99).|
|yyyy|Display the year as a 4-digit number (100&ndash;9999).|
|h|Display the hour as a number without a leading zero (0&ndash;23).|
|hh|Display the hour as a number with a leading zero (00&ndash;23).|
|n|Display the minute as a number without a leading zero (0&ndash;59).|
|nn|Display the minute as a number with a leading zero (00&ndash;59).|
|s|Display the second as a number without a leading zero (0&ndash;59).|
|ss|Display the second as a number with a leading zero (00&ndash;59).|
|ttttt|Display a time as a complete time (including hour, minute, and second), formatted using the time separator defined by the time format recognized by your system. A leading zero is displayed if the leading zero option is selected and the time is before 10:00 A.M. or P.M. The default time format is `h:mm:ss`.|
|AM/PM|Use the 12-hour clock and display an uppercase AM with any hour before noon; display an uppercase PM with any hour between noon and 11:59 P.M.|
|am/pm|Use the 12-hour clock and display a lowercase AM with any hour before noon; display a lowercase PM with any hour between noon and 11:59 P.M.|
|A/P|Use the 12-hour clock and display an uppercase A with any hour before noon; display an uppercase P with any hour between noon and 11:59 P.M.|
|a/p|Use the 12-hour clock and display a lowercase A with any hour before noon; display a lowercase P with any hour between noon and 11:59 P.M.|
|AMPM|Use the 12-hour clock and display the AM [string literal](../../Glossary/vbe-glossary.md#string-literal) as defined by your system with any hour before noon; display the PM string literal as defined by your system with any hour between noon and 11:59 P.M. AMPM can be either uppercase or lowercase, but the case of the string displayed matches the string as defined by your system settings. The default format is AM/PM. If your system is set to 24-hour clock, the string is typical set to a zero-length string.|
  
## Remarks  
  
Date/Time formatting uses the current user locale to determine the ultimate format of the string. For example, to format the date March 18, 1995, with the following format string "m/d/yyyy", if the user locale is set to the United States of America (en-us) the result is '3/12/1995', but if the user locale is set to Germany (de-de) the result is '18.03.1995'.  
  
## See also  
[FORMAT function &#40;DAX&#41;](format-function-dax.md)  
[Custom numeric formats for the FORMAT function](custom-numeric-formats-for-the-format-function.md)  
[Pre-defined date and time formats for the FORMAT function](pre-defined-date-and-time-formats-for-the-format-function.md)  
  
