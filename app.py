Act as an expert Full-Stack Python and Streamlit Developer specializing in building high-performance operational dashboards for rental businesses (like Teek Studio). 

Write a complete, production-ready, highly responsive Streamlit web application in Python for managing a photography equipment rental studio with an Arabic interface and a modern dark-mode UI (color palette: deep dark blue #0c0f1d backgrounds, card containers #161b2e, gold/yellow #f4c430 accents, and clean white typography).

Core Requirements & Features to Implement:
1. State Management (Session State):
   - Persistent dynamic mock databases for:
     * Inventory (columns: المعدة, النوع, الحالة ['متاح' / 'مؤجر'], السعر اليومي).
     * Bookings/Rentals (columns: اسم العميل, المعدة, تاريخ البدء, تاريخ الإرجاع, الإجمالي, الحالة).
     * Customers and Daily Expenses tracking.

2. Dashboard View (الرئيسية):
   - A clean studio header with branding ("Teek Studio").
   - A prominent primary action button to quickly add new rentals.
   - A responsive 2x2 grid of KPI metric cards displaying live counts: Available Items, Rented Items, Overdue Rentals, and Upcoming Bookings.
   - Financial overview summary box displaying outstanding customer balances, daily rental collections, and expenses.
   - An "Upcoming Return Dates" section with clean empty states or actionable alerts.

3. Interactive Navigation & Modules (via Sidebar/Tabs):
   - Inventory Management: Interactive data table view + a working form to add new studio gear with validation.
   - Smart Booking / AI Parser Simulation: A natural language text area input that extracts rental details (client name, gear, duration) and saves them to the active booking registry while updating gear status automatically.
   - Rentals & Expenses Records: Dedicated operational tables to audit daily transactions and expenses seamlessly.

Ensure clean syntax, error-free Pandas operations, robust Arabic text alignment (RTL layout cues where applicable), and fast rendering performance optimized for both mobile and desktop testing.
