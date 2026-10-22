Act as an expert Full-Stack Python and Streamlit Developer. Write a complete, production-ready, highly responsive Streamlit web application in Python for managing "Teek Studio" (a comprehensive photography equipment rental studio management system). 

The application must feature a modern, sleek dark-mode UI (color palette: deep dark blue #0c0f1d backgrounds, card containers #161b2e, gold/yellow #f4c430 accents, and clean white typography) optimized for both mobile and desktop testing.

It must implement robust state management (st.session_state) so data persists during interaction, featuring the following dedicated views accessible via sidebar/navigation:

1. Dashboard (الرئيسية):
   - Studio branding header ("Teek Studio").
   - Quick action button to add new rental operations.
   - A 2x2 grid of KPI metric cards showing live counts: Available Items, Rented Items, Overdue Rentals, and Upcoming Bookings.
   - Financial overview summary box showing outstanding customer balances, daily collections, and expenses.
   - Quick preview section for upcoming return dates.

2. Inventory Management (إدارة المخزون):
   - Structured interactive data table showing studio gear (Name, Category/Type, Status ['متاح' / 'مؤجر'], Daily Price).
   - Fully working input form to add new equipment to the inventory with validation.

3. Rentals Section (قسم التأجير):
   - Operational table managing active and past studio rentals (Client Name, Equipment, Start Date, Due Date, Total Price, Status).
   - An interactive form to create active rental transactions, automatically calculating totals and updating the equipment's status to "Rented" in the inventory.

4. Bookings Section (قسم الحجوزات):
   - A dedicated view/table for upcoming scheduled client bookings.
   - Form to register, confirm, or manage prospective bookings before converting them into active rentals.

5. Customer Database & Expenses (قاعدة بيانات العملاء والمصروفات):
   - Structured table for client profiles (Name, Phone Number, Outstanding Balance/Debt, Notes).
   - Daily expenses tracking and financial overview.

Ensure clean modular Python syntax, error-free Pandas operations, proper Arabic text support, and responsive layout styling.
