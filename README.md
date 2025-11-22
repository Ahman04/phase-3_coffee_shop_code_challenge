# phase-3_coffee_shop_code_challenge
## Coffee Shop Domain Model
## Description

The Coffee Shop Domain Model is a Python-based object-oriented project that simulates how customers order different coffees in a coffee shop.
It models three main entities: Customer, Coffee, and Order, and the relationships between them.
This project demonstrates OOP concepts such as classes, object relationships, validation, many-to-many relationships, and single source of truth.

## Author :
   Abdirahman Mohamed 

  > Setup Instructions
  > Clone this repository
  > Navigate into the project folder
  > Create and activate a virtual environment:
  > pipenv install
  > pipenv shell


## BDD (Behavior Driven Development)
Input: Valid customer name, coffee name, and price

Output: Successfully created order linking customer ↔ coffee

Input: Customer creates order via create_order(coffee, price)

Output: New order added to both customer and coffee order lists

Input: Invalid customer name (empty string or more than 15 characters)

Output: Error → “Name must be a string between 1 and 15 characters”

Input: Invalid coffee name (< 3 characters)

Output: Error → “Coffee name must be at least 3 characters”

Input: Invalid price (less than 1.0 or more than 10.0)

Output: Error → “Price must be a float between 1.0 and 10.0”

Input: Ask for most aficionado of a specific coffee

Output: Returns the customer who spent the most on that coffee

## Technologies Used

Python 3
Object-Oriented Programming
Pipenv



GitHub : [https://github.com/Ahman04/phase-3_coffee_shop_code_challenge.git]


## License

## MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall
be included in all copies or substantial portions of the Software.