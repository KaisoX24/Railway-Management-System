import customtkinter as ctk 
from tkinter import messagebox
from user_management import verify_login, register_user
import uuid

# Sample ticket database (for simplicity, stored in-memory)
ticket_db = {}

# Initialize the main application window
app = ctk.CTk()
app.title("Railway Reservation System")
app.geometry("500x400")

# Function to create an entry field with a label in CustomTkinter
def create_labeled_entry(parent, label_text, show=None):
    frame = ctk.CTkFrame(parent)
    frame.pack(fill="x", pady=5)
    ctk.CTkLabel(frame, text=label_text, width=15).pack(side="left", padx=5)
    entry = ctk.CTkEntry(frame, show=show)
    entry.pack(side="right", fill="x", expand=True, padx=5)
    return entry

# Function to create an entry field with a label and tooltip
def create_labeled_entry_with_tooltip(parent, label_text, show=None, tooltip=None):
    frame = ctk.CTkFrame(parent)
    frame.pack(fill="x", pady=5)
    label = ctk.CTkLabel(frame, text=label_text, width=15)
    label.pack(side="left", padx=5)
    entry = ctk.CTkEntry(frame, show=show)
    entry.pack(side="right", fill="x", expand=True, padx=5)

    if tooltip:
        entry.bind("<Enter>", lambda e, t=tooltip: show_tooltip(e, t))
        entry.bind("<Leave>", hide_tooltip)
    return entry

def show_tooltip(event, text):
    tooltip = ctk.CTkLabel(app, text=text, font=("Arial", 10), bg_color="lightgray")
    tooltip.place(x=event.x_root, y=event.y_root)

def hide_tooltip(event):
    for widget in app.winfo_children():
        if isinstance(widget, ctk.CTkLabel) and widget.cget("bg_color") == "lightgray":
            widget.destroy()

# Function to open the Login window
def open_login_window():
    login_window = ctk.CTkToplevel(app)
    login_window.title("Login")
    login_window.geometry("400x250")
    
    entry_username = create_labeled_entry(login_window, "Username")
    entry_password = create_labeled_entry(login_window, "Password", show="*")

    def login():
        username = entry_username.get()
        password = entry_password.get()
        result = verify_login(username, password)
        
        if result == 0:
            messagebox.showinfo("Login", "Username not found. Please register first.")
        elif result == 1:
            messagebox.showerror("Login", "Incorrect password. Please try again.")
        elif result == 2:
            messagebox.showinfo("Login", "Login successful!")
            login_window.destroy()
            show_main_menu()
        else:
            messagebox.showerror("Login", "An error occurred. Please try again.")

    ctk.CTkButton(login_window, text="Login", command=login).pack(pady=10)

# Function to open the Registration window
def open_register_window():
    register_window = ctk.CTkToplevel(app)
    register_window.title("Register")
    register_window.geometry("400x450")

    # Registration form fields
    entry_username = create_labeled_entry(register_window, "Username")
    entry_password = create_labeled_entry(register_window, "Password", show="*")
    entry_first_name = create_labeled_entry(register_window, "First Name")
    entry_last_name = create_labeled_entry(register_window, "Last Name")
    entry_phone = create_labeled_entry(register_window, "Phone")
    entry_gender = create_labeled_entry(register_window, "Gender (M/F)")
    entry_dob = create_labeled_entry(register_window, "Date of Birth (YYYY-MM-DD)")
    entry_age = create_labeled_entry(register_window, "Age")

    def register():
        username = entry_username.get()
        password = entry_password.get()
        first_name = entry_first_name.get()
        last_name = entry_last_name.get()
        phone = entry_phone.get()
        gender = entry_gender.get()
        dob = entry_dob.get()
        age = entry_age.get()

        if register_user(username, password, first_name, last_name, phone, gender, dob, age):
            messagebox.showinfo("Register", "Registration successful!")
            register_window.destroy()
            open_login_window()
        else:
            messagebox.showerror("Register", "Registration failed. Please try again.")

    ctk.CTkButton(register_window, text="Register", command=register).pack(pady=10)

# Main Menu to show after successful login
def show_main_menu():
    menu_window = ctk.CTkToplevel(app)
    menu_window.title("Railway Reservation System - Main Menu")
    menu_window.geometry("350x250")

    ctk.CTkButton(menu_window, text="Book Ticket", command=book_ticket_ui).pack(pady=5)
    ctk.CTkButton(menu_window, text="Check Ticket", command=check_ticket_ui).pack(pady=5)
    ctk.CTkButton(menu_window, text="Cancel Ticket", command=cancel_ticket_ui).pack(pady=5)

# Ticket Booking UI
def book_ticket_ui():
    book_window = ctk.CTkToplevel(app)
    book_window.title("Book Ticket")
    book_window.geometry("400x350")

    # Booking form fields
    entry_name = create_labeled_entry(book_window, "Name")
    entry_source = create_labeled_entry(book_window, "Source")
    entry_destination = create_labeled_entry(book_window, "Destination")
    entry_date = create_labeled_entry(book_window, "Date (YYYY-MM-DD)")

    def book_ticket():
        name = entry_name.get()
        source = entry_source.get()
        destination = entry_destination.get()
        date = entry_date.get()
        
        if not all([name, source, destination, date]):
            messagebox.showerror("Error", "All fields are required.")
            return

        ticket_id = str(uuid.uuid4())[:8]
        ticket_db[ticket_id] = {
            "name": name,
            "source": source,
            "destination": destination,
            "date": date
        }
        
        messagebox.showinfo("Success", f"Ticket booked! Ticket ID: {ticket_id}")
        book_window.destroy()

    ctk.CTkButton(book_window, text="Book Ticket", command=book_ticket).pack(pady=10)

# Updated Ticket Checking UI
def check_ticket_ui():
    check_window = ctk.CTkToplevel(app)
    check_window.title("Check Ticket")
    check_window.geometry("400x350")

    ctk.CTkLabel(check_window, text="Check by Ticket ID or Passenger Name", font=("Arial", 10)).pack(pady=5)
    entry_ticket_id = create_labeled_entry(check_window, "Ticket ID")
    entry_name = create_labeled_entry(check_window, "Passenger Name")

    def check_ticket():
        ticket_id = entry_ticket_id.get()
        name = entry_name.get()
        
        if ticket_id:
            if ticket_id in ticket_db:
                ticket = ticket_db[ticket_id]
                info = (
                    f"Ticket ID: {ticket_id}\n"
                    f"Name: {ticket['name']}\n"
                    f"Source: {ticket['source']}\n"
                    f"Destination: {ticket['destination']}\n"
                    f"Date: {ticket['date']}"
                )
                messagebox.showinfo("Ticket Details", info)
            else:
                messagebox.showerror("Error", "Ticket ID not found.")
        
        elif name:
            results = [f"Ticket ID: {tid}\nSource: {ticket['source']}\n"
                       f"Destination: {ticket['destination']}\nDate: {ticket['date']}\n"
                       for tid, ticket in ticket_db.items() if ticket['name'].lower() == name.lower()]
            if results:
                messagebox.showinfo("Matching Tickets", "\n\n".join(results))
            else:
                messagebox.showerror("Error", "No tickets found for this name.")
        
        else:
            messagebox.showwarning("Warning", "Please enter either Ticket ID or Passenger Name.")

    ctk.CTkButton(check_window, text="Check Ticket", command=check_ticket).pack(pady=10)

# Ticket Canceling UI with Confirmation
def cancel_ticket_ui():
    cancel_window = ctk.CTkToplevel(app)
    cancel_window.title("Cancel Ticket")
    cancel_window.geometry("400x250")

    entry_ticket_id = create_labeled_entry(cancel_window, "Ticket ID")

    def cancel_ticket():
        ticket_id = entry_ticket_id.get()
        
        if ticket_id in ticket_db:
            # Show confirmation before cancellation
            result = messagebox.askquestion("Confirm Cancellation", "Are you sure you want to cancel this ticket?")
            if result == 'yes':
                del ticket_db[ticket_id]
                messagebox.showinfo("Canceled", "Ticket successfully canceled.")
                cancel_window.destroy()
            else:
                messagebox.showinfo("Cancellation", "Ticket cancellation was canceled.")
        else:
            messagebox.showerror("Error", "Ticket not found.")

    ctk.CTkButton(cancel_window, text="Cancel Ticket", command=cancel_ticket).pack(pady=10)

# Main buttons to open either login or registration
ctk.CTkLabel(app, text="Welcome to Railway Reservation System", font=("Arial", 16)).pack(pady=20)
ctk.CTkButton(app, text="Login", command=open_login_window).pack(pady=10)
ctk.CTkButton(app, text="Register", command=open_register_window).pack(pady=10)

# Run the application
app.mainloop()


