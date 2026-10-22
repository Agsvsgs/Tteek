Act as an expert Full-Stack Python and Streamlit Developer. Write a complete, production-ready, highly responsive Streamlit web application in Python for managing "Teek Studio" (a photography equipment rental studio). 

The app must feature a modern, sleek dark-mode UI (color palette: deep dark blue #0c0f1d backgrounds, card containers #161b2e, gold/yellow #f4c430 accents, and clean white typography) optimized for both mobile and desktop testing.

It must include a bottom/sidebar navigation system with dedicated interactive views for:

1. Dashboard (الرئيسية):
   - Studio branding header ("Teek Studio").
   - Quick action button to add new rentals.
   - 2x2 grid of KPI metric cards: Available Items, Rented Items, Overdue Rentals, and Upcoming Bookings.
   - Financial overview summary box showing outstanding customer balances, daily collections, and expenses.

2. Rentals Section (قسم التأجير):
   - A fully functional operational table managing active and past studio rentals (columns: Client Name, Equipment, Start Date, Due Date, Total Price, Status).
   - An interactive form to create/update active rental transactions and automatically update inventory states.

3. Bookings Section (قسم الحجوزات):
   - A dedicated calendar/list view for upcoming scheduled bookings.
   - Smart input capability or form to register, confirm, or cancel prospective client bookings before they turn into active rentals.

4. Customer Database (قاعدة بيانات العملاء):
   - A structured data table to manage client profiles (Client Name, Phone Number, Total Rentals, Outstanding Balance/Debt, Notes).
   - Search functionality to quickly find specific customers and view their individual rental history and financial status.

Ensure clean modular syntax, robust Pandas state management (st.session_state) so data persists during interaction, error-free operations, and proper Arabic RTL layout styling where applicable.
