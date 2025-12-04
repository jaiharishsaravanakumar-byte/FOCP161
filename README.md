# FOCP161
COURIER TRACKING SYSTEM
# Courier Tracking System

A complete **CRUD console application** built in Python for managing courier packages. Features add, update, track, search, delete, and display operations with file-based persistence using CSV format. Perfect for learning file I/O, input validation, and menu-driven applications. [web:1][web:9]

## ✨ Features

- ✅ **Add Courier** - Create new packages with auto-generated timestamps
- 🔄 **Update Status** - Modify package status with update timestamps  
- 📍 **Track Package** - View detailed info by tracking ID
- 🔍 **Search** - Find by name or tracking ID (case-insensitive)
- 🗑️ **Delete** - Remove packages by tracking ID
- 📋 **View All** - Display complete courier records
- 🛡️ **Validation** - 8-12 character alphanumeric tracking IDs
- 💾 **Persistent Storage** - CSV file-based data storage

## 🚀 Quick Start

1. **Prerequisites**: Python 3.8+
2. **Save** the code as `courier_tracker.py`
3. **Run**:
python courier_tracker.py

text

**Data stored automatically** in `courier_data.txt`

## 📱 Demo

====== COURIER TRACKING SYSTEM ======

Add Courier 2. Update Courier Status

Track Courier 4. View All Couriers

Search Couriers 6. Delete Courier

Exit
=====================================
Enter your choice: 1

Enter Tracking ID (8-12 alphanumeric chars): TRK12345678
Enter Sender Name: John Doe
Enter Receiver Name: Jane Smith
Courier added successfully!

text

**Track example**:
Tracking ID : TRK12345678
Sender : John Doe
Receiver : Jane Smith
Status : In Transit
Last Updated : 2025-12-04 21:10

text

## 📂 File Structure

courier-tracker/
├── courier_tracker.py # Main application (this code)
├── courier_data.txt # Auto-generated data file
└── README.md # This file

text

**Data Format** (CSV): `tracking_id,sender,receiver,status,datetime`

## 🛠️ Technical Highlights

- **File I/O**: Read/write operations with proper error handling
- **Input Validation**: Tracking ID length (8-12 chars) + alphanumeric check
- **Search Algorithm**: Linear search across tracking ID, sender, receiver
- **Data Integrity**: Maintains 5-column CSV structure
- **User Experience**: Clean numbered menu with clear feedback

## 🎯 Learning Outcomes

- File handling with context managers (`with open()`)
- String parsing and CSV manipulation
- Defensive programming (file existence checks)
- Modular function design
- Console UI patterns [web:18]

## 🔮 Future Improvements

Planned enhancements:
SQLite database migration

Multiple status history tracking

Export to CSV/JSON reports

Bulk operations

Backup/restore functionality

GUI with Tkinter

text

## 📝 Data File Example

TRK12345678,John Doe,Jane Smith,In Transit,2025-12-04 21:10
TRK98765432,Alice Brown,Bob Wilson,Delivered,2025-12-04 20:45
