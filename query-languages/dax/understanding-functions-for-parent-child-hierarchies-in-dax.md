---
description: "Learn more about: Understanding functions for parent-child hierarchies in DAX"
title: "Understanding functions for parent-child hierarchies in DAX"
---
# Understanding functions for parent-child hierarchies in DAX

DAX provides five functions to help users manage data that is presented as a parent-child hierarchy in their models. With this functions a user can obtain the entire lineage of parents a row has, how many levels has the lineage to the top parent, who is the parent n-levels above the current row, who is the n-descendant from the top of the current row hierarchy and is certain parent a parent in the current row hierarchy?  
  
## Parent-child functions in DAX

The following table contains a Parent-Child hierarchy on the columns: **EmployeeKey** and **ParentEmployeeKey** that is used in all the functions examples.  

|EmployeeKey|ParentEmployeeKey|  
|---------------|---------------------|  
|112||  
|14|112|  
|3|14|  
|11|3|  
|13|3|  
|162|3|  
|117|162|  
|221|162|  
|81|162|  
  
In the above table you can see that employee 112 has no parent defined, employee 14 has employee 112 as manager (ParentEmployeeKey), employee 3 has employee 14 as manager and employees 11, 13, and 162 have employee 3 as manager. The above helps to understand that employee 112 has no manager above her/him and she/he is the top manager for all employees shown here; also, employee 3 reports to employee 14 and employees 11, 13, 162 report to 3.  
  
The following table presents the available functions, a brief description of the function and an example of the function over the same data shown above.  
  
[PATH function](path-function-dax.md) - Returns a delimited text with the identifiers of all the parents to the current row, starting with the oldest or top most until current.  
  
|EmployeeKey|ParentEmployeeKey|Path|  
|---------------|---------------------|--------|  
|112||112|  
|14|112|112&#124;14|  
|3|14|112&#124;14&#124;3|  
|11|3|112&#124;14&#124;3&#124;11|  
|13|3|112&#124;14&#124;3&#124;13|  
|162|3|112&#124;14&#124;3&#124;162|  
|117|162|112&#124;14&#124;3&#124;162&#124;117|  
|221|162|112&#124;14&#124;3&#124;162&#124;221|  
|81|162|112&#124;14&#124;3&#124;162&#124;81|  
  
[PATHLENGTH function](pathlength-function-dax.md) - Returns the number of levels in a given PATH(), starting at current level until the oldest or top most parent level. In the following example column PathLength is defined as '`= PATHLENGTH([Path])`'; the example includes all data from the Path() example to help understand how this function works.  
  
|EmployeeKey|ParentEmployeeKey|Path|PathLength|  
|---------------|---------------------|--------|--------------|  
|112||112|1|  
|14|112|112&#124;14|2|  
|3|14|112&#124;14&#124;3|3|  
|11|3|112&#124;14&#124;3&#124;11|4|  
|13|3|112&#124;14&#124;3&#124;13|4|  
|162|3|112&#124;14&#124;3&#124;162|4|  
|117|162|112&#124;14&#124;3&#124;162&#124;117|5|  
|221|162|112&#124;14&#124;3&#124;162&#124;221|5|  
|81|162|112&#124;14&#124;3&#124;162&#124;81|5|  
  
[PATHITEM function](pathitem-function-dax.md) - Returns the item at the specified position from a PATH() like result, counting from left to right. In the following example column PathItem - 4th from left is defined as '`= PATHITEM([Path], 4)`'; this example returns the EmployeKey at fourth position in the Path string from the left, using the same sample data from the Path() example.  
  
|EmployeeKey|ParentEmployeeKey|Path|PathItem - 4th from left|  
|---------------|---------------------|--------|-----------------------------|  
|112||112||  
|14|112|112&#124;14||  
|3|14|112&#124;14&#124;3||  
|11|3|112&#124;14&#124;3&#124;11|11|  
|13|3|112&#124;14&#124;3&#124;13|13|  
|162|3|112&#124;14&#124;3&#124;162|162|  
|117|162|112&#124;14&#124;3&#124;162&#124;117|162|  
|221|162|112&#124;14&#124;3&#124;162&#124;221|162|  
|81|162|112&#124;14&#124;3&#124;162&#124;81|162|  
  
[PATHITEMREVERSE function](pathitemreverse-function-dax.md) - Returns the item at `position` from a PATH() like function result, counting backwards from right to left.  
                In the following example column PathItemReverse - 3rd from right is defined as '`= PATHITEMREVERSE([Path], 3)`'; this example returns the EmployeKey at third position in the Path string from the right, using the same sample data from the Path() example.  
  
|EmployeeKey|ParentEmployeeKey|Path|PathItemReverse - 3rd from right|  
|---------------|---------------------|--------|-------------------------------------|  
|112||112||  
|14|112|112&#124;14||  
|3|14|112&#124;14&#124;3|112|  
|11|3|112&#124;14&#124;3&#124;11|14|  
|13|3|112&#124;14&#124;3&#124;13|14|  
|162|3|112&#124;14&#124;3&#124;162|14|  
|117|162|112&#124;14&#124;3&#124;162&#124;117|3|  
|221|162|112&#124;14&#124;3&#124;162&#124;221|3|  
|81|162|112&#124;14&#124;3&#124;162&#124;81|3|  
  
[PATHCONTAINS function](pathcontains-function-dax.md) - Returns `TRUE` if the specified `item` exists within the specified `path`. In the following example column PathContains - employee 162 is defined as '`= PATHCONTAINS([Path], "162")`'; this example returns `TRUE` if the given path contains employee 162. This example uses the results from the Path() example above.  

|EmployeeKey|ParentEmployeeKey|Path|PathContains - employee 162|  
|---------------|---------------------|--------|-------------------------------------|  
|112||112|`FALSE`|  
|14|112|112&#124;14|`FALSE`|  
|3|14|112&#124;14&#124;3|`FALSE`|  
|11|3|112&#124;14&#124;3&#124;11|`FALSE`|  
|13|3|112&#124;14&#124;3&#124;13|`FALSE`|  
|162|3|112&#124;14&#124;3&#124;162|`TRUE`|  
|117|162|112&#124;14&#124;3&#124;162&#124;117|`TRUE`|  
