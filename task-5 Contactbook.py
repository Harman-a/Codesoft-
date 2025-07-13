# import customtkinter as ctk
# from tkinter import messagebox
# import json
# import os

# ctk.set_appearance_mode("Light")
# ctk.set_default_color_theme("blue")

# DATA_FILE = "contacts.json"


# # Utility Functions
# def load_contacts():
#     if not os.path.exists(DATA_FILE):
#         with open(DATA_FILE, 'w') as f:
#             json.dump([], f)
#     with open(DATA_FILE, 'r') as f:
#         return json.load(f)


# def save_contacts(data):
#     with open(DATA_FILE, 'w') as f:
#         json.dump(data, f, indent=4)


# # GUI Class
# class ContactBook(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#         self.title("Contact Book - Task 5")
#         self.geometry("700x450")
#         self.resizable(False, False)

#         self.contacts = load_contacts()

#         # UI Layout
#         self.create_widgets()
#         self.refresh_contact_list()

#     def create_widgets(self):
#         # Entry Frame
#         entry_frame = ctk.CTkFrame(self)
#         entry_frame.pack(pady=10, padx=10, fill="x")

#         self.name_entry = ctk.CTkEntry(entry_frame, placeholder_text="Name")
#         self.name_entry.grid(row=0, column=0, padx=5, pady=5)

#         self.phone_entry = ctk.CTkEntry(entry_frame, placeholder_text="Phone")
#         self.phone_entry.grid(row=0, column=1, padx=5, pady=5)

#         self.email_entry = ctk.CTkEntry(entry_frame, placeholder_text="Email")
#         self.email_entry.grid(row=1, column=0, padx=5, pady=5)

#         self.address_entry = ctk.CTkEntry(entry_frame, placeholder_text="Address")
#         self.address_entry.grid(row=1, column=1, padx=5, pady=5)

#         self.add_button = ctk.CTkButton(entry_frame, text="Add / Update", command=self.add_or_update_contact)
#         self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

#         # Search Field
#         self.search_entry = ctk.CTkEntry(self, placeholder_text="Search by Name or Phone")
#         self.search_entry.pack(pady=5, padx=10, fill="x")
#         self.search_entry.bind("<KeyRelease>", self.search_contact)

#         # Listbox
#         self.contact_listbox = ctk.CTkTextbox(self, width=650, height=150)
#         self.contact_listbox.pack(pady=5, padx=10)

#         # Delete Button
#         self.delete_button = ctk.CTkButton(self, text="Delete Selected", fg_color="red", command=self.delete_contact)
#         self.delete_button.pack(pady=10)

#     def refresh_contact_list(self, filtered=None):
#         self.contact_listbox.delete("0.0", "end")
#         data = filtered if filtered else self.contacts
#         for contact in data:
#             display = f"{contact['name']} - {contact['phone']}\n"
#             self.contact_listbox.insert("end", display)

#     def add_or_update_contact(self):
#         name = self.name_entry.get().strip()
#         phone = self.phone_entry.get().strip()
#         email = self.email_entry.get().strip()
#         address = self.address_entry.get().strip()

#         if not name or not phone:
#             messagebox.showerror("Error", "Name and Phone are required!")
#             return

#         updated = False
#         for contact in self.contacts:
#             if contact['phone'] == phone:
#                 contact.update({"name": name, "email": email, "address": address})
#                 updated = True
#                 break

#         if not updated:
#             self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})

#         save_contacts(self.contacts)
#         self.refresh_contact_list()
#         self.clear_entries()
#         messagebox.showinfo("Success", "Contact saved successfully!")

#     def delete_contact(self):
#         selected = self.contact_listbox.get("sel.first", "sel.last")
#         if not selected.strip():
#             messagebox.showerror("Error", "No contact selected.")
#             return

#         name = selected.split(" - ")[0].strip()
#         self.contacts = [c for c in self.contacts if c["name"] != name]
#         save_contacts(self.contacts)
#         self.refresh_contact_list()
#         messagebox.showinfo("Deleted", "Contact deleted successfully.")

#     def search_contact(self, event):
#         query = self.search_entry.get().strip().lower()
#         if not query:
#             self.refresh_contact_list()
#             return

#         filtered = [c for c in self.contacts if query in c["name"].lower() or query in c["phone"]]
#         self.refresh_contact_list(filtered)

#     def clear_entries(self):
#         self.name_entry.delete(0, 'end')
#         self.phone_entry.delete(0, 'end')
#         self.email_entry.delete(0, 'end')
#         self.address_entry.delete(0, 'end')


# if __name__ == "__main__":
#     app = ContactBook()
#     app.mainloop()

import customtkinter as ctk
from tkinter import messagebox
import json
import os

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

FILE_NAME = "contacts.json"

def fetch_data():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w') as file:
            json.dump([], file)
    with open(FILE_NAME, 'r') as file:
        return json.load(file)

def store_data(contacts):
    with open(FILE_NAME, 'w') as file:
        json.dump(contacts, file, indent=4)

class ContactManager(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Smart Contact Manager")
        self.geometry("720x500")
        self.resizable(False, False)
        self.data = fetch_data()
        self.setup_ui()
        self.show_contacts()

    def setup_ui(self):
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.pack(pady=15, padx=15, fill="x")

        self.name_input = ctk.CTkEntry(self.input_frame, placeholder_text="Full Name")
        self.name_input.grid(row=0, column=0, padx=8, pady=8)

        self.phone_input = ctk.CTkEntry(self.input_frame, placeholder_text="Phone Number")
        self.phone_input.grid(row=0, column=1, padx=8, pady=8)

        self.email_input = ctk.CTkEntry(self.input_frame, placeholder_text="Email Address")
        self.email_input.grid(row=1, column=0, padx=8, pady=8)

        self.address_input = ctk.CTkEntry(self.input_frame, placeholder_text="Home/Work Address")
        self.address_input.grid(row=1, column=1, padx=8, pady=8)

        self.save_btn = ctk.CTkButton(self.input_frame, text="Save Contact", command=self.save_contact)
        self.save_btn.grid(row=2, column=0, columnspan=2, pady=12)

        self.search_box = ctk.CTkEntry(self, placeholder_text="Search Name or Phone")
        self.search_box.pack(pady=10, padx=15, fill="x")
        self.search_box.bind("<KeyRelease>", self.search_data)

        self.display_box = ctk.CTkTextbox(self, width=680, height=180)
        self.display_box.pack(padx=15, pady=10)

        self.remove_btn = ctk.CTkButton(self, text="Remove Selected", command=self.remove_contact, fg_color="lightblue")
        self.remove_btn.pack(pady=10)

        self.load_btn = ctk.CTkButton(self, text="Load Selected", command=self.load_selected_contact)
        self.load_btn.pack(pady=5)


    def show_contacts(self, filtered=None):
        self.display_box.delete("0.0", "end")
        items = filtered if filtered is not None else self.data
        for item in items:
            entry = f"{item['name']} - {item['phone']}\n"
            self.display_box.insert("end", entry)

    def save_contact(self):
        name = self.name_input.get().strip()
        phone = self.phone_input.get().strip()
        email = self.email_input.get().strip()
        address = self.address_input.get().strip()

        if not name or not phone:
            messagebox.showwarning("Missing Info", "Name and phone number are required.")
            return

        updated = False
        for item in self.data:
            if item['phone'] == phone:
                item.update({"name": name, "email": email, "address": address})
                updated = True
                break

        if not updated:
            self.data.append({"name": name, "phone": phone, "email": email, "address": address})

        store_data(self.data)
        self.show_contacts()
        self.reset_fields()
        messagebox.showinfo("Success", "Contact saved!")

    def remove_contact(self):
        selection = self.display_box.get("sel.first", "sel.last")
        if not selection.strip():
            messagebox.showerror("Error", "No contact selected.")
            return

        selected_name = selection.split(" - ")[0].strip()
        self.data = [entry for entry in self.data if entry["name"] != selected_name]
        store_data(self.data)
        self.show_contacts()
        messagebox.showinfo("Deleted", "Contact removed.")

    def search_data(self, event):
        keyword = self.search_box.get().strip().lower()
        if not keyword:
            self.show_contacts()
            return
        results = [item for item in self.data if keyword in item["name"].lower() or keyword in item["phone"]]
        self.show_contacts(results)

    def reset_fields(self):
        self.name_input.delete(0, 'end')
        self.phone_input.delete(0, 'end')
        self.email_input.delete(0, 'end')
        self.address_input.delete(0, 'end')

    def load_selected_contact(self):
        selection = self.display_box.get("sel.first", "sel.last")
        if not selection.strip():
            messagebox.showerror("Error", "No contact selected.")
            return

        selected_name = selection.split(" - ")[0].strip()
        for entry in self.data:
            if entry["name"] == selected_name:
                self.name_input.delete(0, 'end')
                self.name_input.insert(0, entry["name"])
                self.phone_input.delete(0, 'end')
                self.phone_input.insert(0, entry["phone"])
                self.email_input.delete(0, 'end')
                self.email_input.insert(0, entry["email"])
                self.address_input.delete(0, 'end')
                self.address_input.insert(0, entry["address"])
                break


if __name__ == "__main__":
    app = ContactManager()
    app.mainloop()
