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
