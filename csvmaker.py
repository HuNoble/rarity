#!/usr/bin/env python

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  


import csv
import os
import datetime
import Tkinter

class Rarara(Tkinter.Tk):

	first_iteration_done = False
	
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()

	def add_new_row(self):
		path3 = os.getcwd()
		path3 = path3+"/"
		correct_input = True
		d = {}
		try:
			datein = self.date_entry_string.get()
			datetime.datetime.strptime(datein, '%Y/%m/%d')
			add_to_d = {"Date" : datein}
			d.update(add_to_d)
		except:
			print("You must provide a valid date in yyyy/mm/dd format!")
			correct_input = False
	
		try:
			title = self.title_entry_string.get()
			if not title:
				raise ValueError("Title can't be empty!")
			add_to_d = {"Title" : title}
			d.update(add_to_d)
		except ValueError as err:
			print(err)
			correct_input = False
	
		try:
			cweld = self.cweld_entry_string.get()
			add_to_d = {"Cweld" : int(cweld)}
			d.update(add_to_d)
		except:
			print("Cweld must be an integer!")
			correct_input = False
	
		try:
			url = self.url_entry_string.get()
			if not url:
				raise ValueError("Url can't be empty!")
			add_to_d = {"Url" : url}
			d.update(add_to_d)
		except ValueError as err:
			print(err)
			correct_input = False
	
		try:
			severity = self.severity_entry_string.get()
			if severity.upper() == 'INFO':
				severity = 'Info'
			elif severity.upper() == 'LOW':
				severity = "Low"
			elif severity.upper() == 'MEDIUM':
				severity = "Medium"
			elif severity.upper() == 'HIGH':
				severity = "High"
			elif severity.upper() == 'CRITICAL':
				severity = "Critical"
			else:
				raise ValueError('Severity must be Info, Low, Medium, High or Critical!')
			add_to_d = {"Severity" : severity}
			d.update(add_to_d)
		except ValueError as err:
			print(err)
			correct_input = False
	
		try:
			description = self.description_entry_string.get()
			if not description:
				raise ValueError("Description can't be empty!")
			add_to_d = {"Description" : description}
			d.update(add_to_d)
		except ValueError as err:
			print(err)
			correct_input = False
	
		try:
			mitigation = self.mitigation_entry_string.get()
			if not mitigation:
				raise ValueError("Mitigation can't be empty!")
			add_to_d = {"Mitigation" : mitigation}
			d.update(add_to_d)
		except ValueError as err:
			print(err)
			correct_input = False
	
		try:
			impact = self.impact_entry_string.get()
			if not impact:
				raise ValueError("Impact can't be empty!")
			add_to_d = {"Impact" : impact}
			d.update(add_to_d)
		except ValueError as err:
			print(err)
			correct_input = False
	
		try:
			references = self.refrences_entry_string.get()
			if not references:
				raise ValueError("References can't be empty!")
			add_to_d = {"References" : references}
			d.update(add_to_d)
		except ValueError as err:
			print(err)
			correct_input = False
	
		try:
			active = self.active_entry_string.get()
			if (active.upper() == 'TRUE') | (active.upper() == 'FALSE'):
				add_to_d = {"Active" : active}
				d.update(add_to_d)
			else:
				raise ValueError('Input must be y or n!')
		except ValueError as err:
			print(err)
			correct_input = False
	
		try:
			verified = self.verified_entry_string.get()
			if (verified.upper() == 'TRUE') | (verified.upper() == 'FALSE'):
				add_to_d = {"Verified" : verified}
				d.update(add_to_d)
			else:
				raise ValueError('Verified must be y or n!')
		except ValueError as err:
			print(err)
			correct_input = False
	
		try:
			falsepositive = self.falsepositive_entry_string.get()
			if (falsepositive.upper() == 'TRUE') | (falsepositive.upper() == 'FALSE'):
				add_to_d = {"FalsePositive" : falsepositive}
				d.update(add_to_d)
			else:
				raise ValueError('FalsePositive must be y or n!')
		except ValueError as err:
			print(err)
			correct_input = False
	
		try:
			duplicate = self.duplicate_entry_string.get()
			if (duplicate.upper() == 'TRUE') | (duplicate.upper() == 'FALSE'):
				add_to_d = {"Duplicate" : duplicate}
				d.update(add_to_d)
			else:
				raise ValueError('Duplicate must be y or n!')
		except ValueError as err:
			print(err)
			correct_input = False
	
		#print(d)
	
		if correct_input:
			global first_iteration_done
			if not self.first_iteration_done:
				with open(path3 + 'extend.csv', 'w') as fw:
					writer = csv.writer(fw, delimiter=',')
					writer.writerow(d.keys())
			self.first_iteration_done = True
	
			with open(path3 + 'extend.csv', 'a') as fw:
				writer = csv.writer(fw, delimiter=',')
				writer.writerow(d.values())
				print("Row saved.")
				self.date_entry_string.set("")
				self.title_entry_string.set("")
				self.cweld_entry_string.set("")
				self.url_entry_string.set("")
				self.severity_entry_string.set("")
				self.description_entry_string.set("")
				self.mitigation_entry_string.set("")
				self.impact_entry_string.set("")
				self.refrences_entry_string.set("")
				self.active_entry_string.set("")
				self.verified_entry_string.set("")
				self.falsepositive_entry_string.set("")
				self.duplicate_entry_string.set("")
		else:
			print("Row discarded.")
	
	def initialize(self):
		self.grid()
		self.maintitle_label_string = Tkinter.StringVar()
		maintitle_label = Tkinter.Label(self,textvariable=self.maintitle_label_string,anchor="w", font="Helvetica 15")
		maintitle_label.grid(column=0, row=0, columnspan=2, sticky='EW')
		self.maintitle_label_string.set(u"Fill in this form to create a finding!")
		
		self.date_label_string = Tkinter.StringVar()
		date_label = Tkinter.Label(self,textvariable=self.date_label_string,anchor="w", font="Helvetica 15")
		date_label.grid(column=0, row=1, columnspan=2, sticky='EW')
		self.date_label_string.set(u"Date: ")
		self.date_entry_string = Tkinter.StringVar()
		self.date_entry = Tkinter.Entry(self, textvariable=self.date_entry_string, font="Helvetica 15",)
		self.date_entry.grid(column=3, row=1, sticky='EW')
		
		self.title_label_string = Tkinter.StringVar()
		title_label = Tkinter.Label(self,textvariable=self.title_label_string,anchor="w", font="Helvetica 15")
		title_label.grid(column=0, row=2, columnspan=2, sticky='EW')
		self.title_label_string.set(u"Title: ")
		self.title_entry_string = Tkinter.StringVar()
		self.title_entry = Tkinter.Entry(self, textvariable=self.title_entry_string, font="Helvetica 15")
		self.title_entry.grid(column=3, row=2, sticky='EW')
		
		self.cweld_label_string = Tkinter.StringVar()
		cweld_label = Tkinter.Label(self,textvariable=self.cweld_label_string,anchor="w", font="Helvetica 15")
		cweld_label.grid(column=0, row=3, columnspan=2, sticky='EW')
		self.cweld_label_string.set(u"Cweld: ")
		self.cweld_entry_string = Tkinter.StringVar()
		self.cweld_entry = Tkinter.Entry(self, textvariable=self.cweld_entry_string, font="Helvetica 15")
		self.cweld_entry.grid(column=3, row=3, sticky='EW')
		
		self.url_label_string = Tkinter.StringVar()
		url_label = Tkinter.Label(self,textvariable=self.url_label_string,anchor="w", font="Helvetica 15")
		url_label.grid(column=0, row=4, columnspan=2, sticky='EW')
		self.url_label_string.set(u"Url: ")
		self.url_entry_string = Tkinter.StringVar()
		self.url_entry = Tkinter.Entry(self, textvariable=self.url_entry_string, font="Helvetica 15")
		self.url_entry.grid(column=3, row=4, sticky='EW')
		
		severity_list=['Info','Low','Medium','High','Critital']
		self.severity_label_string = Tkinter.StringVar()
		severity_label = Tkinter.Label(self,textvariable=self.severity_label_string,anchor="w", font="Helvetica 15")
		severity_label.grid(column=0, row=5, columnspan=2, sticky='EW')
		self.severity_label_string.set(u"Severity: ")
		self.severity_entry_string = Tkinter.StringVar()
		self.severity_entry = Tkinter.OptionMenu(self, self.severity_entry_string, *severity_list)
		self.severity_entry.config(font="Helvetica 15")
		severity_entry_dropdown = self.nametowidget(self.severity_entry.menuname)
		severity_entry_dropdown.config(font="Helvetica 15")
		self.severity_entry.grid(column=3, row=5, sticky='EW')
		
		self.description_label_string = Tkinter.StringVar()
		description_label = Tkinter.Label(self,textvariable=self.description_label_string,anchor="w", font="Helvetica 15")
		description_label.grid(column=0, row=6, columnspan=2, sticky='EW')
		self.description_label_string.set(u"Description: ")
		self.description_entry_string = Tkinter.StringVar()
		self.description_entry = Tkinter.Entry(self, textvariable=self.description_entry_string, font="Helvetica 15")
		self.description_entry.grid(column=3, row=6, sticky='EW')
		
		self.mitigation_label_string = Tkinter.StringVar()
		mitigation_label = Tkinter.Label(self,textvariable=self.mitigation_label_string,anchor="w", font="Helvetica 15")
		mitigation_label.grid(column=0, row=7, columnspan=2, sticky='EW')
		self.mitigation_label_string.set(u"Mitigation: ")
		self.mitigation_entry_string = Tkinter.StringVar()
		self.mitigation_entry = Tkinter.Entry(self, textvariable=self.mitigation_entry_string, font="Helvetica 15")
		self.mitigation_entry.grid(column=3, row=7, sticky='EW')
		
		self.impact_label_string = Tkinter.StringVar()
		impact_label = Tkinter.Label(self,textvariable=self.impact_label_string,anchor="w", font="Helvetica 15")
		impact_label.grid(column=0, row=8, columnspan=2, sticky='EW')
		self.impact_label_string.set(u"Impact: ")
		self.impact_entry_string = Tkinter.StringVar()
		self.impact_entry = Tkinter.Entry(self, textvariable=self.impact_entry_string, font="Helvetica 15")
		self.impact_entry.grid(column=3, row=8, sticky='EW')
		
		self.refrences_label_string = Tkinter.StringVar()
		refrences_label = Tkinter.Label(self,textvariable=self.refrences_label_string,anchor="w", font="Helvetica 15")
		refrences_label.grid(column=0, row=9, columnspan=2, sticky='EW')
		self.refrences_label_string.set(u"Refrences: ")
		self.refrences_entry_string = Tkinter.StringVar()
		self.refrences_entry = Tkinter.Entry(self, textvariable=self.refrences_entry_string, font="Helvetica 15")
		self.refrences_entry.grid(column=3, row=9, sticky='EW')
		
		y_or_n_list = ['True','False']
		self.active_label_string = Tkinter.StringVar()
		active_label = Tkinter.Label(self,textvariable=self.active_label_string,anchor="w", font="Helvetica 15")
		active_label.grid(column=0, row=10, columnspan=2, sticky='EW')
		self.active_label_string.set(u"Active: ")
		self.active_entry_string = Tkinter.StringVar()
		self.active_entry = Tkinter.OptionMenu(self, self.active_entry_string, *y_or_n_list)
		self.active_entry.config(font="Helvetica 15")
		active_entry_dropdown = self.nametowidget(self.active_entry.menuname)
		active_entry_dropdown.config(font="Helvetica 15")
		self.active_entry.grid(column=3, row=10, sticky='EW')
		
		self.verified_label_string = Tkinter.StringVar()
		verified_label = Tkinter.Label(self,textvariable=self.verified_label_string,anchor="w", font="Helvetica 15")
		verified_label.grid(column=0, row=11, columnspan=2, sticky='EW')
		self.verified_label_string.set(u"Verified: ")
		self.verified_entry_string = Tkinter.StringVar()
		self.verified_entry = Tkinter.OptionMenu(self, self.verified_entry_string, *y_or_n_list)
		self.verified_entry.config(font="Helvetica 15")
		active_verified_dropdown = self.nametowidget(self.verified_entry.menuname)
		active_verified_dropdown.config(font="Helvetica 15")
		self.verified_entry.grid(column=3, row=11, sticky='EW')
		
		self.falsepositive_label_string = Tkinter.StringVar()
		falsepositive_label = Tkinter.Label(self,textvariable=self.falsepositive_label_string,anchor="w", font="Helvetica 15")
		falsepositive_label.grid(column=0, row=12, columnspan=2, sticky='EW')
		self.falsepositive_label_string.set(u"FalsePositive: ")
		self.falsepositive_entry_string = Tkinter.StringVar()
		self.falsepositive_entry = Tkinter.OptionMenu(self, self.falsepositive_entry_string, *y_or_n_list)
		self.falsepositive_entry.config(font="Helvetica 15")
		active_falsepositive_dropdown = self.nametowidget(self.falsepositive_entry.menuname)
		active_falsepositive_dropdown.config(font="Helvetica 15")
		self.falsepositive_entry.grid(column=3, row=12, sticky='EW')
		
		self.duplicate_label_string = Tkinter.StringVar()
		duplicate_label = Tkinter.Label(self,textvariable=self.duplicate_label_string,anchor="w", font="Helvetica 15")
		duplicate_label.grid(column=0, row=13, columnspan=2, sticky='EW')
		self.duplicate_label_string.set(u"Duplicate: ")
		self.duplicate_entry_string = Tkinter.StringVar()
		self.duplicate_entry = Tkinter.OptionMenu(self, self.duplicate_entry_string, *y_or_n_list)
		self.duplicate_entry.config(font="Helvetica 15")
		active_duplicate_dropdown = self.nametowidget(self.duplicate_entry.menuname)
		active_duplicate_dropdown.config(font="Helvetica 15")
		self.duplicate_entry.grid(column=3, row=13, sticky='EW')
		
		validate_button = Tkinter.Button(self, text=u"Validate & Save",command=self.ValidateButtonClick, font="Helvetica 15")
		validate_button.grid(column=0,row=14)
		
		save_button = Tkinter.Button(self, text=u"Close", command=self.CloseButtonClick, font="Helvetica 15")
		save_button.grid(column=3,row=14)
		print("Welcome to Rarity - 'cause who the hell writes reports in the age of automation?")
		print('\n')
	
	def ValidateButtonClick(self):
		self.add_new_row()
	
	def CloseButtonClick(self):
		self.destroy()

if __name__ == "__main__":
	app = Rarara(None)
	app.title('Rarity')
	app.mainloop()
