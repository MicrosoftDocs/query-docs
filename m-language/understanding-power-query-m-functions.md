---
title: "Understanding Power Query M functions | Microsoft Docs"
ms.custom: ""
ms.date: "2015-07-18"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
ms.assetid: c578a8a9-ade7-4793-ae3d-9c791fe402fc
caps.latest.revision: 15
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Understanding Power Query M functions
In the Power Query M formula language, a **function** is a mapping from a set of input values to a single output value. A function is written by first naming the function parameters, and then providing an expression to compute the result of the function. The body of the function follows the goes-to (=&gt;) symbol. Optionally, type information can be included on parameters and the function return value. A function is defined and invoked in the body of a **let** statement. Parameters and/or return value can be implicit or explicit. Implicit parameters and/or return value are of type **any**. Type **any** is similar to an object type in other languages. All types in M derive from type **any**.  
  
A **function** is a value just like a number or a text value, and can be included in-line just like any other expression. The following example shows a function which is the value of an Add variable which is then invoked, or executed, from several other variables. When a function is invoked, a set of values are specified which are logically substituted for the required set of input values within the function body expression.  
  
**Example – Explicit parameters and return value**  
  
```  
let  
    AddOne = (x as number) as number => x + 1,  
    //additional expression steps  
    CalcAddOne = AddOne(5)  
in  
    CalcAddOne  
```  
**Example – Implicit parameters and return value**  
  
```  
let  
    Add = (x, y) => x + y,  
    AddResults =   
        [  
            OnePlusOne = Add(1, 1),     // equals 2  
            OnePlusTwo = Add(1, 2)      // equals 3  
    ]  
in  
    AddResults  
```  
**Find the first element of a list greater than 5, or null otherwise**  
  
```  
let  
    FirstGreaterThan5 = (list) =>   
        let   
            GreaterThan5 = List.Select(list, (n) => n> 5),  
            First = List.First(GreaterThan5)  
        in  
            First,  
    Results =   
    [  
            Found    = FirstGreaterThan5({3,7,9}),  // equals 7  
            NotFound = FirstGreaterThan5({1,3,4})   // equals null  
    ]  
in  
    Results  
```  
Functions can be used recursively. In order to recursively reference the function, prefix the identifier with @.  
  
```  
let   
    fact = (num) => if num = 0 then 1 else num * @fact (num-1)   
in   
    fact(5) // equals 120  
```  
**Each keyword**  
  
The **each** keyword is used to easily create simple functions. “each ...” is syntactic sugar for a function signature that takes the _ parameter “(\_) =&gt; ...”  
  
Each is useful when combined with the lookup operator, which is applied by default to _  
For example,  each [CustomerID] is the same as each \_[CustomerID], which is the same as (\_) =&gt; \_[CustomerID]  
  
**Example – Using each in table row filter**  
  
```  
Table.SelectRows(  
      Table.FromRecords({  
            [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
            [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
            [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
            [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
      }),   
      each [CustomerID] = 2  
)[Name]  
  
// equals "Jim"  
```  
