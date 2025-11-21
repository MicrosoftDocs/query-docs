---
description: "Learn more about: Understanding Power Query M functions"
title: "Understanding Power Query M functions"
ms.topic: language-reference
ms.date: 2/14/2025
ms.custom: "nonautomated-date"
ms.subservice: m-background
---

# Understanding Power Query M functions

In the Power Query M formula language, a *function* is a mapping from a set of input values to a single output value. A function is written by first naming the function parameters, and then providing an expression to compute the result of the function. The body of the function follows the goes-to (=&gt;) symbol. Optionally, type information can be included on parameters and the function return value. A function is defined and invoked in the body of a **let** statement. Parameters and/or return value can be implicit or explicit. Implicit parameters and/or return value are of type **any**. Type **any** is similar to an object type in other languages. All types in M derive from type **any**.  

A function is a value just like a number or a text value, and can be included in-line just like any other expression. The following example shows a function that is the value of an **Add** variable, which is then invoked, or executed, from several other variables. When a function is invoked, a set of values are specified that logically substitute for the required set of input values within the function body expression.

**Example - Explicit parameters and return value**

```powerquery-m
let  
    AddOne = (x as number) as number => x + 1,  
    //additional expression steps  
    CalcAddOne = AddOne(5)  
in  
    CalcAddOne  
```

**Example - Implicit parameters and return value**

```powerquery-m
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

```powerquery-m
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

```powerquery-m
let   
    fact = (num) => if num = 0 then 1 else num * @fact (num-1)   
in   
    fact(5) // equals 120  
```

**Each keyword**

The **each** keyword is used to easily create simple functions. `each ...` is syntactic sugar for a function signature that takes the `_` parameter `(_) => ...`.

The **each** keyword is useful when combined with the lookup operator, which is applied by default to `_`.
For example, `each [CustomerID]` is the same as `each _[CustomerID]`, which is the same as `(_) => _[CustomerID]`.

**Example - Using each in table row filter**

```powerquery-m
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
