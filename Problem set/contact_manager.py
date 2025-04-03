import tkinter as tk
from tkinter import messagebox
import json

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("750x550")  
        self.root.configure(bg="#F4F4F4")

        self.contacts = self.load_contacts()

        
        input_frame = tk.Frame(root, bg="white", bd=2, relief=tk.GROOVE)
        input_frame.pack(pady=10, padx=10, fill="x")

        labels = ["Name:", "Phone:", "Email:", "Address:"]
        self.entries = []
        for i, text in enumerate(labels):
            tk.Label(input_frame, text=text, font=("Arial", 12), bg="white").grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(input_frame, font=("Arial", 12), width=55)  # Increased width
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries.append(entry)

        # Buttons
        btn_frame = tk.Frame(root, bg="#F4F4F4")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", width=10, command=self.add_contact).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Update", font=("Arial", 12, "bold"), bg="#FFA500", fg="white", width=10, command=self.update_contact).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Delete", font=("Arial", 12, "bold"), bg="#E74C3C", fg="white", width=10, command=self.delete_contact).grid(row=0, column=2, padx=5, pady=5)

        self.search_entry = tk.Entry(root, font=("Arial", 12), width=55)  # Increased width
        self.search_entry.pack(pady=5)
        tk.Button(root, text="Search", font=("Arial", 12, "bold"), bg="#3498DB", fg="white", command=self.search_contact).pack()

        # Contact Listbox
        self.contact_listbox = tk.Listbox(root, font=("Courier", 12), height=12, width=95)  # Increased width
        self.contact_listbox.pack(pady=10, padx=10)
        self.contact_listbox.bind("<<ListboxSelect>>", self.load_selected_contact)

        self.refresh_list()

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self):
        name, phone, email, address = [entry.get().strip() for entry in self.entries]
        if name and phone:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            self.save_contacts()
            self.refresh_list()
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Name and Phone are required!")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0] - 2  
            if 0 <= index < len(self.contacts):
                self.contacts[index] = {"name": self.entries[0].get(), "phone": self.entries[1].get(), "email": self.entries[2].get(), "address": self.entries[3].get()}
                self.save_contacts()
                self.refresh_list()
                self.clear_entries()
        else:
            messagebox.showwarning("Update Error", "Select a contact to update.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0] - 2  
            if 0 <= index < len(self.contacts):
                del self.contacts[index]
                self.save_contacts()
                self.refresh_list()
                self.clear_entries()
        else:
            messagebox.showwarning("Delete Error", "Select a contact to delete.")

    def search_contact(self):
        query = self.search_entry.get().strip().lower()
        self.contact_listbox.delete(0, tk.END)
        self.contact_listbox.insert(tk.END, f"{'Name':<25}{'Phone':<20}{'Email':<35}{'Address'}")
        self.contact_listbox.insert(tk.END, "-" * 95)
        for contact in self.contacts:
            if query in contact["name"].lower() or query in contact["phone"]:
                self.contact_listbox.insert(tk.END, f"{contact['name']:<25}{contact['phone']:<20}{contact['email']:<35}{contact['address']}")

    def load_selected_contact(self, event):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0] - 2 
            if 0 <= index < len(self.contacts):
                contact = self.contacts[index]
                for i, key in enumerate(["name", "phone", "email", "address"]):
                    self.entries[i].delete(0, tk.END)
                    self.entries[i].insert(0, contact[key])

    def refresh_list(self):
        self.contact_listbox.delete(0, tk.END)
        self.contact_listbox.insert(tk.END, f"{'Name':<25}{'Phone':<20}{'Email':<35}{'Address'}")
        self.contact_listbox.insert(tk.END, "-" * 95)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['name']:<25}{contact['phone']:<20}{contact['email']:<35}{contact['address']}")

    def clear_entries(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

# Run the application
root = tk.Tk()
app = ContactBook(root)
root.mainloop()
