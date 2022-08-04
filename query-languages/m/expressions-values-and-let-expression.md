---
description: "Learn more about: Expressions, values, and let expression"
title: "Expressions, values, and let expression"
ms.topic: conceptual
ms.date: 4/16/2018
---
# Expressions, values, and let expression
A Power Query M formula language query is composed of formula **expression** steps that create a mashup query. A formula expression can be evaluated (computed), yielding a value. The **let** expression encapsulates a set of values to be computed, assigned names, and then used in a subsequent expression that follows the **in** statement. For example, a let expression could contain a **Source** variable that equals the value of **Text.Proper()** and yields a text value in proper case.  
  
## <a name="Let"></a>Let expression  
  
```powerquery-m
let  
    Source = Text.Proper("hello world")  
in  
    Source  
```  
In the example above, Text.Proper("hello world") is evaluated to "Hello World".  
  
The next sections describe value types in the language.  
  
## <a name="Primitive"></a>Primitive value  
A **primitive** value is single-part value, such as a number, logical, text, or null. A null value can be used to indicate the absence of any data.  
  
|Type|Example value|  
|--------|-----------------|  
|Binary|00 00 00 02    // number of points (2)|  
|Date|5/23/2015|  
|DateTime|5/23/2015 12:00:00 AM|  
|DateTimeZone|5/23/2015 12:00:00 AM -08:00|  
|Duration|15:35:00|  
|Logical|true and false|  
|Null|null|  
|Number|0, 1, -1, 1.5, and 2.3e-5|  
|Text|"abc"|  
|Time|12:34:12 PM|  
  
## <a name="Function"></a>Function value  
A **Function** is a value   which, when invoked with arguments, produces a new value.  Functions are written by listing the function's **parameters** in parentheses, followed by the goes-to symbol =&gt;, followed by the expression defining the function. For example, to create a function called "MyFunction" that has two parameters and performs a calculation on parameter1 and parameter2:  
  
```powerquery-m
let  
    MyFunction = (parameter1, parameter2) => (parameter1 + parameter2) / 2  
in  
    MyFunction  
  
Calling the MyFunction() returns the result:  
  
let  
    Source = MyFunction(2, 4)  
in  
    Source  
```  
This code produces the value of 3.  
  
## <a name="Structured"></a>Structured data values  
The M language supports the following structured data values:  
  
-   [List](#list)  
  
-   [Record](#record)  
  
-   [Table](#table)  
  
-   [Additional structured data examples](#additional)  
  
> [!NOTE]  
> Structured data can contain any M value. To see a couple of examples, see [Additional structured data examples](#additional).  
  
### <a name="list"></a>List  
A List is a zero-based ordered sequence of values enclosed in curly brace characters { }. The curly brace characters { } are also used to retrieve an item from a List by index position. See \[List value](#_List_value). 
  
> [!NOTE]  
> Power Query M supports an infinite list size, but if a list is written as a literal, the list has a fixed length. For example, {1, 2, 3} has a fixed length of 3.  
  
The following are some **List** examples.  
  
|Value|Type|  
|---------|--------|  
|{123, true, "A"}|List containing a number, a logical, and text.|  
|{1, 2, 3}|List of numbers|  
|{<br />   {1, 2, 3},<br />   {4, 5, 6}<br />}|List of List of numbers|  
|{<br />  [CustomerID = 1, Name = "Bob", Phone = "123-4567"],<br />  [CustomerID = 2, Name = "Jim", Phone = "987-6543"]<br />}|List of Records|  
|{123, true, "A"}{0}|Get the value of the first item in a List. This expression returns the value 123.|  
|{<br />  {1, 2, 3},<br />  {4, 5, 6}<br />}{0}{1}|Get the value of the second item from the first List element. This expression returns the value 2.|  
  
### <a name="record"></a>Record  
A **Record** is a set of fields. A **field** is a name/value pair where the name is a text value that is unique within the field's record. The syntax for record values allows the names to be written without quotes, a form also referred to as **identifiers**. An identifier can take the following two forms:  
  
-   identifier_name such as OrderID.  
  
-   \#"identifier name" such as #"Today's data is: ".  
  
The following is a record containing fields named "OrderID", "CustomerID", "Item", and "Price" with values 1, 1, "Fishing rod", and 100.00. Square brace characters [ ] denote the beginning and end of a record expression, and are used to get a field value from a record. The follow examples show a record and how to get the Item field value. 
  
Here's an example record:  
  
```powerquery-m
let Source =   
        [  
              OrderID = 1,   
              CustomerID = 1,   
              Item = "Fishing rod",   
              Price = 100.00  
        ]  
in Source  
```  
To get the value of  an Item, you use square brackets as Source[Item]:  
  
```powerquery-m
let Source =   
    [  
          OrderID = 1,   
          CustomerID = 1,   
          Item = "Fishing rod",   
          Price = 100.00  
    ]  
in Source[Item] //equals "Fishing rod"  
```  
  
### <a name="table"></a>Table  
A **Table** is a set of values organized into named columns and rows. The column type can be implicit or explicit. You can use #table to create a list of column names and list of rows. A **Table** of values is a List in a **List**. The curly brace characters { } are also used to retrieve a row from a **Table** by index position (see [Example 3 – Get a row from a table by index position](#tableIndex)). 
  
#### Example 1 - Create a table with implicit column types  
  
```powerquery-m
let  
  Source = #table(   
    {"OrderID", "CustomerID", "Item", "Price"},   
      {   
          {1, 1, "Fishing rod", 100.00},   
          {2, 1, "1 lb. worms", 5.00}   
      })  
in  
    Source  
```  
  
#### Example 2 – Create a table with explicit column types  
  
```powerquery-m
let  
    Source = #table(  
    type table [OrderID = number, CustomerID = number, Item = text, Price = number],   
        {   
                {1, 1, "Fishing rod", 100.00},   
             {2, 1, "1 lb. worms", 5.00}   
        }  
    )  
in  
    Source  
```  
Both of the examples above creates a table with the following shape:  
  
|OrderID|CustomerID|Item|Price|  
|-----------|--------------|--------|---------|  
|1|1|Fishing rod|100.00|  
|2|1|1 lb. worms|5.00|  
  
#### <a name="tableIndex"></a>Example 3 – Get a row from a table by index position  
  
```powerquery-m
let  
    Source = #table(  
    type table [OrderID = number, CustomerID = number, Item = text, Price = number],   
        {   
              {1, 1, "Fishing rod", 100.00},   
              {2, 1, "1 lb. worms", 5.00}   
         }  
    )  
in  
    Source{1}  
```  
This expression returns the follow record:  
  
|Field|Value|  
|-|-|  
|**OrderID**|2|  
|**CustomerID**|1|  
|**Item**|1 lb. worms|  
|**Price**|5|  
  
### <a name="additional"></a>Additional structured data examples  
Structured data can contain any M value. Here are some examples:  
  
#### Example 1 - List with \[Primitive](#_Primitive_value_1) values, \[Function](#_Function_value), and \[Record](#_Record_value)  
  
```powerquery-m
let  
    Source =   
{  
   1,   
   "Bob",   
   DateTime.ToText(DateTime.LocalNow(), "yyyy-MM-dd"),   
   [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0]   
}  
in   
    Source  
```  
Evaluating this expression can be visualized as:  
  
![List Example 1](media/list-example-1.png "List Example 1")  
  
### Example 2 - Record containing Primitive values and nested Records  
  
```powerquery-m
let  
    Source = [CustomerID = 1, Name = "Bob", Phone = "123-4567", Orders =   
        {  
              [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0],  
            [OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0]  
        }]  
in   
    Source  
```  
Evaluating this expression can be visualized as:  
  
![List Example 2](media/list-example-2.png "List Example 2")  
  
> [!NOTE]  
> Although many values can be written literally as an expression, a value is not an expression. For example, the expression 1 evaluates to the value 1; the expression 1+1 evaluates to the value 2. This distinction is subtle, but important. Expressions are recipes for evaluation; values are the results of evaluation. 
  
### <a name="If"></a>If expression  
The **if** expression selects between two expressions based on a logical condition. For example:  
  
```powerquery-m
if 2 > 1 then  
    2 + 2   
else   
    1 + 1  
```  
The first expression (2 + 2) is selected if the logical expression (2 &gt; 1) is true, and the second expression (1 + 1) is selected if it is false. The selected expression (in this case 2 + 2) is evaluated and becomes the result of the **if** expression (4).  
  
