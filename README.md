# Dry Cleaning Senior Project

## Overview

This project is a prototype desktop management system developed for a small family-owned dry-cleaning business as part of a senior thesis in Mathematics and Computer Science at Purchase College (SUNY).

The goal of the project is to explore how a lightweight, locally hosted application can improve workflow efficiency in a small business environment compared to older legacy dry-cleaning management software systems.

The prototype focuses on core workflow operations such as:

* customer management
* order creation
* order retrieval
* pickup status updates
* structured database storage

The system was developed using Python, PyQt6, and SQLite following a modular Model–View–Controller (MVC) inspired architecture.

-

## Current Prototype Features

### Implemented

* SQLite local database
* Customer record creation
* Order creation
* Order retrieval by receipt identifier
* Pickup status updates
* Multi-page desktop interface
* Sidebar navigation
* MVC-style project structure

### Partially Implemented

* Customer lookup workflows
* Order history retrieval
* Payment tracking
* Authentication/login structure

### Planned / Future Work

* Advanced order entry workflows
* Reporting tools
* Receipt printing
* Barcode scanner integration
* Expanded UI refinement
* Role-based permissions

-

## Technologies Used

* Python 3
* PyQt6
* SQLite
* Qt Designer
* Canva (UI mockups)

-

## Project Structure

```text
drycleaning_app/
│
├── controller/
├── database/
├── model/
├── view/
├── main.py
```

* `controller/` handles workflow logic and communication between the interface and database
* `database/` contains SQLite database management code
* `model/` contains planned data model structures
* `view/` contains PyQt6 interface components

-

## Running the Application

### Requirements

Install PyQt6:

```bash
pip install PyQt6
```

### Launch

Run the application from the project root directory:

```bash
python main.py
```

-

## Thesis Context

This repository accompanies the senior thesis:

**“Dry Cleaning Software: Design and Prototype of a Desktop Management System for a Small Business”**

submitted to the Department of Mathematics and Computer Science at Purchase College, State University of New York.

The project should be understood as a functional prototype and research-focused implementation rather than a finished commercial product.

-

## Author

Paxton P. Chavez
Purchase College – SUNY
B.A. Mathematics and Computer Science
May 2026
