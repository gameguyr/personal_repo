#! SQL

#####################
# PURPOSE: trying to understand joins.
#  Working off the W3school website this query
#  gives the product name ande  category description
#  of the most expensive product

# DATE: Mon Jun  2 23:20:20 PDT 2014
#
# AUTHOR: Russell Lego
####################

SELECT Products.* , Categories.Description

FROM Products JOIN Categories ON Products.CategoryID=Categories.CategoryID

WHERE Products.Price = (SELECT MAX(Price) FROM Products) 